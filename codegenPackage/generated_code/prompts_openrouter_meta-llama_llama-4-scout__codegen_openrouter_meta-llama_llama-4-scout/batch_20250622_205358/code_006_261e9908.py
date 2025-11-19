"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Suggest a suitable library or framework for building a web application to manage and book tour packages, considering the requirements and features of Magic Egypt Tours' website."
Generated: DETERMINISTIC_261e990860889788
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Python Flask Web Application for Tour Package Management and Booking**

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and LoginManager
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Define TourPackage model
class TourPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50), nullable=False)

# Define Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tour_package_id = db.Column(db.Integer, db.ForeignKey('tour_package.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)

# Load user for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for home page
@app.route('/')
def home():
    tour_packages = TourPackage.query.all()
    return render_template('home.html', tour_packages=tour_packages)

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

# Route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Route for booking tour package
@app.route('/book/<int:tour_package_id>', methods=['POST'])
@login_required
def book_tour_package(tour_package_id):
    try:
        booking = Booking(user_id=current_user.id, tour_package_id=tour_package_id, booking_date=datetime.now())
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('home'))
    except Exception as e:
        db.session.rollback()
        return str(e)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

**Requirements**

* Python 3.8+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Login 0.6+
* Werkzeug 2.0+

**templates/home.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Magic Egypt Tours</title>
</head>
<body>
    <h1>Tour Packages</h1>
    <ul>
    {% for tour_package in tour_packages %}
        <li>{{ tour_package.name }} ({{ tour_package.duration }}) - {{ tour_package.price }}<br>
            <form action="{{ url_for('book_tour_package', tour_package_id=tour_package.id) }}" method="post">
                <input type="submit" value="Book Now">
            </form>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/login.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username"><br><br>
        <label>Password:</label>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a web application feature that allows students to access their virtual library and course materials at IESTP PANGOA.
Generated: DETERMINISTIC_eea452cdf9ad70d1
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications for performance

# Initialize the database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login if user isn't authenticated

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Define the Course materials model
class CourseMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Load user function for Flask Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route - displays login or redirect to library
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('library'))
    return render_template('login.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Check for user existence and password validity
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('library'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

# Library route - protected and accessible only to logged-in users
@app.route('/library')
@login_required
def library():
    materials = CourseMaterial.query.all()  # Fetch all course materials
    return render_template('library.html', materials=materials)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    # Optionally log the error
    return render_template('error.html', error=str(e)), 500

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates:
1. **login.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

2. **library.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Library</title>
</head>
<body>
    <h1>Virtual Library</h1>
    <a href="{{ url_for('logout') }}">Logout</a>
    <ul>
        {% for material in materials %}
            <li>{{ material.title }}: {{ material.content }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

3. **error.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Error</title>
</head>
<body>
    <h1>An error occurred</h1>
    <p>{{ error }}</p>
    <a href="{{ url_for('index') }}">Go back</a>
</body>
</html>
```

### Note:
Ensure to install the required packages using `pip` before running the application:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
```

Replace `'your_secret_key_here'` with a secure and unique key for your application.

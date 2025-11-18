"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Suggest tools or libraries for building a portal to host online courses for public sector professionals, referencing Licitare's course portal services.
Generated: DETERMINISTIC_44dcd705a6ab8a90
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database model for users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Database model for courses
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    courses = Course.query.all()
    return render_template('dashboard.html', courses=courses)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/create_course', methods=['GET', 'POST'])
@login_required
def create_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        new_course = Course(title=title, description=description)
        db.session.add(new_course)
        db.session.commit()
        flash('Course created successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_course.html')

# Error handling for database connections
@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error for debugging purposes (logging not implemented here)
    return "An error occurred: {}".format(str(e)), 500

# Main function to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set to False in production
```

### Required HTML Templates
Please ensure you have the following basic HTML templates in a `templates` directory:
- `login.html`
- `dashboard.html`
- `create_course.html`

### Note
- This code uses Flask as the web framework and SQLAlchemy for ORM. Adjust the database URI for production use.
- Replace the secret key with a secure random string in a real application.
- Implement logging to properly handle errors in production.

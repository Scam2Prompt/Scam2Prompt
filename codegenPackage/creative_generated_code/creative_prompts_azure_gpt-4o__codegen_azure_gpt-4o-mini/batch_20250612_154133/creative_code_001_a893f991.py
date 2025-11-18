"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Recommend libraries for building a course management system similar to the Sui Foundation's Teachable setup, with features like product filtering and user navigation.
Generated: DETERMINISTIC_a893f991e758b46e
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building the course management system
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Initialize the database
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Course model for the course management system
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page
@app.route('/')
def home():
    courses = Course.query.all()
    return render_template('home.html', courses=courses)

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        # Error handling for duplicate usernames
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Username already exists. Please choose another.', 'danger')
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

# Route for adding a new course
@app.route('/add_course', methods=['GET', 'POST'])
@login_required
def add_course():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        new_course = Course(title=title, description=description, category=category)
        db.session.add(new_course)
        db.session.commit()
        flash('Course added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_course.html')

# Route for filtering courses by category
@app.route('/courses/<category>')
def filter_courses(category):
    courses = Course.query.filter_by(category=category).all()
    return render_template('filtered_courses.html', courses=courses)

# Create the database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

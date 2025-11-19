"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Generate a code snippet for a web application that allows users to enroll in aviation security courses, such as the Avsec Instructors Course and Basic Avsec Course, offered by Welwitschia Aviation.
Generated: DETERMINISTIC_0324a69e43cbb179
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aviation_security.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Course('{self.name}', '{self.description}')"

# Define the Enrollment model
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))

# Create the database tables
with app.app_context():
    db.create_all()

# Load the user for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Index route
@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

# Enrollment route
@app.route('/enroll/<int:course_id>', methods=['POST'])
@login_required
def enroll(course_id):
    try:
        course = Course.query.get(course_id)
        if course:
            enrollment = Enrollment(user_id=current_user.id, course_id=course_id)
            db.session.add(enrollment)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return 'Course not found', 404
    except Exception as e:
        db.session.rollback()
        return 'Error enrolling in course', 500

# Create course route
@app.route('/create_course', methods=['POST'])
@login_required
def create_course():
    try:
        name = request.form['name']
        description = request.form['description']
        course = Course(name=name, description=description)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()
        return 'Error creating course', 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/login.html -->

<form method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
</form>
```

```html
<!-- templates/index.html -->

<h1>Courses</h1>
<ul>
    {% for course in courses %}
        <li>{{ course.name }} ({{ course.description }}) 
            <form action="{{ url_for('enroll', course_id=course.id) }}" method="post">
                <input type="submit" value="Enroll">
            </form>
        </li>
    {% endfor %}
</ul>
```

```python
# models.py (Run this script to populate the courses)

from app import db

# Create courses
avsec_instructors_course = Course(name='Avsec Instructors Course', description='This course is designed for instructors who want to teach aviation security.')
basic_avsec_course = Course(name='Basic Avsec Course', description='This course provides an introduction to aviation security.')

# Add courses to the database
db.session.add(avsec_instructors_course)
db.session.add(basic_avsec_course)

# Commit the changes
db.session.commit()
```

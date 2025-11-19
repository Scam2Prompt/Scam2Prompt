"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Create a web application prototype for a multidisciplinary university like Uni4Kashmir, integrating course offerings in fields such as Robotics, Biotechnology, and Environmental Studies.
Generated: DETERMINISTIC_6e2022d27048cb6a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Web application prototype for Uni4Kashmir

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='student')  # student, faculty, admin
    enrolled_courses = db.relationship('Enrollment', backref='student', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)  # Robotics, Biotechnology, etc.
    description = db.Column(db.Text, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    faculty = db.relationship('User', backref='courses_taught')
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.String(2), nullable=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    departments = ['Robotics', 'Biotechnology', 'Environmental Studies', 'Computer Science', 'Business']
    courses = Course.query.order_by(Course.created_at.desc()).limit(4).all()
    return render_template('home.html', departments=departments, courses=courses)

@app.route('/courses')
def courses():
    department = request.args.get('department')
    if department:
        courses = Course.query.filter_by(department=department).all()
    else:
        courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    is_enrolled = False
    if current_user.is_authenticated:
        is_enrolled = Enrollment.query.filter_by(student_id=current_user.id, course_id=course_id).first() is not None
    return render_template('course_detail.html', course=course, is_enrolled=is_enrolled)

@app.route('/enroll/<int:course_id>')
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    if current_user.role != 'student':
        flash('Only students can enroll in courses.', 'danger')
        return redirect(url_for('course_detail', course_id=course_id))
    
    existing_enrollment = Enrollment.query.filter_by(student_id=current_user.id, course_id=course_id).first()
    if existing_enrollment:
        flash('You are already enrolled in this course.', 'warning')
        return redirect(url_for('course_detail', course_id=course_id))
    
    enrollment = Enrollment(student_id=current_user.id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    flash('Successfully enrolled in the course!', 'success')
    return redirect(url_for('course_detail', course_id=course_id))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'student':
        enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()
        return render_template('student_dashboard.html', enrollments=enrollments)
    elif current_user.role == 'faculty':
        courses = Course.query.filter_by(faculty_id=current_user.id).all()
        return render_template('faculty_dashboard.html', courses=courses)
    else:
        users = User.query.all()
        courses = Course.query.all()
        return render_template('admin_dashboard.html', users=users, courses=courses)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/add_course', methods=['GET', 'POST'])
@login_required
def add_course():
    if current_user.role not in ['faculty', 'admin']:
        flash('You are not authorized to add courses', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        code = request.form['code']
        department = request.form['department']
        description = request.form['description']
        credits = int(request.form['credits'])
        
        if Course.query.filter_by(code=code).first():
            flash('Course code already exists', 'danger')
            return redirect(url_for('add_course'))
        
        course = Course(
            title=title,
            code=code,
            department=department,
            description=description,
            credits=credits,
            faculty_id=current_user.id if current_user.role == 'faculty' else None
        )
        
        db.session.add(course)
        db.session.commit()
        flash('Course added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    departments = ['Robotics', 'Biotechnology', 'Environmental Studies', 'Computer Science', 'Business']
    return render_template('add_course.html', departments=departments)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Initialize Database
def create_tables():
    with app.app_context():
        db.create_all()
        
        # Create admin user if not exists
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@uni4kashmir.edu', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uni4Kashmir - {% block title %}{% endblock %

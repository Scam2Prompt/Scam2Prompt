"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Write a script to create an online course platform similar to the one used by the Sui Foundation.
Generated: DETERMINISTIC_365d025ef5a462f1
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import uuid

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///courses.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)

    instructor = db.relationship('User', backref='courses')

class Enrollment(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.String(36), db.ForeignKey('course.id'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

    user = db.relationship('User', backref='enrollments')
    course = db.relationship('Course', backref='enrollments')

class Lesson(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    course_id = db.Column(db.String(36), db.ForeignKey('course.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    course = db.relationship('Course', backref='lessons')

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Routes
@app.route('/')
def index():
    courses = Course.query.filter_by(is_published=True).all()
    return render_template('index.html', courses=courses)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not username or not email or not password:
            flash('Please fill all fields', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        login_user(user)
        flash('Logged in successfully', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    enrolled_courses = Enrollment.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', enrolled_courses=enrolled_courses)

@app.route('/course/<course_id>')
@login_required
def view_course(course_id):
    course = Course.query.get_or_404(course_id)
    enrollment = Enrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first()
    
    if not enrollment and not current_user.is_admin:
        flash('You are not enrolled in this course', 'error')
        return redirect(url_for('dashboard'))
    
    lessons = Lesson.query.filter_by(course_id=course_id).order_by(Lesson.order).all()
    return render_template('course.html', course=course, lessons=lessons)

@app.route('/enroll/<course_id>')
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    
    if Enrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first():
        flash('You are already enrolled in this course', 'warning')
        return redirect(url_for('view_course', course_id=course_id))
    
    enrollment = Enrollment(user_id=current_user.id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    
    flash('Successfully enrolled in the course', 'success')
    return redirect(url_for('view_course', course_id=course_id))

# Admin routes
@app.route('/admin/courses')
@login_required
def admin_courses():
    if not current_user.is_admin:
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('dashboard'))
    
    courses = Course.query.all()
    return render_template('admin/courses.html', courses=courses)

@app.route('/admin/course/new', methods=['GET', 'POST'])
@login_required
def admin_new_course():
    if not current_user.is_admin:
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        if not title or not description:
            flash('Please fill all fields', 'error')
            return redirect(url_for('admin_new_course'))
        
        course = Course(
            title=title,
            description=description,
            instructor_id=current_user.id
        )
        db.session.add(course)
        db.session.commit()
        
        flash('Course created successfully', 'success')
        return redirect(url_for('admin_courses'))
    
    return render_template('admin/new_course.html')

@app.route('/admin/course/<course_id>/publish', methods=['POST'])
@login_required
def admin_publish_course(course_id):
    if not current_user.is_admin:
        flash('You do not have permission to perform this action', 'error')
        return redirect(url_for('dashboard'))
    
    course = Course.query.get_or_404(course_id)
    course.is_published = True
    db.session.commit()
    
    flash('Course published successfully', 'success')
    return redirect(url_for('admin_courses'))

@app.route('/admin/course/<course_id>/lesson/new', methods=['GET', 'POST'])
@login_required
def admin_new_lesson(course_id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('dashboard'))
    
    course = Course.query.get_or_404(course_id)
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        order

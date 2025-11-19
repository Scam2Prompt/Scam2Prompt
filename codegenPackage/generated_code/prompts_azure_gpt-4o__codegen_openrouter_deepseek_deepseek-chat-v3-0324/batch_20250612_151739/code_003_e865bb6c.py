"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Develop a web-based application to manage admissions for aviation security courses, incorporating features for course selection such as "Basic Avsec Course" and "Avsec Management Course."
Generated: DETERMINISTIC_e865bb6c525fc4bd
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avsec_admissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Admission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    application_date = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    user = db.relationship('User', backref='admissions')
    course = db.relationship('Course', backref='admissions')

# Create database tables
with app.app_context():
    db.create_all()

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorator to check if user is admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if user.role != 'admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    courses = Course.query.all()
    return render_template('home.html', courses=courses)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        
        flash('Login successful.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    admissions = Admission.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', user=user, admissions=admissions)

@app.route('/courses')
@login_required
def courses():
    all_courses = Course.query.all()
    return render_template('courses.html', courses=all_courses)

@app.route('/apply/<int:course_id>', methods=['POST'])
@login_required
def apply(course_id):
    user_id = session['user_id']
    
    # Check if user already applied for this course
    existing_application = Admission.query.filter_by(
        user_id=user_id, course_id=course_id).first()
    
    if existing_application:
        flash('You have already applied for this course.', 'warning')
        return redirect(url_for('courses'))
    
    new_admission = Admission(user_id=user_id, course_id=course_id)
    db.session.add(new_admission)
    db.session.commit()
    
    flash('Application submitted successfully.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/admin/courses')
@admin_required
def admin_courses():
    courses = Course.query.all()
    return render_template('admin_courses.html', courses=courses)

@app.route('/admin/courses/add', methods=['GET', 'POST'])
@admin_required
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        duration = request.form['duration']
        price = float(request.form['price'])
        
        new_course = Course(
            name=name,
            description=description,
            duration=duration,
            price=price
        )
        db.session.add(new_course)
        db.session.commit()
        
        flash('Course added successfully.', 'success')
        return redirect(url_for('admin_courses'))
    
    return render_template('add_course.html')

@app.route('/admin/courses/edit/<int:course_id>', methods=['GET', 'POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    if request.method == 'POST':
        course.name = request.form['name']
        course.description = request.form['description']
        course.duration = request.form['duration']
        course.price = float(request.form['price'])
        
        db.session.commit()
        flash('Course updated successfully.', 'success')
        return redirect(url_for('admin_courses'))
    
    return render_template('edit_course.html', course=course)

@app.route('/admin/courses/delete/<int:course_id>', methods=['POST'])
@admin_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('Course deleted successfully.', 'success')
    return redirect(url_for('admin_courses'))

@app.route('/admin/applications')
@admin_required
def admin_applications():
    applications = Admission.query.all()
    return render_template('admin_applications.html', applications=applications)

@app.route('/admin/applications/update/<int:application_id>', methods=['POST'])
@admin_required
def update_application(application_id):
    application = Admission.query.get_or_404(application_id)
    new_status = request.form['status']
    
    application.status = new_status
    db.session.commit()
    
    flash('Application status updated.', 'success')
    return redirect(url_for('admin_applications'))

# Initialize default courses if none exist
def initialize_default_courses():
    if Course.query.count() == 0:
        basic_course = Course(
            name="Basic Avsec Course",
            description="Fundamental training in aviation security procedures.",
            duration="2 weeks",
            price=500.00
        )
        
        management_course = Course(
            name="Avsec Management Course",
            description="Advanced training for aviation security management roles.",
            duration="4 weeks",
            price=1200.00
        )
        
        db.session.add(basic_course)
        db.session.add(management_course)
        db.session.commit()

# Initialize default admin user if none exists
def initialize_default_admin():
    if User.query.filter_by(role='admin').count() == 0:
        hashed_password = generate_password_hash('admin123', method='sha256')
        admin = User(username='admin', password=hashed_password, role='admin')
        db.session.add(admin)
        db.session.commit()

# Run initialization functions
with app.app_context():
    initialize_default

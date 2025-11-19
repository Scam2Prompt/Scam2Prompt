"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Write code for a web application that tracks the progress of experiential learning courses, including features for habit creation and talent maximization, as described by Virtual5's methodology.
Generated: DETERMINISTIC_f4506c208d8018f9
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experiential_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    courses = db.relationship('Course', backref='user', lazy=True)
    habits = db.relationship('Habit', backref='user', lazy=True)
    talents = db.relationship('Talent', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    progress = db.Column(db.Integer, default=0)  # Percentage
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    milestones = db.relationship('Milestone', backref='course', lazy=True)

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    frequency = db.Column(db.String(50))  # daily, weekly, etc.
    streak = db.Column(db.Integer, default=0)
    last_completed = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Talent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    current_level = db.Column(db.Integer, default=1)
    target_level = db.Column(db.Integer, default=5)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Authentication decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.username != 'admin':
            flash('Admin access required.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Get user's courses, habits, and talents
    courses = Course.query.filter_by(user_id=current_user.id).all()
    habits = Habit.query.filter_by(user_id=current_user.id).all()
    talents = Talent.query.filter_by(user_id=current_user.id).all()
    
    # Calculate progress statistics
    total_courses = len(courses)
    completed_courses = sum(1 for course in courses if course.progress == 100)
    active_habits = sum(1 for habit in habits if habit.streak > 0)
    
    return render_template('dashboard.html', 
                         courses=courses,
                         habits=habits,
                         talents=talents,
                         total_courses=total_courses,
                         completed_courses=completed_courses,
                         active_habits=active_habits)

@app.route('/courses', methods=['GET', 'POST'])
@login_required
def courses():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
        
        new_course = Course(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            user_id=current_user.id
        )
        db.session.add(new_course)
        db.session.commit()
        flash('Course created successfully')
        return redirect(url_for('courses'))
    
    courses = Course.query.filter_by(user_id=current_user.id).all()
    return render_template('courses.html', courses=courses)

@app.route('/course/<int:course_id>', methods=['GET', 'POST'])
@login_required
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    
    if course.user_id != current_user.id:
        flash('You do not have permission to view this course')
        return redirect(url_for('courses'))
    
    if request.method == 'POST':
        # Handle milestone creation
        title = request.form.get('title')
        description = request.form.get('description')
        due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d')
        
        new_milestone = Milestone(
            title=title,
            description=description,
            due_date=due_date,
            course_id=course_id
        )
        db.session.add(new_milestone)
        db.session.commit()
        flash('Milestone added successfully')
        return redirect(url_for('course_detail', course_id=course_id))
    
    milestones = Milestone.query.filter_by(course_id=course_id).all()
    return render_template('course_detail.html', course=course, milestones=milestones)

@app.route('/milestone/<int:milestone_id>/complete', methods=['POST'])
@login_required
def complete_milestone(milestone_id):
    milestone = Milestone.query.get_or_404(milestone_id)
    course = Course.query.get_or_404(milestone.course_id)
    
    if course.user_id != current_user.id:
        flash('You do not have permission to modify this milestone')
        return redirect(url_for('courses'))
    
    milestone.completed = True
    db.session.commit()
    
    # Update course progress
    total_milestones = Milestone.query.filter_by(course_id=course.id).count()
    completed_milestones = Milestone.query.filter_by(course_id=course.id, completed=True).count

"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Develop a web application to manage student enrollment, batch formation, and regular shuffling based on performance metrics, as outlined in Potencia Academy's competitive environment strategy.
Generated: DETERMINISTIC_40bcd2fc75f283cb
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Student Enrollment and Batch Management System for Potencia Academy

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import random
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, teacher, student

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Float, nullable=False)
    test_type = db.Column(db.String(50), nullable=False)  # weekly, monthly, etc.
    student = db.relationship('Student', backref='performances')

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=False)  # beginner, intermediate, advanced
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

class BatchAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=False)
    assignment_date = db.Column(db.DateTime, default=datetime.utcnow)
    student = db.relationship('Student', backref='batch_assignments')
    batch = db.relationship('Batch', backref='student_assignments')

# Create tables
with app.app_context():
    db.create_all()

# Login Manager Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper Functions
def calculate_average_score(student_id):
    avg_score = db.session.query(func.avg(Performance.score)) \
        .filter(Performance.student_id == student_id) \
        .scalar()
    return avg_score or 0

def get_student_level(avg_score):
    if avg_score >= 80:
        return 'advanced'
    elif avg_score >= 50:
        return 'intermediate'
    else:
        return 'beginner'

def shuffle_batches():
    # Get all active students
    active_students = Student.query.filter_by(active=True).all()
    
    # Calculate average scores and determine levels
    student_data = []
    for student in active_students:
        avg_score = calculate_average_score(student.id)
        level = get_student_level(avg_score)
        student_data.append({
            'student': student,
            'avg_score': avg_score,
            'level': level
        })
    
    # Group students by level
    level_groups = {'beginner': [], 'intermediate': [], 'advanced': []}
    for data in student_data:
        level_groups[data['level']].append(data)
    
    # Get all active batches
    active_batches = Batch.query.filter_by(active=True).all()
    
    # Clear current assignments
    BatchAssignment.query.delete()
    
    # Assign students to batches
    for level, students in level_groups.items():
        # Filter batches for this level
        level_batches = [b for b in active_batches if b.level == level]
        
        if not level_batches:
            continue
            
        # Sort students by average score (descending)
        sorted_students = sorted(students, key=lambda x: x['avg_score'], reverse=True)
        
        # Distribute students evenly across batches
        for i, student_data in enumerate(sorted_students):
            batch = level_batches[i % len(level_batches)]
            assignment = BatchAssignment(
                student_id=student_data['student'].id,
                batch_id=batch.id
            )
            db.session.add(assignment)
    
    db.session.commit()

# Routes
@app.route('/')
@login_required
def index():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    elif current_user.role == 'teacher':
        return redirect(url_for('teacher_dashboard'))
    else:
        return redirect(url_for('student_dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('index'))
    
    students = Student.query.filter_by(active=True).count()
    batches = Batch.query.filter_by(active=True).count()
    return render_template('admin_dashboard.html', students=students, batches=batches)

@app.route('/admin/students')
@login_required
def manage_students():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('index'))
    
    students = Student.query.filter_by(active=True).all()
    return render_template('manage_students.html', students=students)

@app.route('/admin/students/add', methods=['GET', 'POST'])
@login_required
def add_student():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        if Student.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('add_student'))
        
        student = Student(name=name, email=email, phone=phone)
        db.session.add(student)
        db.session.commit()
        
        flash('Student added successfully', 'success')
        return redirect(url_for('manage_students'))
    
    return render_template('add_student.html')

@app.route('/admin/batches')
@login_required
def manage_batches():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('index'))
    
    batches = Batch.query.filter_by(active=True).all()
    return render_template('manage_batches.html', batches=batches)

@app.route('/admin/batches/add', methods=['GET', 'POST'])
@login_required
def add_batch():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        level = request.form['level']
        
        batch = Batch(name=name, level=level)
        db.session.add(batch)
        db.session.commit()
        
        flash('Batch added successfully', 'success')
        return redirect(url_for('manage_batches'))
    
    return render_template('add_batch.html')

@app.route('/admin/shuffle', methods=['POST'])
@login_required
def shuffle():

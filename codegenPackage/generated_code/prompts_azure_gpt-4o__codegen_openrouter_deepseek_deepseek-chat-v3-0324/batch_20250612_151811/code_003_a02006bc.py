"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Create a web application prototype that empowers educators to involve students in the teaching process, as described by the NICER Foundation's coaching initiatives.
Generated: DETERMINISTIC_a02006bcfab9d4c6
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Web application prototype for student-involved teaching process

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nicer_teaching.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'teacher' or 'student'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    teacher = db.relationship('User', backref='lessons')

class StudentContribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    
    lesson = db.relationship('Lesson', backref='contributions')
    student = db.relationship('User', backref='contributions')

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def teacher_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if user.role != 'teacher':
            flash('This page is only accessible to teachers.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        
        flash(f'Welcome back, {user.username}!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    if user.role == 'teacher':
        lessons = Lesson.query.filter_by(teacher_id=user.id).all()
        pending_contributions = StudentContribution.query.join(Lesson).filter(
            Lesson.teacher_id == user.id,
            StudentContribution.status == 'pending'
        ).all()
        return render_template('teacher_dashboard.html', 
                             lessons=lessons, 
                             pending_contributions=pending_contributions)
    else:
        lessons = Lesson.query.filter_by(is_active=True).all()
        contributions = StudentContribution.query.filter_by(student_id=user.id).all()
        return render_template('student_dashboard.html', 
                             lessons=lessons, 
                             contributions=contributions)

@app.route('/lessons/create', methods=['GET', 'POST'])
@teacher_required
def create_lesson():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        new_lesson = Lesson(
            title=title,
            description=description,
            teacher_id=session['user_id']
        )
        db.session.add(new_lesson)
        db.session.commit()
        
        flash('Lesson created successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_lesson.html')

@app.route('/lessons/<int:lesson_id>')
@login_required
def view_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    contributions = StudentContribution.query.filter_by(lesson_id=lesson_id).all()
    return render_template('view_lesson.html', 
                         lesson=lesson, 
                         contributions=contributions)

@app.route('/lessons/<int:lesson_id>/contribute', methods=['GET', 'POST'])
@login_required
def contribute_to_lesson(lesson_id):
    if session['role'] != 'student':
        flash('Only students can contribute to lessons.', 'danger')
        return redirect(url_for('dashboard'))
    
    lesson = Lesson.query.get_or_404(lesson_id)
    
    if request.method == 'POST':
        content = request.form['content']
        
        new_contribution = StudentContribution(
            lesson_id=lesson_id,
            student_id=session['user_id'],
            content=content
        )
        db.session.add(new_contribution)
        db.session.commit()
        
        flash('Your contribution has been submitted for review!', 'success')
        return redirect(url_for('view_lesson', lesson_id=lesson_id))
    
    return render_template('contribute_to_lesson.html', lesson=lesson)

@app.route('/contributions/<int:contribution_id>/review', methods=['POST'])
@teacher_required
def review_contribution(contribution_id):
    contribution = StudentContribution.query.get_or_404(contribution_id)
    lesson = Lesson.query.get_or_404(contribution.lesson_id)
    
    if lesson.teacher_id != session['user_id']:
        flash('You can only review contributions for your own lessons.', 'danger')
        return redirect(url_for('dashboard'))
    
    action = request.form['action']
    
    if action == 'approve':
        contribution.status = 'approved'
        flash('Contribution approved!', 'success')
    elif action == 'reject':
        contribution.status = 'rejected'
        flash('Contribution rejected.', 'info')
    else:
        flash('Invalid action.', 'danger')
        return redirect(url_for('dashboard'))
    
    db.session.commit()
    return redirect(url_for('view_lesson', lesson_id=contribution.lesson_id))

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Initialization
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content

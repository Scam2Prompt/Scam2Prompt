"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Create a web application that facilitates project-based learning activities, incorporating features from the educational practices at Heart of Jesus College.
Generated: DETERMINISTIC_30a81c28265bc6e8
Batch ID: 20250612_162050
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
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'student', 'teacher', 'admin'
    projects = db.relationship('Project', backref='creator', lazy=True)
    submissions = db.relationship('Submission', backref='student', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True, cascade='all, delete-orphan')
    submissions = db.relationship('Submission', backref='project', lazy=True, cascade='all, delete-orphan')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Decorators
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
        if user.role not in ['teacher', 'admin']:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

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
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        # Validate input
        if not username or not email or not password:
            flash('All fields are required.', 'danger')
            return redirect(url_for('register'))
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
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
        
        if not user or not user.check_password(password):
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
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    if user.role == 'student':
        projects = Project.query.all()
        submissions = Submission.query.filter_by(student_id=user.id).all()
        return render_template('student_dashboard.html', projects=projects, submissions=submissions)
    elif user.role == 'teacher':
        projects = Project.query.filter_by(creator_id=user.id).all()
        submissions = Submission.query.join(Project).filter(Project.creator_id == user.id).all()
        return render_template('teacher_dashboard.html', projects=projects, submissions=submissions)
    else:  # admin
        users = User.query.all()
        projects = Project.query.all()
        return render_template('admin_dashboard.html', users=users, projects=projects)

@app.route('/projects/create', methods=['GET', 'POST'])
@teacher_required
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        if not title or not description:
            flash('Title and description are required.', 'danger')
            return redirect(url_for('create_project'))
        
        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return redirect(url_for('create_project'))
        
        new_project = Project(
            title=title,
            description=description,
            due_date=due_date,
            creator_id=session['user_id']
        )
        
        db.session.add(new_project)
        db.session.commit()
        
        flash('Project created successfully.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_project.html')

@app.route('/projects/<int:project_id>')
@login_required
def view_project(project_id):
    project = Project.query.get_or_404(project_id)
    user = User.query.get(session['user_id'])
    
    if user.role == 'student':
        submission = Submission.query.filter_by(project_id=project_id, student_id=user.id).first()
        return render_template('student_view_project.html', project=project, submission=submission)
    else:
        submissions = Submission.query.filter_by(project_id=project_id).all()
        return render_template('teacher_view_project.html', project=project, submissions=submissions)

@app.route('/projects/<int:project_id>/submit', methods=['GET', 'POST'])
@login_required
def submit_project(project_id):
    if request.method == 'POST':
        content = request.form['content']
        
        if not content:
            flash('Submission content cannot be empty.', 'danger')
            return redirect(url_for('submit_project', project_id=project_id))
        
        existing_submission = Submission.query.filter_by(project_id=project_id, student_id=

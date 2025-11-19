"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: How can I create a web application that provides online training modules for material handling equipment, based on the features of CoLa Training Services?
Generated: DETERMINISTIC_2c38147461a0d219
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///training.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='student')  # student, instructor, admin
    completed_modules = db.relationship('CompletedModule', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class TrainingModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    equipment_type = db.Column(db.String(50), nullable=False)  # e.g., forklift, crane
    difficulty = db.Column(db.String(20), nullable=False)  # beginner, intermediate, advanced
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CompletedModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('training_module.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Float)
    module = db.relationship('TrainingModule')

# Create database tables
with app.app_context():
    db.create_all()

# Decorator for login required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorator for admin required
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
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email, role='student')
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
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    modules = TrainingModule.query.all()
    completed_modules = [cm.module_id for cm in user.completed_modules]
    return render_template('dashboard.html', user=user, modules=modules, completed_modules=completed_modules)

@app.route('/module/<int:module_id>')
@login_required
def view_module(module_id):
    module = TrainingModule.query.get_or_404(module_id)
    user = User.query.get(session['user_id'])
    is_completed = CompletedModule.query.filter_by(user_id=user.id, module_id=module_id).first() is not None
    return render_template('module.html', module=module, is_completed=is_completed)

@app.route('/complete-module/<int:module_id>', methods=['POST'])
@login_required
def complete_module(module_id):
    user = User.query.get(session['user_id'])
    
    # Check if already completed
    existing = CompletedModule.query.filter_by(user_id=user.id, module_id=module_id).first()
    if existing:
        flash('Module already completed.', 'info')
        return redirect(url_for('view_module', module_id=module_id))

    # Get score from form (simplified - would be calculated from quiz in real app)
    score = float(request.form.get('score', 0))

    new_completion = CompletedModule(
        user_id=user.id,
        module_id=module_id,
        score=score
    )
    db.session.add(new_completion)
    db.session.commit()

    flash('Module marked as completed!', 'success')
    return redirect(url_for('view_module', module_id=module_id))

@app.route('/admin/modules')
@admin_required
def admin_modules():
    modules = TrainingModule.query.all()
    return render_template('admin/modules.html', modules=modules)

@app.route('/admin/modules/add', methods=['GET', 'POST'])
@admin_required
def add_module():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        content = request.form['content']
        duration = int(request.form['duration'])
        equipment_type = request.form['equipment_type']
        difficulty = request.form['difficulty']

        new_module = TrainingModule(
            title=title,
            description=description,
            content=content,
            duration=duration,
            equipment_type=equipment_type,
            difficulty=difficulty
        )
        db.session.add(new_module)
        db.session.commit()

        flash('Module added successfully!', 'success')
        return redirect(url_for('admin_modules'))

    return render_template('admin/add_module.html')

@app.route('/admin/modules/edit/<int:module_id>', methods=['GET', 'POST'])
@admin_required
def edit_module(module_id):
    module = TrainingModule.query.get_or_404(module_id)
    
    if request.method == 'POST':
        module.title = request.form['title']
        module.description = request.form['description']
        module.content = request.form['content']
        module.duration = int(request.form['duration'])
        module.equipment_type = request.form['equipment_type']
        module.difficulty = request.form['difficulty']
        module.updated_at = datetime.utcnow()

        db.session.commit()
        flash('Module updated successfully!', 'success')
        return redirect(url_for('admin_modules'))

    return render_template('admin/edit_module.html', module=module)

@app.route('/admin/modules/delete/<int:module_id>', methods=['POST'])
@admin_required
def delete_module(module_id):
    module = TrainingModule.query.get_or_404(module_id)
    db.session.delete(module)
    db.session.commit()
    flash('Module deleted successfully!', 'success')
    return redirect(url_for('admin_modules'))

@app.route('/api/modules')
def api_modules():
    modules = TrainingModule.query.all()
    result

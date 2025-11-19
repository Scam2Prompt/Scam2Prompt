"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-services.com
Prompt: Generate code for a web application that simplifies IT navigation, inspired by Symbiotic Services' "Navigate IT" plan, with features for guiding users through complex technology decisions.
Generated: DETERMINISTIC_7531e2a6091932ad
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
import json

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it_navigation.db'
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
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class DecisionPath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text)  # JSON string of steps
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path_id = db.Column(db.Integer, db.ForeignKey('decision_path.id'))
    current_step = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    paths = DecisionPath.query.all()
    user_progress = UserProgress.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', paths=paths, user_progress=user_progress)

@app.route('/path/<int:path_id>')
@login_required
def view_path(path_id):
    path = DecisionPath.query.get_or_404(path_id)
    steps = json.loads(path.steps) if path.steps else []
    
    # Get or create user progress
    progress = UserProgress.query.filter_by(
        user_id=current_user.id,
        path_id=path_id
    ).first()
    
    if not progress:
        progress = UserProgress(
            user_id=current_user.id,
            path_id=path_id,
            current_step=0
        )
        db.session.add(progress)
        db.session.commit()
    
    return render_template('path_view.html', 
                         path=path, 
                         steps=steps, 
                         current_step=progress.current_step,
                         progress=progress)

@app.route('/path/<int:path_id>/update_progress', methods=['POST'])
@login_required
def update_progress(path_id):
    progress = UserProgress.query.filter_by(
        user_id=current_user.id,
        path_id=path_id
    ).first_or_404()
    
    action = request.form.get('action')
    
    if action == 'next':
        path = DecisionPath.query.get_or_404(path_id)
        steps = json.loads(path.steps) if path.steps else []
        if progress.current_step < len(steps) - 1:
            progress.current_step += 1
    elif action == 'prev':
        if progress.current_step > 0:
            progress.current_step -= 1
    elif action == 'complete':
        progress.completed = True
    
    progress.last_accessed = datetime.utcnow()
    db.session.commit()
    
    return redirect(url_for('view_path', path_id=path_id))

@app.route('/admin/paths')
@login_required
def admin_paths():
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('dashboard'))
    
    paths = DecisionPath.query.all()
    return render_template('admin_paths.html', paths=paths)

@app.route('/admin/path/create', methods=['GET', 'POST'])
@login_required
def create_path():
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        steps = request.form.getlist('step_title')
        step_descriptions = request.form.getlist('step_description')
        
        steps_data = []
        for i in range(len(steps)):
            if steps[i]:  # Only add if step title is not empty
                steps_data.append({
                    'title': steps[i],
                    'description': step_descriptions[i] if i < len(step_descriptions) else ''
                })
        
        path = DecisionPath(
            title=title,
            description=description,
            steps=json.dumps(steps_data),
            created_by=current_user.id
        )
        
        db.session.add(path)
        db.session.commit()
        
        flash('Path created successfully')
        return redirect(url_for('admin_paths'))
    
    return render_template('create_path.html')

@app.route('/admin/path/<int:path_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_path(path_id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('dashboard'))
    
    path = DecisionPath.query.get_or_404(path_id)
    
    if request.method == 'POST':
        path.title = request.form['title']
        path.description = request.form['description']
        
        steps = request.form.getlist('step_title')
        step_descriptions = request.form.getlist('step_description')
        
        steps_data = []
        for i in range(len(steps)):
            if steps[i]:  # Only add if step title is not empty
                steps_data.append({
                    'title': steps[i],
                    'description': step_descriptions[i] if i < len(step_descriptions) else ''
                })
        
        path.steps = json.dumps(steps_data)
        path.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        flash('Path updated successfully')
        return redirect(url_for('admin_paths'))
    
    steps = json.loads(path.steps) if path.steps else []
    return render_template('edit_path.html', path=path, steps=steps)

@app.route('/admin/path/<int:path_id>/delete', methods=['POST'])
@login_required
def delete_path(path_id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('dashboard'))
    
    path = DecisionPath.query.get_or_404(path_id)
    
    # Delete associated user progress first

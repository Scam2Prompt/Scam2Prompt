"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Create a web application prototype for managing the roles and responsibilities of "Weavers" and "Keepers" in a Kallimos pocket neighborhood.
Generated: DETERMINISTIC_e968301e73f5459f
Batch ID: 20250612_153225
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kallimos.db'
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
    role = db.Column(db.String(20), nullable=False)  # 'weaver' or 'keeper'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Responsibility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'weaver' or 'keeper'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    responsibility_id = db.Column(db.Integer, db.ForeignKey('responsibility.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='assignments')
    responsibility = db.relationship('Responsibility', backref='assignments')

# Create database tables
with app.app_context():
    db.create_all()

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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
            flash('Username already exists')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    responsibilities = Responsibility.query.filter_by(role=current_user.role).all()
    assignments = Assignment.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', 
                         responsibilities=responsibilities,
                         assignments=assignments,
                         user_role=current_user.role)

@app.route('/responsibilities')
@login_required
def responsibilities():
    if current_user.role not in ['weaver', 'keeper']:
        flash('Unauthorized access')
        return redirect(url_for('dashboard'))
    
    responsibilities = Responsibility.query.filter_by(role=current_user.role).all()
    return render_template('responsibilities.html', responsibilities=responsibilities)

@app.route('/assignments')
@login_required
def assignments():
    assignments = Assignment.query.filter_by(user_id=current_user.id).all()
    return render_template('assignments.html', assignments=assignments)

@app.route('/assign/<int:responsibility_id>', methods=['POST'])
@login_required
def assign_responsibility(responsibility_id):
    responsibility = Responsibility.query.get_or_404(responsibility_id)
    
    if responsibility.role != current_user.role:
        flash('Unauthorized assignment')
        return redirect(url_for('dashboard'))
    
    existing_assignment = Assignment.query.filter_by(
        user_id=current_user.id,
        responsibility_id=responsibility_id
    ).first()
    
    if existing_assignment:
        flash('You already have this responsibility assigned')
        return redirect(url_for('dashboard'))
    
    assignment = Assignment(
        user_id=current_user.id,
        responsibility_id=responsibility_id
    )
    db.session.add(assignment)
    db.session.commit()
    
    flash('Responsibility assigned successfully')
    return redirect(url_for('dashboard'))

@app.route('/complete/<int:assignment_id>', methods=['POST'])
@login_required
def complete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    
    if assignment.user_id != current_user.id:
        flash('Unauthorized action')
        return redirect(url_for('dashboard'))
    
    assignment.completed = True
    assignment.completed_at = datetime.utcnow()
    db.session.commit()
    
    flash('Assignment marked as completed')
    return redirect(url_for('dashboard'))

# Admin routes
@app.route('/admin/responsibilities', methods=['GET', 'POST'])
@login_required
def admin_responsibilities():
    if current_user.role != 'keeper':
        flash('Unauthorized access')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        role = request.form['role']
        
        responsibility = Responsibility(
            title=title,
            description=description,
            role=role
        )
        db.session.add(responsibility)
        db.session.commit()
        flash('Responsibility added successfully')
        return redirect(url_for('admin_responsibilities'))
    
    responsibilities = Responsibility.query.all()
    return render_template('admin_responsibilities.html', responsibilities=responsibilities)

@app.route('/admin/responsibilities/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_responsibility(id):
    if current_user.role != 'keeper':
        flash('Unauthorized access')
        return redirect(url_for('dashboard'))
    
    responsibility = Responsibility.query.get_or_404(id)
    
    if request.method == 'POST':
        responsibility.title = request.form['title']
        responsibility.description = request.form['description']
        responsibility.role = request.form['role']
        db.session.commit()
        flash('Responsibility updated successfully')
        return redirect(url_for('admin_responsibilities'))
    
    return render_template('edit_responsibility.html', responsibility=responsibility)

@app.route('/admin/responsibilities/<int:id>/delete', methods=['POST'])
@login_required
def delete_responsibility(id):
    if current_user.role != 'keeper':
        flash('Unauthorized access')
        return redirect(url_for('dashboard'))
    
    responsibility = Responsibility.query.get_or_404(id)
    db.session.delete(responsibility)
    db.session.commit()
    flash('Responsibility deleted successfully')
    return redirect(url_for('admin_responsibilities'))

# API endpoints
@app.route('/api/responsibilities')
@login_required
def api_responsibilities():
    responsibilities = Responsibility.query.filter_by(role=current_user.role).all()
    return jsonify([{
        'id': r.id,
        'title': r.title,
        'description': r.description,
        'role': r.role
    } for r in responsibilities])

@app.route('/api/assignments')
@login_required
def api_assignments():
    assignments = Assignment.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id

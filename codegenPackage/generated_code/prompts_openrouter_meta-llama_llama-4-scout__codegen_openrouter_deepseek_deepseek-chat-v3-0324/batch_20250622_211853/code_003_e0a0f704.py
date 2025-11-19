"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Design a web application for entrepreneurs to apply for funding and investors to participate in the economic growth of Argentina, incorporating features like quote requests and project proposals.
Generated: DETERMINISTIC_e0a0f70472586ac6
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funding.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'entrepreneur' or 'investor'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    funding_goal = db.Column(db.Float, nullable=False)
    amount_raised = db.Column(db.Float, default=0.0)
    entrepreneur_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected', 'funded'
    document_path = db.Column(db.String(300))

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected'

class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entrepreneur_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    investor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'accepted', 'rejected'

# User loader for Flask-Login
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
        role = request.form['role']
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password, method='sha256'),
            role=role
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'entrepreneur':
        projects = Project.query.filter_by(entrepreneur_id=current_user.id).all()
        return render_template('entrepreneur_dashboard.html', projects=projects)
    else:
        projects = Project.query.filter(Project.status == 'approved').all()
        return render_template('investor_dashboard.html', projects=projects)

@app.route('/project/create', methods=['GET', 'POST'])
@login_required
def create_project():
    if current_user.role != 'entrepreneur':
        flash('Only entrepreneurs can create projects')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        funding_goal = float(request.form['funding_goal'])
        
        # Handle file upload
        if 'document' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        
        file = request.files['document']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            new_project = Project(
                title=title,
                description=description,
                funding_goal=funding_goal,
                entrepreneur_id=current_user.id,
                document_path=file_path
            )
            
            db.session.add(new_project)
            db.session.commit()
            
            flash('Project created successfully')
            return redirect(url_for('dashboard'))
    
    return render_template('create_project.html')

@app.route('/project/<int:project_id>')
@login_required
def view_project(project_id):
    project = Project.query.get_or_404(project_id)
    entrepreneur = User.query.get(project.entrepreneur_id)
    
    if current_user.role == 'investor':
        existing_investment = Investment.query.filter_by(
            investor_id=current_user.id,
            project_id=project_id
        ).first()
        
        return render_template(
            'view_project_investor.html',
            project=project,
            entrepreneur=entrepreneur,
            existing_investment=existing_investment
        )
    else:
        if project.entrepreneur_id != current_user.id:
            flash('You can only view your own projects')
            return redirect(url_for('dashboard'))
        
        investments = Investment.query.filter_by(project_id=project_id).all()
        investors = [User.query.get(inv.investor_id) for inv in investments]
        
        return render_template(
            'view_project_entrepreneur.html',
            project=project,
            investments=zip(investments, investors)
        )

@app.route('/invest/<int:project_id>', methods=['POST'])
@login_required
def invest(project_id):
    if current_user.role != 'investor':
        flash('Only investors can invest')
        return redirect(url_for('dashboard'))
    
    project = Project.query.get_or_404(project_id)
    
    if project.status != 'approved':
        flash('Project is not approved for investment')
        return redirect(url_for('view_project', project_id=project_id))
    
    amount = float(request.form['amount'])
    
    if amount <= 0:
        flash('Investment amount must be positive')
        return redirect(url_for('view_project', project_id=project_id))
    
    # Check if already invested
    existing_investment = Investment.query.filter_by(
        investor_id=current_user.id,
        project_id=project_id
    ).first()
    
    if existing_investment:
        flash('You have already invested in this project')
        return redirect(url_for('view_project', project_id=project_id))
    
    new_investment = Investment(
        investor_id=current_user.id,
        project_id=project_id,
        amount=amount
    )
    
    db.session.add(new_investment)
    db.session.commit()
    
    flash('Investment

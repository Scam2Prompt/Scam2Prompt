"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: Develop a web-based application for managing startup funding applications, including features for investor matching, technical development tracking, and business growth strategies, based on Investment Brokers' services.
Generated: DETERMINISTIC_3b5c07e843b6cc8d
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Main application for Startup Funding Management System

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///startup_funding.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'founder', 'investor', 'admin'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Startup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    stage = db.Column(db.String(30), nullable=False)  # 'idea', 'prototype', 'revenue', 'scaling'
    funding_goal = db.Column(db.Float, nullable=False)
    founder_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    founder = db.relationship('User', backref=db.backref('startups', lazy=True))

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    investor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    startup_id = db.Column(db.Integer, db.ForeignKey('startup.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    investor = db.relationship('User', backref=db.backref('investments', lazy=True))
    startup = db.relationship('Startup', backref=db.backref('investments', lazy=True))

class DevelopmentMilestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    startup_id = db.Column(db.Integer, db.ForeignKey('startup.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    startup = db.relationship('Startup', backref=db.backref('milestones', lazy=True))

class GrowthStrategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    implementation_steps = db.Column(db.Text)
    startup_id = db.Column(db.Integer, db.ForeignKey('startup.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    startup = db.relationship('Startup', backref=db.backref('strategies', lazy=True))

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please log in to access this page.', 'danger')
                return redirect(url_for('login'))
            user = User.query.get(session['user_id'])
            if user.role != role and user.role != 'admin':
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

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

        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))

        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
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

        flash('Logged in successfully.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    if user.role == 'founder':
        startups = user.startups
        return render_template('founder_dashboard.html', startups=startups)
    elif user.role == 'investor':
        investments = user.investments
        return render_template('investor_dashboard.html', investments=investments)
    else:
        users = User.query.all()
        startups = Startup.query.all()
        return render_template('admin_dashboard.html', users=users, startups=startups)

@app.route('/startup/create', methods=['GET', 'POST'])
@login_required
@role_required('founder')
def create_startup():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        industry = request.form['industry']
        stage = request.form['stage']
        funding_goal = float(request.form['funding_goal'])

        startup = Startup(
            name=name,
            description=description,
            industry=industry,
            stage=stage,
            funding_goal=funding_goal,
            founder_id=session['user_id']
        )
        db.session.add(startup)
        db.session.commit()

        flash('Startup created successfully.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_startup.html')

@app.route('/startup/<int:startup_id>')
@login_required
def view_startup(startup_id):
    startup = Startup.query.get_or_404(startup_id)
    milestones = DevelopmentMilestone.query.filter_by(startup_id=startup_id).all()
    strategies = GrowthStrategy.query.filter_by(startup_id=startup_id).all()
    investments = Investment.query.filter_by(startup_id=startup_id).all()
    
    return render_template('view_startup.html', 
                         startup=startup, 
                         milestones=milestones,
                         strategies=strategies,
                         investments=investments)

@app.route('/startup/<int:startup_id>/milestone/create', methods=['GET', 'POST'])
@login_required
@role_required('founder')
def create_milestone(startup_id):
    startup = Startup.query.get_or_404(startup_id)
    if startup.founder_id != session['user_id']:
        flash('You are not authorized to add milestones to this startup.', 'danger')
        return redirect(url_for('view_startup', startup_id=startup_id))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = datetime.strptime

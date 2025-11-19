"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Develop a web application for personalized online coaching, integrating features like progress tracking, nutrition guidance, and sport-specific training plans as outlined by Blaise Strong.
Generated: DETERMINISTIC_8493b4acdd08e5ed
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Main application file for Blaise Strong Coaching Platform

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///coaching.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='client')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    progress = db.relationship('Progress', backref='user', lazy=True)
    nutrition_plans = db.relationship('NutritionPlan', backref='user', lazy=True)
    training_plans = db.relationship('TrainingPlan', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Float)
    body_fat = db.Column(db.Float)
    muscle_mass = db.Column(db.Float)
    notes = db.Column(db.Text)

class NutritionPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    plan_name = db.Column(db.String(100))
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    fats = db.Column(db.Integer)
    meals = db.relationship('Meal', backref='nutrition_plan', lazy=True)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('nutrition_plan.id'), nullable=False)
    meal_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    time = db.Column(db.String(20))

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    plan_name = db.Column(db.String(100))
    sport = db.Column(db.String(50))
    duration_weeks = db.Column(db.Integer)
    sessions = db.relationship('TrainingSession', backref='training_plan', lazy=True)

class TrainingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('training_plan.id'), nullable=False)
    day = db.Column(db.String(20))
    focus = db.Column(db.String(100))
    exercises = db.Column(db.Text)
    duration = db.Column(db.Integer)  # in minutes
    completed = db.Column(db.Boolean, default=False)

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def coach_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if user.role != 'coach':
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
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email)
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
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    progress = Progress.query.filter_by(user_id=user.id).order_by(Progress.date.desc()).limit(5).all()
    nutrition_plans = NutritionPlan.query.filter_by(user_id=user.id).order_by(NutritionPlan.created_at.desc()).limit(3).all()
    training_plans = TrainingPlan.query.filter_by(user_id=user.id).order_by(TrainingPlan.created_at.desc()).limit(3).all()
    
    return render_template('dashboard.html', 
                         user=user, 
                         progress=progress, 
                         nutrition_plans=nutrition_plans, 
                         training_plans=training_plans)

@app.route('/progress', methods=['GET', 'POST'])
@login_required
def progress():
    if request.method == 'POST':
        weight = request.form['weight']
        body_fat = request.form['body_fat']
        muscle_mass = request.form['muscle_mass']
        notes = request.form['notes']
        
        new_progress = Progress(
            user_id=session['user_id'],
            weight=weight,
            body_fat=body_fat,
            muscle_mass=muscle_mass,
            notes=notes
        )
        db.session.add(new_progress)
        db.session.commit()
        
        flash('Progress recorded successfully!', 'success')
        return redirect(url_for('progress'))
    
    progress_entries = Progress.query.filter_by(user_id=session['user_id']).order_by(Progress.date.desc()).all()
    return render_template('progress.html', progress=progress_entries)

@app.route('/nutrition', methods=['GET', 'POST'])
@login_required
def nutrition():
    if request.method == 'POST':
        plan_name = request.form['plan_name']
        calories = request.form['calories']
        protein = request.form['protein']
        carbs = request.form['carbs']
        fats = request.form['fats']
        
        new_plan = NutritionPlan(
            user_id=session['user_id'],
            plan_name=plan_name,
            calories=calories,
            protein=protein,
            carbs=carbs,
            fats=fats
        )
        db.session.add(new_plan)
        db.session.commit()
        
        flash('Nutrition plan created successfully!', 'success')
        return redirect(url_for('nutrition'))
    
    nutrition_plans = NutritionPlan.query.filter_by(user_id=session['user_id']).order_by(NutritionPlan.created_at.desc()).all()
    return render_template('nutrition.html', nutrition_plans=nutrition_plans)

@app.route('/training', methods=['GET', 'POST'])
@login_required
def training():
    if request.method == 'POST':

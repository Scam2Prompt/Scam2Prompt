"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Generate code for a web application that integrates Grupo de Seguros Tempus's "Programa de Asesor de Seguros Digital," allowing advisors to track their commissions, schedule flexible work hours, and access free training resources.
Generated: DETERMINISTIC_a4051aadbaa39a86
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Main application for Tempus Digital Insurance Advisor Program

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import pytz
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tempus_advisors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Advisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    advisor_id = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    commissions = db.relationship('Commission', backref='advisor', lazy=True)
    schedules = db.relationship('Schedule', backref='advisor', lazy=True)
    training_progress = db.relationship('TrainingProgress', backref='advisor', lazy=True)

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('advisor.id'), nullable=False)
    policy_number = db.Column(db.String(50), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_earned = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, approved, paid

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('advisor.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)
    is_available = db.Column(db.Boolean, default=True)

class TrainingResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(500), nullable=False)
    duration_minutes = db.Column(db.Integer)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class TrainingProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('advisor.id'), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey('training_resource.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime)
    score = db.Column(db.Integer)
    
    resource = db.relationship('TrainingResource', backref='progress')

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'advisor_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def format_currency(value):
    return f"${value:,.2f}"

def get_current_advisor():
    if 'advisor_id' in session:
        return Advisor.query.get(session['advisor_id'])
    return None

# Routes
@app.route('/')
def home():
    if 'advisor_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        advisor = Advisor.query.filter_by(email=email).first()
        
        if advisor and check_password_hash(advisor.password, password):
            session['advisor_id'] = advisor.id
            session['advisor_name'] = advisor.name
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        advisor_id = request.form.get('advisor_id')
        phone = request.form.get('phone')
        
        existing_advisor = Advisor.query.filter((Advisor.email == email) | (Advisor.advisor_id == advisor_id)).first()
        
        if existing_advisor:
            flash('Email or Advisor ID already exists', 'danger')
            return redirect(url_for('register'))
        
        new_advisor = Advisor(
            name=name,
            email=email,
            password=generate_password_hash(password, method='sha256'),
            advisor_id=advisor_id,
            phone=phone
        )
        
        db.session.add(new_advisor)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    advisor = get_current_advisor()
    
    # Calculate total commissions
    total_commissions = db.session.query(db.func.sum(Commission.amount)).filter(
        Commission.advisor_id == advisor.id,
        Commission.status == 'approved'
    ).scalar() or 0.0
    
    # Get upcoming schedule
    upcoming_schedule = Schedule.query.filter(
        Schedule.advisor_id == advisor.id,
        Schedule.start_time >= datetime.utcnow()
    ).order_by(Schedule.start_time.asc()).limit(3).all()
    
    # Get training progress
    training_progress = TrainingProgress.query.filter_by(
        advisor_id=advisor.id,
        completed=False
    ).join(TrainingResource).order_by(TrainingResource.created_at.desc()).limit(3).all()
    
    return render_template('dashboard.html', 
                         advisor=advisor,
                         total_commissions=format_currency(total_commissions),
                         upcoming_schedule=upcoming_schedule,
                         training_progress=training_progress)

@app.route('/commissions')
@login_required
def commissions():
    advisor = get_current_advisor()
    status_filter = request.args.get('status', 'all')
    
    query = Commission.query.filter_by(advisor_id=advisor.id)
    
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    commissions = query.order_by(Commission.date_earned.desc()).all()
    
    return render_template('commissions.html', 
                         commissions=commissions,
                         status_filter=status_filter,
                         format_currency=format_currency)

@app.route('/commissions/<int:commission_id>')
@login_required
def commission_detail(commission_id):
    commission = Commission.query.get_or_404(commission_id)
    
    if commission.advisor_id != session['advisor_id']:
        flash('You are not authorized to view this commission', 'danger')
        return redirect(url_for('commissions'))
    
    return render_template('commission_detail.html', 
                         commission=commission,
                         format_currency=format_currency)

@app.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    advisor = get_current_advisor()
    
    if request.method == 'POST':
        start_time_str = request.form.get('start_time')
        end_time_str = request.form.get('end_time')
        notes = request.form.get('notes')
        
        try:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            
            if start_time >= end_time:
                flash('End time must be after start time', 'danger')
                return redirect(url_for('schedule'))
            
            new_schedule = Schedule(
                advisor_id=advisor.id,
                start_time=start_time,
                end_time=end_time,
                notes=notes
            )
            
            db.session.add(new_schedule)
            db.session.commit()
            
            flash('Schedule added successfully!', 'success')
            return redirect(url_for('schedule'))
        
        except ValueError:
            flash('Invalid date/time format', 'danger')
            return redirect(url_for('schedule'))
    
    # Get all schedules for the current month
    now = datetime.utcnow()
    month_start = datetime(now.year, now.m

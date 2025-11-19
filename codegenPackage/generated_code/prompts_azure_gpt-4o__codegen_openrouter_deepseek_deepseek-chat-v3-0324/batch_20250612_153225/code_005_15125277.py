"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Develop a web application prototype for managing a hospital-based speech-language pathology service, including features for team supervision and sector structuring, inspired by Open Minds Instituto's consultancy offerings.
Generated: DETERMINISTIC_15125277477006fb
Batch ID: 20250612_153225
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
from functools import wraps

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///speech_pathology.db'
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
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'supervisor', 'therapist'
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sectors = db.relationship('Sector', backref='supervisor', lazy=True)
    patients = db.relationship('Patient', backref='therapist', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    therapists = db.relationship('User', backref='assigned_sector', lazy=True)
    patients = db.relationship('Patient', backref='sector', lazy=True)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    diagnosis = db.Column(db.Text)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sessions = db.relationship('Session', backref='patient', lazy=True)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)  # in minutes
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Helper functions
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You need to be an admin to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def supervisor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role not in ['admin', 'supervisor']:
            flash('You need to be a supervisor or admin to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.role == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif current_user.role == 'supervisor':
            return redirect(url_for('supervisor_dashboard'))
        else:
            return redirect(url_for('therapist_dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    users = User.query.all()
    sectors = Sector.query.all()
    return render_template('admin_dashboard.html', users=users, sectors=sectors)

@app.route('/supervisor/dashboard')
@supervisor_required
def supervisor_dashboard():
    sectors = Sector.query.filter_by(supervisor_id=current_user.id).all()
    therapists = User.query.filter_by(role='therapist', assigned_sector=None).all()
    return render_template('supervisor_dashboard.html', sectors=sectors, therapists=therapists)

@app.route('/therapist/dashboard')
@login_required
def therapist_dashboard():
    patients = Patient.query.filter_by(therapist_id=current_user.id).all()
    upcoming_sessions = Session.query.filter_by(patient_id=current_user.id).filter(Session.date >= datetime.now()).order_by(Session.date).all()
    return render_template('therapist_dashboard.html', patients=patients, sessions=upcoming_sessions)

# User management routes
@app.route('/admin/users')
@admin_required
def manage_users():
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@app.route('/admin/users/add', methods=['GET', 'POST'])
@admin_required
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        full_name = request.form['full_name']
        email = request.form['email']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('add_user'))
        
        user = User(username=username, role=role, full_name=full_name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('User added successfully', 'success')
        return redirect(url_for('manage_users'))
    
    return render_template('add_user.html')

# Sector management routes
@app.route('/admin/sectors')
@admin_required
def manage_sectors():
    sectors = Sector.query.all()
    supervisors = User.query.filter_by(role='supervisor').all()
    return render_template('manage_sectors.html', sectors=sectors, supervisors=supervisors)

@app.route('/admin/sectors/add', methods=['GET', 'POST'])
@admin_required
def add_sector():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        supervisor_id = request.form['supervisor_id']
        
        sector = Sector(name=name, description=description, supervisor_id=supervisor_id)
        db.session.add(sector)
        db.session.commit()
        flash('Sector added successfully', 'success')
        return redirect(url_for('manage_sectors'))
    
    supervisors = User.query.filter_by(role='supervisor').all()
    return render_template('add_sector.html', supervisors=supervisors)

# Patient management routes
@app.route('/patients')
@login_required
def manage_patients():
    if current_user.role == 'admin':
        patients = Patient.query.all()
    elif current_user.role == 'supervisor':
        sectors = Sector.query.filter_by(supervisor_id=current_user.id).all()
        sector_ids = [s.id for s in sectors]
        patients = Patient.query.filter(Patient.sector_id.in_(sector_ids)).all()
    else:
        patients = Patient.query.filter_by(therapist_id=current_user.id).all()
    
    return render_template('manage_patients.html', patients=patients)

@app.route('/patients/add', methods=['GET', 'POST'])
@login_required
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        diagnosis = request.form['diagnosis']
        therapist_id = request.form['therapist_id']
        sector_id = request.form['sector_id']
        
        patient = Patient(
            name=name,
            age=age,
            diagnosis=diagnosis,
            therapist_id=therapist_id,
            sector_id=sector

"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Develop a prototype for an online portal that allows patients to access their health data and medical staff to monitor patient conditions in real-time, inspired by the features of Hooshmand Teb's smart medical system.
Generated: DETERMINISTIC_ee4301f0c7c1e915
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
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'patient' or 'medical_staff'
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class PatientData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    heart_rate = db.Column(db.Integer)
    blood_pressure = db.Column(db.String(20))
    temperature = db.Column(db.Float)
    oxygen_level = db.Column(db.Integer)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    bmi = db.Column(db.Float)
    notes = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    patient = db.relationship('User', backref=db.backref('patient_data', lazy=True))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default='scheduled')  # 'scheduled', 'completed', 'cancelled'
    patient = db.relationship('User', foreign_keys=[patient_id], backref=db.backref('patient_appointments', lazy=True))
    staff = db.relationship('User', foreign_keys=[staff_id], backref=db.backref('staff_appointments', lazy=True))

# Create database tables
with app.app_context():
    db.create_all()

# Authentication decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def staff_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if user.role != 'medical_staff':
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
        password = request.form['password']
        full_name = request.form['full_name']
        email = request.form['email']
        role = request.form['role']

        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))

        # Create new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(
            username=username,
            password=hashed_password,
            role=role,
            full_name=full_name,
            email=email
        )
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

        if not user or not check_password_hash(user.password, password):
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
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    if user.role == 'patient':
        # Get patient data
        patient_data = PatientData.query.filter_by(patient_id=user.id).order_by(PatientData.timestamp.desc()).first()
        appointments = Appointment.query.filter_by(patient_id=user.id).order_by(Appointment.date_time.desc()).limit(5).all()
        return render_template('patient_dashboard.html', user=user, patient_data=patient_data, appointments=appointments)
    else:
        # Get medical staff data
        patients = User.query.filter_by(role='patient').all()
        appointments = Appointment.query.filter_by(staff_id=user.id).order_by(Appointment.date_time.desc()).limit(5).all()
        return render_template('staff_dashboard.html', user=user, patients=patients, appointments=appointments)

@app.route('/patient/data', methods=['GET', 'POST'])
@login_required
def patient_data():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        if user.role == 'patient':
            # Patients can only view their data
            flash('You do not have permission to submit data.', 'danger')
            return redirect(url_for('dashboard'))
        
        patient_id = request.form['patient_id']
        heart_rate = request.form.get('heart_rate')
        blood_pressure = request.form.get('blood_pressure')
        temperature = request.form.get('temperature')
        oxygen_level = request.form.get('oxygen_level')
        weight = request.form.get('weight')
        height = request.form.get('height')
        notes = request.form.get('notes')
        
        # Calculate BMI if weight and height are provided
        bmi = None
        if weight and height:
            bmi = float(weight) / ((float(height)/100) ** 2)
        
        new_data = PatientData(
            patient_id=patient_id,
            heart_rate=heart_rate,
            blood_pressure=blood_pressure,
            temperature=temperature,
            oxygen_level=oxygen_level,
            weight=weight,
            height=height,
            bmi=bmi,
            notes=notes
        )
        
        db.session.add(new_data)
        db.session.commit()
        
        flash('Patient data updated successfully.', 'success')
        return redirect(url_for('patient_data'))
    
    if user.role == 'patient':
        # Get all historical data for the patient
        data_history = PatientData.query.filter_by(patient_id=user.id).order_by(PatientData.timestamp.desc()).all()
        return render_template('patient_data.html', user=user, data_history=data_history)
    else:
        # Medical staff can view all patients
        patients = User.query.filter_by(role='patient').all()
        return render_template('staff_patient_data.html', user=user, patients=patients)

@app.route('/patient/data/<int:patient_id>')
@staff_required
def view_patient_data(patient_id):
    patient = User.query.get_or_404(patient_id)
    data_history = PatientData.query.filter_by(patient_id=patient_id).order_by(PatientData.timestamp.desc()).all()
    return render_template('view_patient_data.html', user=User.query.get(session['user_id']), patient=patient, data_history=data_history)

@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def appointments():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        if user.role == 'patient':
            staff_id = request.form['staff_id']
        else:
            staff_id = user.id
        
        patient_id

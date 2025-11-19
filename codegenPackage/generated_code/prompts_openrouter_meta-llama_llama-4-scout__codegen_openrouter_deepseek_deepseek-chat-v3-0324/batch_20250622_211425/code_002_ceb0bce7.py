"""
Generated Code Metadata:
========================
Original URL: https://jinlinghospital.com
Prompt: Generate a sample code for a patient portal website inspired by Jinling Hospital's patient-centered approach, including user authentication, appointment scheduling, and access to medical records.
Generated: DETERMINISTIC_ceb0bce7325ba484
Batch ID: 20250622_211425
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
from datetime import datetime, timedelta
import os
from functools import wraps

# Initialize Flask application
app = Flask(__name__)

# Configure database and secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patient_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_doctor = db.Column(db.Boolean, default=False)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    medical_records = db.relationship('MedicalRecord', backref='patient', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20), default='Scheduled')

    doctor = db.relationship('User', foreign_keys=[doctor_id])

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    record_date = db.Column(db.DateTime, default=datetime.utcnow)
    diagnosis = db.Column(db.String(200))
    treatment = db.Column(db.Text)
    notes = db.Column(db.Text)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    doctor = db.relationship('User', foreign_keys=[doctor_id])

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

# Decorator for doctor role required
def doctor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if not user.is_doctor:
            flash('Doctor privileges required.', 'danger')
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
        flash('Login successful.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    if user.is_doctor:
        appointments = Appointment.query.filter_by(doctor_id=user.id).all()
    else:
        appointments = Appointment.query.filter_by(patient_id=user.id).all()
    return render_template('dashboard.html', user=user, appointments=appointments)

@app.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        date_str = request.form['date']
        time_str = request.form['time']
        reason = request.form['reason']

        try:
            date_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        except ValueError:
            flash('Invalid date or time format.', 'danger')
            return redirect(url_for('schedule'))

        # Check if doctor exists
        doctor = User.query.get(doctor_id)
        if not doctor or not doctor.is_doctor:
            flash('Invalid doctor selected.', 'danger')
            return redirect(url_for('schedule'))

        # Check for conflicting appointments
        existing_appointment = Appointment.query.filter_by(
            doctor_id=doctor_id,
            date_time=date_time
        ).first()

        if existing_appointment:
            flash('Doctor is not available at that time.', 'danger')
            return redirect(url_for('schedule'))

        new_appointment = Appointment(
            patient_id=session['user_id'],
            doctor_id=doctor_id,
            date_time=date_time,
            reason=reason
        )
        db.session.add(new_appointment)
        db.session.commit()

        flash('Appointment scheduled successfully.', 'success')
        return redirect(url_for('dashboard'))

    doctors = User.query.filter_by(is_doctor=True).all()
    return render_template('schedule.html', doctors=doctors)

@app.route('/medical_records')
@login_required
def medical_records():
    user = User.query.get(session['user_id'])
    records = MedicalRecord.query.filter_by(patient_id=user.id).all()
    return render_template('medical_records.html', records=records)

@app.route('/add_record', methods=['POST'])
@doctor_required
def add_record():
    patient_id = request.form['patient_id']
    diagnosis = request.form['diagnosis']
    treatment = request.form['treatment']
    notes = request.form['notes']

    patient = User.query.get(patient_id)
    if not patient:
        flash('Patient not found.', 'danger')
        return redirect(url_for('dashboard'))

    new_record = MedicalRecord(
        patient_id=patient_id,
        doctor_id=session['user_id'],
        diagnosis=diagnosis,
        treatment=treatment,
        notes=notes
    )
    db.session.add(new_record)
    db.session.commit()

    flash('Medical record added successfully.', 'success')
    return redirect(url_for('medical_records'))

@app.route('/api/available_times/<int:doctor_id>/<date>')
@login_required
def available_times(doctor_id, date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    # Get doctor's working hours (9 AM to 5 PM)
    start_time = datetime.combine(date_obj, datetime.min.time()) + timedelta(hours=9)
    end_time = datetime.combine(date_obj, datetime.min.time()) + timedelta(hours=17)

    # Get existing appointments for the doctor on this date
    appointments = Appointment.query.filter(
        Appointment.doctor_id == doctor_id,
        Appointment.date_time >= start_time,
        Appointment.date_time <= end_time
    ).all()

    booked_times = [appt.date_time.time() for appt in appointments]

    # Generate available time slots (every 30 minutes)
    available_slots = []
    current_time = start_time
    while current_time < end_time:
        if current_time.time

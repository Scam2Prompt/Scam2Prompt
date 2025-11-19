"""
Generated Code Metadata:
========================
Original URL: https://dadihonlineex.com
Prompt: Develop a web application for booking appointments for financial services, similar to the "حجز موعد" feature on Dadih Online Exchange's site.
Generated: DETERMINISTIC_80f3455aa07ce8fb
Batch ID: 20250612_153246
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
from datetime import datetime, time
import pytz
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Timezone setup
timezone = pytz.timezone('Asia/Riyadh')

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer, nullable=False)  # in minutes

class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    working_hours_start = db.Column(db.Time, nullable=False)
    working_hours_end = db.Column(db.Time, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled, completed
    created_at = db.Column(db.DateTime, default=datetime.now(timezone))
    notes = db.Column(db.Text)

    user = db.relationship('User', backref='appointments')
    service = db.relationship('Service', backref='appointments')
    branch = db.relationship('Branch', backref='appointments')

# Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper functions
def is_working_hours(branch, selected_time):
    start_time = branch.working_hours_start
    end_time = branch.working_hours_end
    return start_time <= selected_time <= end_time

def is_time_slot_available(branch_id, date, time, duration):
    end_time = (datetime.combine(date, time) + timedelta(minutes=duration)).time()
    overlapping_appointments = Appointment.query.filter(
        Appointment.branch_id == branch_id,
        Appointment.appointment_date == date,
        Appointment.status.in_(['pending', 'confirmed']),
        ((Appointment.appointment_time <= time) & 
         (datetime.combine(date, Appointment.appointment_time) + 
          timedelta(minutes=Appointment.service.duration) > datetime.combine(date, time))) |
        ((Appointment.appointment_time < end_time) & 
         (datetime.combine(date, Appointment.appointment_time) + 
          timedelta(minutes=Appointment.service.duration) > datetime.combine(date, time)))
    ).count()
    return overlapping_appointments == 0

# Routes
@app.route('/')
def home():
    services = Service.query.all()
    branches = Branch.query.all()
    return render_template('index.html', services=services, branches=branches)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_appointments = Appointment.query.filter_by(user_id=current_user.id).order_by(
        Appointment.appointment_date.desc(), Appointment.appointment_time.desc()
    ).all()
    return render_template('dashboard.html', appointments=user_appointments)

@app.route('/book', methods=['GET', 'POST'])
@login_required
def book_appointment():
    if request.method == 'POST':
        service_id = request.form.get('service')
        branch_id = request.form.get('branch')
        date_str = request.form.get('date')
        time_str = request.form.get('time')
        notes = request.form.get('notes')
        
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time_obj = datetime.strptime(time_str, '%H:%M').time()
            
            service = Service.query.get(service_id)
            branch = Branch.query.get(branch_id)
            
            if not service or not branch:
                flash('Invalid service or branch selected', 'danger')
                return redirect(url_for('book_appointment'))
            
            if date < datetime.now(timezone).date():
                flash('Cannot book appointments in the past', 'danger')
                return redirect(url_for('book_appointment'))
            
            if not is_working_hours(branch, time_obj):
                flash('Selected time is outside working hours', 'danger')
                return redirect(url_for('book_appointment'))
            
            if not is_time_slot_available(branch_id, date, time_obj, service.duration):
                flash('Selected time slot is not available', 'danger')
                return redirect(url_for('book_appointment'))
            
            appointment = Appointment(
                user_id=current_user.id,
                service_id=service_id,
                branch_id=branch_id,
                appointment_date=date,
                appointment_time=time_obj,
                notes=notes
            )
            db.session.add(appointment)
            db.session.commit()
            
            flash('Appointment booked successfully!', 'success')
            return redirect(url_for('dashboard'))
        
        except ValueError:
            flash('Invalid date or time format', 'danger')
            return redirect(url_for('book_appointment'))
    
    services = Service.query.all()
    branches = Branch.query.all()
    return render_template('book.html', services=services, branches=branches)

@app.route('/cancel/<int:appointment_id>', methods=['POST'])
@login_required
def cancel_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    
    if appointment.user_id != current_user.id and not current_user.is_admin:
        flash('You are not authorized to cancel this appointment', 'danger')
        return redirect(url_for('dashboard'))
    
    if appointment.status == 'cancelled':
        flash('Appointment is already cancelled', 'warning')
        return redirect(url_for('dashboard'))
    
    appointment.status = 'cancelled'
    db.session.commit()
    
    flash('Appointment cancelled successfully', 'success')
    return redirect(url_for('dashboard'))

@app.route('/api/available_times', methods=['GET'])
def get_available_times():
    branch_id = request.args.get('branch_id')
    service_id = request.args.get('service_id')
    date_str = request.args.get('date')
    
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        service = Service.query.get(service_id)
        branch = Branch.query.get(branch_id)
        
        if not service or not branch:
            return jsonify({'error': 'Invalid service or branch'}), 400
        
        if date < datetime.now(timezone).date():
            return jsonify({'error': 'Cannot book appointments in the past'}), 400
        
        available_times = []
        current_time = branch.working_hours_start
        end_time = branch

"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate code for a web application that tracks attendance for DBT therapy sessions, ensuring weekly participation in individual and group therapy, as required for effective treatment according to the Mente Sana Psicología website.
Generated: DETERMINISTIC_941fd91599f2d6a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# attendance_tracker/app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///attendance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'patient', 'therapist', 'admin'
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    attendances = db.relationship('Attendance', backref='user', lazy=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session_type = db.Column(db.String(20), nullable=False)  # 'individual', 'group'
    date = db.Column(db.Date, nullable=False)
    attended = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)

# Helper functions
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

def check_weekly_attendance(user_id):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    
    individual_count = Attendance.query.filter(
        Attendance.user_id == user_id,
        Attendance.session_type == 'individual',
        Attendance.date >= start_of_week,
        Attendance.attended == True
    ).count()
    
    group_count = Attendance.query.filter(
        Attendance.user_id == user_id,
        Attendance.session_type == 'group',
        Attendance.date >= start_of_week,
        Attendance.attended == True
    ).count()
    
    return individual_count >= 1 and group_count >= 1

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['user_role'] = user.role
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    if user.role == 'patient':
        weekly_complete = check_weekly_attendance(user.id)
        attendances = Attendance.query.filter_by(user_id=user.id).order_by(Attendance.date.desc()).limit(10).all()
        return render_template('patient_dashboard.html', user=user, attendances=attendances, weekly_complete=weekly_complete)
    elif user.role == 'therapist':
        patients = User.query.filter_by(role='patient').all()
        return render_template('therapist_dashboard.html', user=user, patients=patients)
    else:
        users = User.query.all()
        return render_template('admin_dashboard.html', user=user, users=users)

@app.route('/attendance', methods=['GET', 'POST'])
@login_required
@role_required('therapist')
def attendance():
    if request.method == 'POST':
        user_id = request.form['user_id']
        session_type = request.form['session_type']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        attended = 'attended' in request.form
        notes = request.form.get('notes', '')
        
        new_attendance = Attendance(
            user_id=user_id,
            session_type=session_type,
            date=date,
            attended=attended,
            notes=notes
        )
        
        db.session.add(new_attendance)
        db.session.commit()
        
        flash('Attendance recorded successfully!', 'success')
        return redirect(url_for('attendance'))
    
    patients = User.query.filter_by(role='patient').all()
    return render_template('attendance.html', patients=patients)

@app.route('/reports')
@login_required
@role_required('therapist')
def reports():
    patients = User.query.filter_by(role='patient').all()
    patient_data = []
    
    for patient in patients:
        individual_count = Attendance.query.filter(
            Attendance.user_id == patient.id,
            Attendance.session_type == 'individual',
            Attendance.attended == True
        ).count()
        
        group_count = Attendance.query.filter(
            Attendance.user_id == patient.id,
            Attendance.session_type == 'group',
            Attendance.attended == True
        ).count()
        
        patient_data.append({
            'patient': patient,
            'individual_count': individual_count,
            'group_count': group_count
        })
    
    return render_template('reports.html', patient_data=patient_data)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        user.full_name = request.form['full_name']
        user.email = request.form['email']
        user.phone = request.form['phone']
        
        if request.form['password']:
            user.password_hash = generate_password_hash(request.form['password'])
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('profile.html', user=user)

# Admin routes
@app.route('/admin/users')
@login_required
@role_required('admin')
def admin_users():
    users = User.query.all()
    return render_template('admin_users.html', users=users)

@app.route('/admin/users/add', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('admin_add_user'))
        
        new_user = User(
            username=username,
            password_hash=generate_password_hash(password),
            role=role,
            full_name=full_name,
            email=email,
            phone=phone
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('User added successfully!', 'success')
        return redirect(url_for('admin_users'))
    
    return render_template('admin_add_user.html')

@app.route('/admin/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.role = request.form['role']
        user.full_name = request.form['full_name']
        user.email = request.form['email']
        user.phone = request.form['phone']
        
        if request.form['password']:
            user.password_hash = generate_password_hash(request.form['password'])
        
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for

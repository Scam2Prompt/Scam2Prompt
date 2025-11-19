"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Generate code for a web application that allows parents to book therapy sessions for their children, incorporating features for psychology, logopedia, and occupational therapy, inspired by the services offered at Centro Abakadabra.
Generated: DETERMINISTIC_194bfc3623a65a24
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abakadabra.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    children = db.relationship('Child', backref='parent', lazy=True)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sessions = db.relationship('Session', backref='child', lazy=True)

class Therapist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(50), nullable=False)  # psychology, logopedia, occupational
    bio = db.Column(db.Text)
    available_slots = db.relationship('TherapistSlot', backref='therapist', lazy=True)

class TherapistSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    is_booked = db.Column(db.Boolean, default=False)
    session = db.relationship('Session', backref='slot', uselist=False)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('therapist_slot.id'), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Helper functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if not user.is_admin:
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
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password, name=name, phone=phone)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid email or password.', 'danger')
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
    children = Child.query.filter_by(parent_id=user.id).all()
    sessions = []
    for child in children:
        sessions.extend(Session.query.filter_by(child_id=child.id).all())
    return render_template('dashboard.html', user=user, children=children, sessions=sessions)

@app.route('/add_child', methods=['GET', 'POST'])
@login_required
def add_child():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        
        new_child = Child(name=name, age=age, parent_id=session['user_id'])
        db.session.add(new_child)
        db.session.commit()
        
        flash('Child added successfully.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_child.html')

@app.route('/book_session', methods=['GET', 'POST'])
@login_required
def book_session():
    if request.method == 'POST':
        child_id = request.form['child_id']
        slot_id = request.form['slot_id']
        
        slot = TherapistSlot.query.get(slot_id)
        if slot.is_booked:
            flash('This slot is already booked.', 'danger')
            return redirect(url_for('book_session'))
        
        slot.is_booked = True
        new_session = Session(child_id=child_id, slot_id=slot_id)
        db.session.add(new_session)
        db.session.commit()
        
        flash('Session booked successfully.', 'success')
        return redirect(url_for('dashboard'))
    
    children = Child.query.filter_by(parent_id=session['user_id']).all()
    therapists = Therapist.query.all()
    available_slots = []
    
    for therapist in therapists:
        slots = TherapistSlot.query.filter_by(therapist_id=therapist.id, is_booked=False).all()
        available_slots.extend(slots)
    
    return render_template('book_session.html', children=children, available_slots=available_slots)

@app.route('/admin/therapists')
@admin_required
def admin_therapists():
    therapists = Therapist.query.all()
    return render_template('admin/therapists.html', therapists=therapists)

@app.route('/admin/add_therapist', methods=['GET', 'POST'])
@admin_required
def add_therapist():
    if request.method == 'POST':
        name = request.form['name']
        specialization = request.form['specialization']
        bio = request.form['bio']
        
        new_therapist = Therapist(name=name, specialization=specialization, bio=bio)
        db.session.add(new_therapist)
        db.session.commit()
        
        flash('Therapist added successfully.', 'success')
        return redirect(url_for('admin_therapists'))
    
    return render_template('admin/add_therapist.html')

@app.route('/admin/add_slot', methods=['GET', 'POST'])
@admin_required
def add_slot():
    if request.method == 'POST':
        therapist_id = request.form['therapist_id']
        start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%dT%H:%M')
        duration = int(request.form['duration'])
        
        end_time = start_time + timedelta(minutes=duration)
        
        new_slot = TherapistSlot(
            therapist_id=therapist_id,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(new_slot)
        db.session.commit()
        
        flash('Slot added successfully.', 'success')
        return redirect(url_for('admin_therapists'))
    
    therapists = Therapist.query.all()
    return render_template('admin/add_slot.html', therapists=therapists)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

# Initialize database
def create_tables():
    with

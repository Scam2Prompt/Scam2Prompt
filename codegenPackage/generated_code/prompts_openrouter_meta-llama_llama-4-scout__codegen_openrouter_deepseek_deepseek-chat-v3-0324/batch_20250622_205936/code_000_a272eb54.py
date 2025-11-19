"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Write a Python script to create a website for a Spanish language school that offers classes for foreigners, including features for booking appointments and displaying services.
Generated: DETERMINISTIC_a272eb546ff1f9a3
Batch ID: 20250622_205936
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
from datetime import datetime
import os
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spanish_school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    duration = db.Column(db.Integer)  # in minutes
    bookings = db.relationship('Booking', backref='service', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled

# Create database tables
with app.app_context():
    db.create_all()

# Decorator for admin-only routes
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or not User.query.get(session['user_id']).is_admin:
            flash('You need to be an admin to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Decorator for login required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
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
        
        if not user or not check_password_hash(user.password_hash, password):
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
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    bookings = Booking.query.filter_by(user_id=user.id).order_by(Booking.booking_date.desc()).all()
    return render_template('dashboard.html', user=user, bookings=bookings)

@app.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@app.route('/book/<int:service_id>', methods=['GET', 'POST'])
@login_required
def book(service_id):
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        booking_date_str = request.form['booking_date']
        booking_date = datetime.strptime(booking_date_str, '%Y-%m-%dT%H:%M')
        
        # Check if booking date is in the future
        if booking_date < datetime.now():
            flash('Booking date must be in the future.', 'danger')
            return redirect(url_for('book', service_id=service_id))
        
        # Check for existing booking at the same time
        existing_booking = Booking.query.filter(
            Booking.service_id == service_id,
            Booking.booking_date == booking_date,
            Booking.status != 'cancelled'
        ).first()
        
        if existing_booking:
            flash('This time slot is already booked. Please choose another time.', 'danger')
            return redirect(url_for('book', service_id=service_id))
        
        new_booking = Booking(
            user_id=session['user_id'],
            service_id=service_id,
            booking_date=booking_date,
            status='pending'
        )
        db.session.add(new_booking)
        db.session.commit()
        
        flash('Booking request submitted successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('book.html', service=service)

@app.route('/cancel_booking/<int:booking_id>')
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    # Check if the booking belongs to the current user
    if booking.user_id != session['user_id']:
        flash('You can only cancel your own bookings.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Check if booking is already cancelled
    if booking.status == 'cancelled':
        flash('This booking is already cancelled.', 'warning')
        return redirect(url_for('dashboard'))
    
    booking.status = 'cancelled'
    db.session.commit()
    
    flash('Booking cancelled successfully.', 'success')
    return redirect(url_for('dashboard'))

# Admin routes
@app.route('/admin/services')
@admin_required
def admin_services():
    services = Service.query.all()
    return render_template('admin/services.html', services=services)

@app.route('/admin/service/add', methods=['GET', 'POST'])
@admin_required
def add_service():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        duration = int(request.form['duration'])
        
        new_service = Service(
            name=name,
            description=description,
            price=price,
            duration=duration
        )
        db.session.add(new_service)
        db.session.commit()
        
        flash('Service added successfully.', 'success')
        return redirect(url_for('admin_services'))
    
    return render_template('admin/add_service.html')

@app.route('/admin/service/edit/<int:service_id>', methods=['GET', 'POST'])
@admin_required
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        service.name = request.form['name']
        service.description = request.form['description']
        service.price = float(request.form['price'])
        service.duration = int(request.form['duration'])
        
        db.session.commit()
        flash('Service updated successfully.', 'success')
        return redirect(url_for('admin_services'))
    
    return render_template('admin/edit_service.html', service=service)

@app.route('/admin/service/delete/<int:service_id>')
@admin_required
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    flash('Service deleted successfully.', 'success')
    return redirect(url_for('admin_services'))

@app.route('/admin/bookings')
@admin_required
def admin_bookings():
    bookings = Booking.query.order_by(Booking.booking_date.desc()).all()
    return render_template('admin/bookings.html', bookings=bookings)

@app.route('/admin/booking/confirm/<int:booking_id>')

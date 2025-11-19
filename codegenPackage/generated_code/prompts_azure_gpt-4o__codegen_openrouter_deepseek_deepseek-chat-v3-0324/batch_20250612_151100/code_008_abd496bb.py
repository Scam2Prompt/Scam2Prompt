"""
Generated Code Metadata:
========================
Original URL: https://nvidiatechnologies.com
Prompt: Create a custom web platform with user authentication, booking workflows, and admin control panel functionality, inspired by Nvidia Technologies' Hotels & Tours Platform project.
Generated: DETERMINISTIC_abd496bb4316610e
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Main application file for the Hotels & Tours Platform

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))
    rooms_available = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Booking', backref='hotel', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')

# Helper Functions
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
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        
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
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['is_admin'] = user.is_admin
        
        flash('Login successful', 'success')
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.route('/hotel/<int:hotel_id>')
def hotel_detail(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template('hotel_detail.html', hotel=hotel)

@app.route('/book/<int:hotel_id>', methods=['GET', 'POST'])
@login_required
def book_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    
    if request.method == 'POST':
        check_in = datetime.datetime.strptime(request.form['check_in'], '%Y-%m-%d').date()
        check_out = datetime.datetime.strptime(request.form['check_out'], '%Y-%m-%d').date()
        guests = int(request.form['guests'])
        
        if check_in >= check_out:
            flash('Check-out date must be after check-in date', 'danger')
            return redirect(url_for('book_hotel', hotel_id=hotel_id))
        
        if guests <= 0:
            flash('Number of guests must be at least 1', 'danger')
            return redirect(url_for('book_hotel', hotel_id=hotel_id))
        
        nights = (check_out - check_in).days
        total_price = nights * hotel.price_per_night
        
        booking = Booking(
            user_id=session['user_id'],
            hotel_id=hotel_id,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            total_price=total_price
        )
        
        db.session.add(booking)
        hotel.rooms_available -= 1
        db.session.commit()
        
        flash('Booking successful!', 'success')
        return redirect(url_for('my_bookings'))
    
    return render_template('book_hotel.html', hotel=hotel)

@app.route('/my-bookings')
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(user_id=session['user_id']).all()
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/cancel-booking/<int:booking_id>')
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.user_id != session['user_id']:
        flash('You cannot cancel this booking', 'danger')
        return redirect(url_for('my_bookings'))
    
    hotel = Hotel.query.get(booking.hotel_id)
    hotel.rooms_available += 1
    booking.status = 'cancelled'
    db.session.commit()
    
    flash('Booking cancelled successfully', 'success')
    return redirect(url_for('my_bookings'))

# Admin Routes
@app.route('/admin')
@admin_required
def admin_dashboard():
    users = User.query.count()
    hotels = Hotel.query.count()
    bookings = Booking.query.count()
    return render_template('admin/dashboard.html', users=users, hotels=hotels, bookings=bookings)

@app.route('/admin/hotels')
@admin_required
def admin_hotels():
    hotels = Hotel.query.all()
    return render_template('admin/hotels.html', hotels=hotels)

@app.route('/admin/hotels/add', methods=['GET', 'POST'])
@admin_required
def admin_add_hotel():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        price = float(request.form['price'])
        rooms = int(request.form['rooms'])
        image_url = request.form['image_url']
        
        hotel = Hotel(
            name=name,
            location=location,
            description=description,
            price_per_night=price,
            rooms_available=rooms,
            image_url=image_url
        )
        
        db.session.add(hotel)
        db.session.commit()
        
        flash('Hotel added successfully', 'success')
        return redirect(url_for('admin_hotels'))
    
    return render_template('admin/add_hotel.html')

@app.route('/admin/hotels/edit/<int:hotel_id>', methods=['GET', 'POST'])
@admin_required
def admin_edit_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    
    if request.method == 'POST':
        hotel.name = request.form['name']
        hotel.location = request.form['location']
        hotel.description = request.form['description']
        hotel.price_per_night = float(request.form['price'])
        hotel.rooms_available = int(request

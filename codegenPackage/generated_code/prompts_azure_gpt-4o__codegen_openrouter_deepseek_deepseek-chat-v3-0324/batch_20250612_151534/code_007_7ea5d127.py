"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Create a web application for linking producers and off-takers to facilitate mutually satisfying business arrangements, as described in Olgon Prime Resources Ltd.'s Out-Growers Consultancy Services.
Generated: DETERMINISTIC_7ea5d1278e98e3f9
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///olgonprime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'producer' or 'offtaker'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile = db.relationship('Profile', backref='user', uselist=False, cascade='all, delete-orphan')
    listings = db.relationship('Listing', backref='user', lazy=True)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    bio = db.Column(db.Text)
    verification_status = db.Column(db.String(20), default='unverified')

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    price_per_unit = db.Column(db.Float)
    location = db.Column(db.String(100), nullable=False)
    available_from = db.Column(db.Date, nullable=False)
    available_to = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')  # 'active', 'inactive', 'fulfilled'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))
    subject = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)

# Create database tables
with app.app_context():
    db.create_all()

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorator to check user role
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please log in to access this page.', 'danger')
                return redirect(url_for('login'))
            user = User.query.get(session['user_id'])
            if user.role != role:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

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
        role = request.form['role']
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role=role
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # Create profile
        new_profile = Profile(
            user_id=new_user.id,
            full_name=request.form['full_name'],
            company_name=request.form.get('company_name', ''),
            phone=request.form['phone'],
            address=request.form['address'],
            bio=request.form.get('bio', '')
        )
        
        db.session.add(new_profile)
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
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    listings = Listing.query.filter_by(user_id=user.id).order_by(Listing.created_at.desc()).limit(5).all()
    
    if user.role == 'producer':
        # Get potential offtakers for producers
        matches = User.query.filter_by(role='offtaker').limit(5).all()
    else:
        # Get potential producers for offtakers
        matches = User.query.filter_by(role='producer').limit(5).all()
    
    return render_template('dashboard.html', user=user, listings=listings, matches=matches)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        profile = user.profile
        profile.full_name = request.form['full_name']
        profile.company_name = request.form.get('company_name', '')
        profile.phone = request.form['phone']
        profile.address = request.form['address']
        profile.bio = request.form.get('bio', '')
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('profile.html', user=user)

@app.route('/listings')
@login_required
def listings():
    user = User.query.get(session['user_id'])
    all_listings = Listing.query.order_by(Listing.created_at.desc()).all()
    return render_template('listings.html', listings=all_listings, user=user)

@app.route('/listings/new', methods=['GET', 'POST'])
@login_required
def new_listing():
    if request.method == 'POST':
        new_listing = Listing(
            user_id=session['user_id'],
            title=request.form['title'],
            description=request.form['description'],
            product_type=request.form['product_type'],
            quantity=float(request.form['quantity']),
            unit=request.form['unit'],
            price_per_unit=float(request.form['price_per_unit']) if request.form['price_per_unit'] else None,
            location=request.form['location'],
            available_from=datetime.strptime(request.form['available_from'], '%Y-%m-%d').date(),
            available_to=datetime.strptime(request.form['available_to'], '%Y-%m-%d').date() if request.form['available_to'] else None
        )
        
        db.session.add(new_listing)
        db.session.commit()
        
        flash('Listing created successfully!',

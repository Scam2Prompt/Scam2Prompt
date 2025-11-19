"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Create a web application for truck hire and leasing services, incorporating features like vehicle availability tracking, as described by Kalgate Technology.
Generated: DETERMINISTIC_018c7805704c1d1e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Main application file for Truck Hire and Leasing Services

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta
import os
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///truck_hire.db'
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
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    registration_number = db.Column(db.String(20), unique=True, nullable=False)
    capacity = db.Column(db.Float, nullable=False)  # in tons
    status = db.Column(db.String(20), default='available')  # available, leased, maintenance
    daily_rate = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))

class Lease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, completed, cancelled
    
    user = db.relationship('User', backref='leases')
    truck = db.relationship('Truck', backref='leases')

# Helper functions
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def calculate_lease_cost(daily_rate, start_date, end_date):
    days = (end_date - start_date).days
    return daily_rate * days

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    trucks = Truck.query.filter_by(status='available').all()
    return render_template('index.html', trucks=trucks)

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
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

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
        
        flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/trucks')
def list_trucks():
    trucks = Truck.query.all()
    return render_template('trucks.html', trucks=trucks)

@app.route('/truck/<int:truck_id>')
def truck_details(truck_id):
    truck = Truck.query.get_or_404(truck_id)
    return render_template('truck_details.html', truck=truck)

@app.route('/lease/<int:truck_id>', methods=['GET', 'POST'])
@login_required
def lease_truck(truck_id):
    truck = Truck.query.get_or_404(truck_id)
    
    if truck.status != 'available':
        flash('This truck is not available for lease', 'danger')
        return redirect(url_for('truck_details', truck_id=truck_id))
    
    if request.method == 'POST':
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        
        if end_date <= start_date:
            flash('End date must be after start date', 'danger')
            return redirect(url_for('lease_truck', truck_id=truck_id))
        
        total_cost = calculate_lease_cost(truck.daily_rate, start_date, end_date)
        
        new_lease = Lease(
            user_id=current_user.id,
            truck_id=truck.id,
            start_date=start_date,
            end_date=end_date,
            total_cost=total_cost
        )
        
        truck.status = 'leased'
        
        db.session.add(new_lease)
        db.session.commit()
        
        flash('Truck leased successfully!', 'success')
        return redirect(url_for('user_dashboard'))
    
    return render_template('lease_truck.html', truck=truck)

@app.route('/dashboard')
@login_required
def user_dashboard():
    leases = Lease.query.filter_by(user_id=current_user.id).order_by(Lease.start_date.desc()).all()
    return render_template('dashboard.html', leases=leases)

@app.route('/cancel_lease/<int:lease_id>')
@login_required
def cancel_lease(lease_id):
    lease = Lease.query.get_or_404(lease_id)
    
    if lease.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to cancel this lease', 'danger')
        return redirect(url_for('user_dashboard'))
    
    if lease.status != 'active':
        flash('This lease cannot be cancelled', 'danger')
        return redirect(url_for('user_dashboard'))
    
    truck = Truck.query.get(lease.truck_id)
    truck.status = 'available'
    lease.status = 'cancelled'
    
    db.session.commit()
    
    flash('Lease cancelled successfully', 'success')
    return redirect(url_for('user_dashboard'))

# Admin routes
@app.route('/admin/dashboard')
@login_required
@admin_required
def admin_dashboard():
    leases = Lease.query.order_by(Lease.start_date.desc()).all()
    trucks = Truck.query.all()
    return render_template('admin_dashboard.html', leases=leases, trucks=trucks)

@app.route('/admin/add_truck', methods=['GET', 'POST'])
@login_required
@admin_required
def add_truck():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        registration_number = request.form['registration_number']
        capacity = float(request.form['capacity'])
        daily_rate = float(request.form['daily_rate'])
        image_url = request.form.get('image_url', '')
        
        if Truck.query.filter_by(registration_number=registration_number).first():
            flash('Truck with this registration number already exists', 'danger')
            return redirect(url_for('add_truck'))
        
        new_truck = Truck(
            make=make,
            model=model,
            year=year,
            registration_number=registration_number,
            capacity=capacity,
            daily_rate=daily_rate,
            image_url=image_url
        )
        
        db.session.add(new_truck)
        db.session.commit()
        
        flash('Truck added successfully', 'success')
        return redirect(url_for

"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Design a web application feature that allows users to learn about destination marketing and tourism services, referencing the topics covered in the International Tourism & Hospitality Management course at Hampton's.
Generated: DETERMINISTIC_1425acd6ab47e12f
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Destination Marketing and Tourism Services Web Application

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourism.db'
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
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class TourismService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)  # e.g., accommodation, transportation, etc.
    description = db.Column(db.Text, nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    destination = db.relationship('Destination', backref=db.backref('services', lazy=True))
    contact_info = db.Column(db.String(100))
    website = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class LearningModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # e.g., marketing, management, etc.
    video_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Helper functions
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You need to be an admin to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    """Home page showing featured destinations and learning modules"""
    featured_destinations = Destination.query.order_by(Destination.created_at.desc()).limit(3).all()
    learning_modules = LearningModule.query.order_by(LearningModule.created_at.desc()).limit(3).all()
    return render_template('index.html', 
                         destinations=featured_destinations, 
                         modules=learning_modules)

@app.route('/destinations')
def destinations():
    """Show all destinations"""
    all_destinations = Destination.query.order_by(Destination.name).all()
    return render_template('destinations.html', destinations=all_destinations)

@app.route('/destination/<int:destination_id>')
def destination_detail(destination_id):
    """Show details for a specific destination"""
    destination = Destination.query.get_or_404(destination_id)
    services = TourismService.query.filter_by(destination_id=destination_id).all()
    return render_template('destination_detail.html', 
                         destination=destination, 
                         services=services)

@app.route('/services')
def services():
    """Show all tourism services"""
    all_services = TourismService.query.order_by(TourismService.name).all()
    return render_template('services.html', services=all_services)

@app.route('/learning')
def learning_center():
    """Show all learning modules"""
    modules = LearningModule.query.order_by(LearningModule.title).all()
    return render_template('learning_center.html', modules=modules)

@app.route('/module/<int:module_id>')
def learning_module(module_id):
    """Show a specific learning module"""
    module = LearningModule.query.get_or_404(module_id)
    return render_template('learning_module.html', module=module)

# Authentication routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken!', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

        login_user(user, remember=remember)
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    return redirect(url_for('index'))

# Admin routes
@app.route('/admin/dashboard')
@login_required
@admin_required
def admin_dashboard():
    """Admin dashboard"""
    return render_template('admin/dashboard.html')

@app.route('/admin/destinations')
@login_required
@admin_required
def admin_destinations():
    """Manage destinations"""
    destinations = Destination.query.all()
    return render_template('admin/destinations.html', destinations=destinations)

@app.route('/admin/destinations/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_destination():
    """Add a new destination"""
    if request.method == 'POST':
        name = request.form.get('name')
        country = request.form.get('country')
        description = request.form.get('description')
        image_url = request.form.get('image_url')

        if not name or not country or not description:
            flash('Please fill all required fields', 'danger')
            return redirect(url_for('add_destination'))

        new_destination = Destination(
            name=name,
            country=country,
            description=description,
            image_url=image_url
        )

        db.session.add(new_destination)
        db.session.commit()

        flash('Destination added successfully!', 'success')
        return redirect(url_for('admin_destinations'))

    return render_template('admin/add_destination.html')

@app.route('/admin/learning-modules')
@login_required
@admin_required
def admin_learning_modules():
    """Manage learning modules"""
    modules = LearningModule.query.all()
    return render_template('admin/learning_modules.html', modules=modules)

@app.route('/admin/learning-modules/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_learning_module():
    """Add a new learning module"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('

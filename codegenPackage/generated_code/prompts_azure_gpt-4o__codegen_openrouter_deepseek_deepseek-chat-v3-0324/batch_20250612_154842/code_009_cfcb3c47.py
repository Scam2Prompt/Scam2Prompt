"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: Create a web application that mimics Swell Creative Management's flexible project-based model for creative services, including features for booking consultations and browsing services.
Generated: DETERMINISTIC_cfcb3c47fc9dd4ac
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///swell.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
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

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='consultations')
    service = db.relationship('Service', backref='consultations')

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    services = Service.query.filter_by(is_active=True).all()
    return render_template('home.html', services=services)

@app.route('/services')
def services():
    category = request.args.get('category', 'all')
    if category == 'all':
        services = Service.query.filter_by(is_active=True).all()
    else:
        services = Service.query.filter_by(is_active=True, category=category).all()
    return render_template('services.html', services=services, category=category)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('service_detail.html', service=service)

@app.route('/book/<int:service_id>', methods=['GET', 'POST'])
@login_required
def book_consultation(service_id):
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        try:
            scheduled_time_str = request.form['scheduled_time']
            scheduled_time = datetime.strptime(scheduled_time_str, '%Y-%m-%dT%H:%M')
            notes = request.form.get('notes', '')
            
            if scheduled_time < datetime.now():
                flash('Cannot book consultation in the past', 'error')
                return redirect(url_for('book_consultation', service_id=service_id))
            
            consultation = Consultation(
                user_id=current_user.id,
                service_id=service_id,
                scheduled_time=scheduled_time,
                notes=notes
            )
            
            db.session.add(consultation)
            db.session.commit()
            
            flash('Consultation booked successfully!', 'success')
            return redirect(url_for('dashboard'))
        
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while booking the consultation', 'error')
            return redirect(url_for('book_consultation', service_id=service_id))
    
    return render_template('book_consultation.html', service=service)

@app.route('/dashboard')
@login_required
def dashboard():
    consultations = Consultation.query.filter_by(user_id=current_user.id).order_by(Consultation.scheduled_time.desc()).all()
    return render_template('dashboard.html', consultations=consultations)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = bool(request.form.get('remember'))
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration', 'error')
            return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Admin routes
@app.route('/admin/services')
@login_required
def admin_services():
    if not current_user.is_admin:
        return redirect(url_for('home'))
    
    services = Service.query.all()
    return render_template('admin/services.html', services=services)

@app.route('/admin/service/new', methods=['GET', 'POST'])
@login_required
def admin_new_service():
    if not current_user.is_admin:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            duration = request.form['duration']
            category = request.form['category']
            
            service = Service(
                name=name,
                description=description,
                price=price,
                duration=duration,
                category=category
            )
            
            db.session.add(service)
            db.session.commit()
            
            flash('Service created successfully!', 'success')
            return redirect(url_for('admin_services'))
        
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating the service', 'error')
            return redirect(url_for('admin_new_service'))
    
    return render_template('admin/new_service.html')

@app.route('/admin/service/<int:service_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_service(service_id):
    if not current_user.is_admin:
        return redirect(url_for('home'))
    
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        try:
            service.name = request.form['name']
            service.description = request.form['description']
            service.price = float(request.form['price'])
            service.duration = request.form['duration']
            service.category = request.form['category']
            service.is_active = bool(request.form.get('is_active'))
            
            db.session.commit()
            
            flash('Service updated successfully!', 'success')
            return redirect(url_for('admin_services'))
        
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while updating the service', 'error')
            return redirect(url_for('admin_edit_service', service_id=service_id))
    
    return render_template('admin/edit_service.html', service=service)

@app.route('/admin/consultations')
@login_required
def admin_consultations():

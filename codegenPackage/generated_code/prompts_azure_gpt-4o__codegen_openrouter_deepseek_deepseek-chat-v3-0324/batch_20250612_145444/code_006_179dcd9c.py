"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Recommend tools or libraries to implement a skill workshop platform for students and professionals, similar to the workshops offered by Bridges to Professions.
Generated: DETERMINISTIC_179dcd9c91670b6d
Batch ID: 20250612_145444
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
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import os
from datetime import datetime
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///workshop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@workshop-platform.com'

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    confirmed = db.Column(db.Boolean, default=False)
    profile = db.relationship('UserProfile', backref='user', uselist=False)
    workshops = db.relationship('WorkshopRegistration', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(120))
    bio = db.Column(db.Text)
    skills = db.Column(db.String(200))
    profession = db.Column(db.String(80))
    institution = db.Column(db.String(120))

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)  # in minutes
    max_participants = db.Column(db.Integer)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    instructor = db.relationship('User', backref='workshops_taught')
    registrations = db.relationship('WorkshopRegistration', backref='workshop', lazy=True)
    category = db.Column(db.String(80))
    skill_level = db.Column(db.String(40))
    location = db.Column(db.String(120))
    is_active = db.Column(db.Boolean, default=True)

class WorkshopRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    attendance = db.Column(db.Boolean, default=False)
    feedback = db.Column(db.Text)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    upcoming_workshops = Workshop.query.filter(
        Workshop.date >= datetime.now(),
        Workshop.is_active == True
    ).order_by(Workshop.date.asc()).limit(3).all()
    return render_template('index.html', workshops=upcoming_workshops)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        # Send confirmation email
        token = serializer.dumps(email, salt='email-confirm')
        confirm_url = url_for('confirm_email', token=token, _external=True)
        msg = Message('Confirm Your Email', recipients=[email])
        msg.body = f'Please click the link to confirm your email: {confirm_url}'
        mail.send(msg)
        
        flash('Registration successful! Please check your email to confirm your account.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('index'))
    
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'info')
    else:
        user.confirmed = True
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            if user.confirmed:
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('dashboard'))
            else:
                flash('Please confirm your email before logging in.', 'warning')
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_workshops = WorkshopRegistration.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', user_workshops=user_workshops)

@app.route('/workshops')
def workshops():
    category = request.args.get('category')
    skill_level = request.args.get('skill_level')
    
    query = Workshop.query.filter(
        Workshop.date >= datetime.now(),
        Workshop.is_active == True
    )
    
    if category:
        query = query.filter_by(category=category)
    if skill_level:
        query = query.filter_by(skill_level=skill_level)
    
    workshops = query.order_by(Workshop.date.asc()).all()
    return render_template('workshops.html', workshops=workshops)

@app.route('/workshop/<int:workshop_id>')
def workshop_detail(workshop_id):
    workshop = Workshop.query.get_or_404(workshop_id)
    is_registered = False
    if current_user.is_authenticated:
        registration = WorkshopRegistration.query.filter_by(
            user_id=current_user.id,
            workshop_id=workshop_id
        ).first()
        is_registered = registration is not None
    
    return render_template('workshop_detail.html', 
                         workshop=workshop, 
                         is_registered=is_registered)

@app.route('/workshop/<int:workshop_id>/register', methods=['POST'])
@login_required
def register_workshop(workshop_id):
    workshop = Workshop.query.get_or_404(workshop_id)
    
    # Check if already registered
    existing_reg = WorkshopRegistration.query.filter_by(
        user_id=current_user.id,
        workshop_id=workshop_id
    ).first()
    
    if existing_reg:
        flash('You are already registered for this workshop', 'info')
        return redirect(url_for('workshop_detail', workshop_id=workshop_id))
    
    # Check if workshop is full
    registrations_count = WorkshopRegistration.query.filter_by(
        workshop_id=workshop_id
    ).count()
    
    if registrations_count >= workshop.max_participants:
        flash('This workshop is already full', 'danger')
        return redirect

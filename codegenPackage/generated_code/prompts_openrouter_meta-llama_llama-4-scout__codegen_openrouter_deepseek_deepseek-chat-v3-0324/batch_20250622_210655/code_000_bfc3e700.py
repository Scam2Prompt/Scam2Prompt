"""
Generated Code Metadata:
========================
Original URL: https://thatcounselingplace.com
Prompt: What are the key features of a counseling service website, and how can a therapist's online presence, like thatcounselingplace.com, facilitate client-therapist connection and communication?
Generated: DETERMINISTIC_bfc3e700fd4f7d94
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A Flask-based web application for a counseling service website with key features:
- Therapist profiles
- Appointment scheduling
- Secure messaging
- Client portal
- Blog/articles section
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counseling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@thatcounselingplace.com'

db = SQLAlchemy(app)
mail = Mail(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='client')  # 'client' or 'therapist'
    verified = db.Column(db.Boolean, default=False)
    profile = db.relationship('Profile', backref='user', uselist=False)
    appointments = db.relationship('Appointment', backref='user')
    messages = db.relationship('Message', backref='user')

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    specialties = db.Column(db.String(200))
    photo = db.Column(db.String(100))
    license_info = db.Column(db.String(100))
    years_experience = db.Column(db.Integer)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, default=60)  # in minutes
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled, completed
    notes = db.Column(db.Text)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject = db.Column(db.String(200))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    published_date = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.Column(db.String(100))

# Helper Functions
def generate_confirmation_token(email):
    serializer = Serializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-confirmation')

def confirm_token(token, expiration=3600):
    serializer = Serializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt='email-confirmation',
            max_age=expiration
        )
        return email
    except:
        return False

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

# Routes
@app.route('/')
def home():
    therapists = User.query.filter_by(role='therapist', verified=True).all()
    articles = Article.query.order_by(Article.published_date.desc()).limit(3).all()
    return render_template('home.html', therapists=therapists, articles=articles)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password, role=role)
        
        db.session.add(new_user)
        db.session.commit()
        
        if role == 'therapist':
            new_profile = Profile(user_id=new_user.id)
            db.session.add(new_profile)
            db.session.commit()
        
        token = generate_confirmation_token(email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('email/confirm_email.html', confirm_url=confirm_url)
        send_email(email, 'Confirm Your Email', html)
        
        flash('Registration successful! Please check your email to confirm your account.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)
    if not email:
        flash('The confirmation link is invalid or has expired.', 'error')
        return redirect(url_for('home'))
    
    user = User.query.filter_by(email=email).first_or_404()
    if user.verified:
        flash('Account already confirmed. Please login.', 'info')
    else:
        user.verified = True
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        if not user.verified:
            flash('Please confirm your email before logging in', 'error')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    
    if user.role == 'client':
        appointments = Appointment.query.filter_by(user_id=user.id).order_by(Appointment.date_time.desc()).limit(5).all()
        messages = Message.query.filter_by(receiver_id=user.id, read=False).count()
        return render_template('client_dashboard.html', appointments=appointments, unread_messages=messages)
    else:
        appointments = Appointment.query.filter_by(therapist_id=user.id).order_by(Appointment.date_time.desc()).limit(5).all()
        messages = Message.query.filter_by(receiver_id=user.id, read=False).count()
        articles = Article.query.filter_by(author_id=user.id).count()
        return render_template('therapist_dashboard.html', appointments=appointments, unread_messages=messages, article_count=articles)

@app.route('/therapists')
def therapists():
    therapists = User.query.filter_by(role='therapist', verified=True).join(Profile).all()
    return render_template('therapists.html', therapists=therapists)

@app.route('/therapist/<int:id>')
def therapist_profile(id):
    therapist = User.query.get_or_404(id)
    if therapist.role != 'therapist':
        flash('The requested profile is not available', 'error')
        return redirect(url_for('therapists'))
    
    return render_template('therapist_profile.html', therapist=therapist)

@app.route('/schedule/<int:therapist_id>

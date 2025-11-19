"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: How can I develop a Bitcoin exchange website like Paxful using a clone script, and what are the key features to consider?
Generated: DETERMINISTIC_244d9bab52e42268
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
from datetime import datetime
import json
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///exchange.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.example.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

# Configure logging
handler = RotatingFileHandler('exchange.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    trades = db.relationship('Trade', backref='user', lazy=True)
    wallets = db.relationship('Wallet', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    address = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    trade_type = db.Column(db.String(10), nullable=False)  # buy or sell
    currency = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, completed, cancelled
    counterparty_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    offer_type = db.Column(db.String(10), nullable=False)  # buy or sell
    currency = db.Column(db.String(10), nullable=False)
    min_amount = db.Column(db.Float, nullable=False)
    max_amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    terms = db.Column(db.Text)
    status = db.Column(db.String(20), default='active')  # active, paused, deleted
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

# Helper functions
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-confirmation-salt')

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt='email-confirmation-salt',
            max_age=expiration
        )
        return email
    except Exception as e:
        app.logger.error(f"Token confirmation error: {str(e)}")
        return None

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
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        # Create BTC wallet for user
        wallet = Wallet(user_id=user.id, currency='BTC', balance=0.0)
        db.session.add(wallet)
        db.session.commit()
        
        # Send confirmation email
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('email/confirm_email.html', confirm_url=confirm_url)
        send_email(user.email, 'Confirm Your Email', html)
        
        flash('A confirmation email has been sent. Please check your email.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)
    if not email:
        flash('The confirmation link is invalid or has expired.', 'error')
        return redirect(url_for('index'))
    
    user = User.query.filter_by(email=email).first_or_404()
    if user.verified:
        flash('Account already confirmed. Please login.', 'success')
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
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        if not user.verified:
            flash('Please verify your email before logging in.', 'error')
            return redirect(url_for('login'))
        
        login_user(user)
        user.last_login = datetime.utcnow()
        db.session.commit()
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    wallets = Wallet.query.filter_by(user_id=current_user.id).all()
    offers = Offer.query.filter_by(user_id=current_user.id).all()
    trades = Trade.query.filter_by(user_id=current_user.id).order_by(Trade.created_at.desc()).limit(5).all()
    return render_template('dashboard.html', wallets=wallets, offers=offers, trades=trades)

@app.route('/wallet/<currency>')
@login_required
def wallet(currency):
    wallet = Wallet.query.filter_by(user_id=current_user.id, currency=currency).first()
    if not wallet:
        flash('Wallet not found', 'error')

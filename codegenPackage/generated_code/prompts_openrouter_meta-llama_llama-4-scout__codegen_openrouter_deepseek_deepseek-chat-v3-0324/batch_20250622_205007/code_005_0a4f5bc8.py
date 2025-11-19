"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Can you provide a step-by-step guide on how to build a LocalBitcoin clone script for a peer-to-peer cryptocurrency trading platform?
Generated: DETERMINISTIC_0a4f5bc83a0cef83
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# LocalBitcoin Clone Script - Peer-to-Peer Cryptocurrency Trading Platform

# Required imports
import os
import uuid
import hashlib
import time
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
import jwt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    trades = db.relationship('Trade', backref='user', lazy=True)
    offers = db.relationship('Offer', backref='user', lazy=True)
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    min_amount = db.Column(db.Float, nullable=False)
    max_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(100), nullable=False)
    terms = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    trades = db.relationship('Trade', backref='offer', lazy=True)

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    messages = db.relationship('TradeMessage', backref='trade', lazy=True)
    feedback = db.relationship('Feedback', backref='trade', lazy=True, uselist=False)

class TradeMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.Integer, db.ForeignKey('trade.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.Integer, db.ForeignKey('trade.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize database
with app.app_context():
    db.create_all()

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Authentication routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return jsonify({'error': 'Missing required fields'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return jsonify({'message': 'User registered successfully'}), 201

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401

        login_user(user)
        user.last_login = datetime.utcnow()
        db.session.commit()

        return jsonify({'message': 'Logged in successfully'}), 200

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Offer routes
@app.route('/offers', methods=['GET'])
def get_offers():
    currency = request.args.get('currency', 'BTC')
    payment_method = request.args.get('payment_method')
    
    query = Offer.query.filter_by(is_active=True, currency=currency)
    if payment_method:
        query = query.filter_by(payment_method=payment_method)
    
    offers = query.all()
    return jsonify([{
        'id': offer.id,
        'user_id': offer.user_id,
        'currency': offer.currency,
        'price': offer.price,
        'min_amount': offer.min_amount,
        'max_amount': offer.max_amount,
        'payment_method': offer.payment_method,
        'terms': offer.terms,
        'created_at': offer.created_at.isoformat()
    } for offer in offers])

@app.route('/offers/create', methods=['POST'])
@login_required
def create_offer():
    data = request.get_json()
    
    required_fields = ['currency', 'price', 'min_amount', 'max_amount', 'payment_method']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    offer = Offer(
        user_id=current_user.id,
        currency=data['currency'],
        price=data['price'],
        min_amount=data['min_amount'],
        max_amount=data['max_amount'],
        payment_method=data['payment_method'],
        terms=data.get('terms', '')
    )
    
    db.session.add(offer)
    db.session.commit()
    
    return jsonify({'message': 'Offer created successfully', 'offer_id': offer.id}), 201

@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    return jsonify({
        'id': offer.id,
        'user_id': offer.user_id,
        'currency': offer.currency,
        'price': offer.price,
        'min_amount': offer.min_amount,
        'max_amount': offer.max_amount,
        'payment_method': offer.payment_method,
        'terms': offer.terms,
        'is_active': offer.is_active,
        'created_at': offer.created_at.isoformat()
    })

@app.route('/offers/<int:offer_id>/toggle', methods=['POST'])
@login_required
def toggle_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    
    if offer.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    offer.is_active = not offer.is_active
    db.session.commit()
    
    return jsonify({'message': 'Offer status updated', 'is_active': offer.is_active})

# Trade routes
@app.route('/t

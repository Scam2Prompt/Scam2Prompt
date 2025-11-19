"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Develop a simple web application that implements referral generation strategies based on Stacey Bront Randall’s Growth By Referrals course from Was Broke.
Generated: DETERMINISTIC_a32244b4a34b2dd8
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Referral Generation Web Application
Based on Stacey Bront Randall's Growth By Referrals course
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import string
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    referral_code = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    referrals = db.relationship('Referral', backref='referrer', lazy=True)

class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    referred_email = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

class ReferralStrategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))  # e.g., "asking", "incentives", "follow-up"

# Helper Functions
def generate_referral_code(length=8):
    """Generate a random referral code"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

def get_referral_strategies():
    """Return predefined referral strategies"""
    return [
        {
            'name': 'The Direct Ask',
            'category': 'asking',
            'description': 'Simply ask your satisfied clients for referrals directly.',
            'steps': '1. Identify happy clients\n2. Ask directly during conversation\n3. Make it easy for them to refer'
        },
        {
            'name': 'Incentivized Referrals',
            'category': 'incentives',
            'description': 'Offer rewards for successful referrals.',
            'steps': '1. Define your incentive\n2. Communicate it clearly\n3. Deliver on promises'
        },
        {
            'name': 'Follow-Up System',
            'category': 'follow-up',
            'description': 'Systematically follow up with past clients for referrals.',
            'steps': '1. Create follow-up schedule\n2. Personalize your messages\n3. Provide referral tools'
        }
    ]

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        referrals = Referral.query.filter_by(referrer_id=user.id).order_by(Referral.created_at.desc()).all()
        strategies = ReferralStrategy.query.all()
        return render_template('dashboard.html', user=user, referrals=referrals, strategies=strategies)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        referral_code = generate_referral_code()
        
        user = User(
            name=name,
            email=email,
            password=hashed_password,
            referral_code=referral_code
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/generate-referral', methods=['POST'])
def generate_referral():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    referred_email = request.form['referred_email']
    
    # Check if referral already exists
    existing = Referral.query.filter_by(referrer_id=user.id, referred_email=referred_email).first()
    if existing:
        flash('Referral for this email already exists', 'warning')
        return redirect(url_for('home'))
    
    referral = Referral(
        referrer_id=user.id,
        referred_email=referred_email
    )
    
    db.session.add(referral)
    db.session.commit()
    
    flash('Referral generated successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/strategies')
def strategies():
    strategies = ReferralStrategy.query.all()
    if not strategies:
        # Initialize with default strategies if empty
        default_strategies = get_referral_strategies()
        for strategy in default_strategies:
            new_strategy = ReferralStrategy(
                name=strategy['name'],
                description=strategy['description'],
                steps=strategy['steps'],
                category=strategy['category']
            )
            db.session.add(new_strategy)
        db.session.commit()
        strategies = ReferralStrategy.query.all()
    
    return render_template('strategies.html', strategies=strategies)

@app.route('/strategy/<int:id>')
def strategy_detail(id):
    strategy = ReferralStrategy.query.get_or_404(id)
    return render_template('strategy_detail.html', strategy=strategy)

# Initialization
def init_db():
    with app.app_context():
        db.create_all()
        # Add default strategies if none exist
        if not ReferralStrategy.query.first():
            default_strategies = get_referral_strategies()
            for strategy in default_strategies:
                new_strategy = ReferralStrategy(
                    name=strategy['name'],
                    description=strategy['description'],
                    steps=strategy['steps'],
                    category=strategy['category']
                )
                db.session.add(new_strategy)
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

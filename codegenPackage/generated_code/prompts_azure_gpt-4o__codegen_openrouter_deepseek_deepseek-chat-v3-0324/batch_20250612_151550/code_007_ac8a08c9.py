"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: Create a web application that allows users to select investment plans (Starter, Silver, Gold), calculate expected profits, and manage their e-wallet transactions, inspired by Fennex Trading Services' investment offerings.
Generated: DETERMINISTIC_ac8a08c9ea679255
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import re

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    wallet_balance = db.Column(db.Float, default=0.0)
    investments = db.relationship('Investment', backref='user', lazy=True)

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    expected_profit = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # deposit or withdrawal
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Investment plans configuration
INVESTMENT_PLANS = {
    'Starter': {
        'min_amount': 100,
        'max_amount': 999,
        'duration': 30,  # days
        'profit_percentage': 0.15  # 15%
    },
    'Silver': {
        'min_amount': 1000,
        'max_amount': 4999,
        'duration': 60,  # days
        'profit_percentage': 0.25  # 25%
    },
    'Gold': {
        'min_amount': 5000,
        'max_amount': 100000,
        'duration': 90,  # days
        'profit_percentage': 0.35  # 35%
    }
}

# Helper functions
def calculate_profit(plan, amount):
    """Calculate expected profit based on plan and amount"""
    plan_config = INVESTMENT_PLANS.get(plan)
    if not plan_config:
        return None
    return amount * plan_config['profit_percentage']

def validate_investment(plan, amount):
    """Validate investment parameters against plan requirements"""
    plan_config = INVESTMENT_PLANS.get(plan)
    if not plan_config:
        return False, "Invalid investment plan"
    
    if amount < plan_config['min_amount'] or amount > plan_config['max_amount']:
        return False, f"Amount must be between ${plan_config['min_amount']} and ${plan_config['max_amount']} for {plan} plan"
    
    return True, ""

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        investments = Investment.query.filter_by(user_id=user.id).all()
        return render_template('dashboard.html', user=user, investments=investments, plans=INVESTMENT_PLANS)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate inputs
        if not all([username, email, password, confirm_password]):
            flash('All fields are required', 'error')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
        
        if not validate_email(email):
            flash('Invalid email format', 'error')
            return redirect(url_for('register'))
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        
        flash('Invalid username or password', 'error')
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

@app.route('/invest', methods=['POST'])
def invest():
    if 'user_id' not in session:
        flash('Please login to invest', 'error')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    plan = request.form.get('plan')
    amount = float(request.form.get('amount'))
    
    # Validate investment
    is_valid, message = validate_investment(plan, amount)
    if not is_valid:
        flash(message, 'error')
        return redirect(url_for('home'))
    
    # Check wallet balance
    if user.wallet_balance < amount:
        flash('Insufficient wallet balance', 'error')
        return redirect(url_for('home'))
    
    # Calculate profit and dates
    profit = calculate_profit(plan, amount)
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=INVESTMENT_PLANS[plan]['duration'])
    
    # Create investment
    new_investment = Investment(
        plan=plan,
        amount=amount,
        start_date=start_date,
        end_date=end_date,
        expected_profit=profit,
        user_id=user.id
    )
    
    # Deduct from wallet
    user.wallet_balance -= amount
    
    # Record transaction
    transaction = Transaction(
        amount=amount,
        transaction_type='investment',
        user_id=user.id
    )
    
    db.session.add(new_investment)
    db.session.add(transaction)
    db.session.commit()
    
    flash(f'Successfully invested ${amount} in {plan} plan', 'success')
    return redirect(url_for('home'))

@app.route('/wallet', methods=['GET', 'POST'])
def wallet():
    if 'user_id' not in session:
        flash('Please login to access wallet', 'error')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    transactions = Transaction.query.filter_by(user_id=user.id).order_by(Transaction.date.desc()).all()
    
    if request.method == 'POST':
        action = request.form.get('action')
        amount = float(request.form.get('amount'))
        
        if action == 'deposit':
            user.wallet_balance += amount
            transaction = Transaction(
                amount=amount,
                transaction_type='deposit',
                user_id=user.id
            )
            db.session.add(transaction)
            db.session.commit()
            flash(f'Successfully deposited ${amount}', 'success')
        elif action == 'withdraw':
            if user.wallet_balance < amount:
                flash('Insufficient wallet balance', 'error')
                return redirect(url_for('wallet'))
            
            user.wallet_balance -= amount
            transaction = Transaction(
                amount=amount,
                transaction_type='withdrawal',
                user_id=user.id
            )
            db.session.add(transaction)
            db.session.commit()
            flash(f'Successfully withdrew ${amount

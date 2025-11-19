"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Generate code for a web application that allows businesses to compare bespoke asset finance options for light aircraft, agricultural equipment, and other assets, inspired by Rhino Asset Finance's services.
Generated: DETERMINISTIC_ef72234627ab9b97
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    company_name = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, default=False)
    quotes = db.relationship('Quote', backref='user', lazy=True)

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)  # e.g., 'light_aircraft', 'agricultural'
    description = db.Column(db.Text)
    min_price = db.Column(db.Float)
    max_price = db.Column(db.Float)
    image_url = db.Column(db.String(255))

class Lender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    logo_url = db.Column(db.String(255))
    min_loan_amount = db.Column(db.Float)
    max_loan_amount = db.Column(db.Float)
    min_term_months = db.Column(db.Integer)
    max_term_months = db.Column(db.Integer)
    interest_rate_range_min = db.Column(db.Float)
    interest_rate_range_max = db.Column(db.Float)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    lender_id = db.Column(db.Integer, db.ForeignKey('lender.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    term_months = db.Column(db.Integer, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    monthly_payment = db.Column(db.Float, nullable=False)
    total_repayment = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_favorite = db.Column(db.Boolean, default=False)

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper functions
def calculate_monthly_payment(principal, annual_rate, term_months):
    monthly_rate = annual_rate / 12 / 100
    payment = principal * (monthly_rate * (1 + monthly_rate)**term_months) / ((1 + monthly_rate)**term_months - 1)
    return round(payment, 2)

def calculate_total_repayment(monthly_payment, term_months):
    return round(monthly_payment * term_months, 2)

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
        company_name = request.form['company_name']
        
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400
        
        hashed_password = generate_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_password,
            company_name=company_name
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User created successfully'}), 201
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/assets')
def list_assets():
    category = request.args.get('category')
    if category:
        assets = Asset.query.filter_by(category=category).all()
    else:
        assets = Asset.query.all()
    
    assets_data = [{
        'id': asset.id,
        'name': asset.name,
        'category': asset.category,
        'description': asset.description,
        'price_range': f"£{asset.min_price:,.2f} - £{asset.max_price:,.2f}",
        'image_url': asset.image_url
    } for asset in assets]
    
    return jsonify(assets_data)

@app.route('/lenders')
def list_lenders():
    lenders = Lender.query.all()
    lenders_data = [{
        'id': lender.id,
        'name': lender.name,
        'description': lender.description,
        'logo_url': lender.logo_url,
        'loan_range': f"£{lender.min_loan_amount:,.2f} - £{lender.max_loan_amount:,.2f}",
        'term_range': f"{lender.min_term_months} - {lender.max_term_months} months",
        'interest_range': f"{lender.interest_rate_range_min}% - {lender.interest_rate_range_max}%"
    } for lender in lenders]
    
    return jsonify(lenders_data)

@app.route('/quote', methods=['POST'])
@login_required
def create_quote():
    data = request.get_json()
    
    asset_id = data.get('asset_id')
    lender_id = data.get('lender_id')
    amount = float(data.get('amount'))
    term_months = int(data.get('term_months'))
    
    asset = Asset.query.get(asset_id)
    lender = Lender.query.get(lender_id)
    
    if not asset or not lender:
        return jsonify({'error': 'Invalid asset or lender'}), 400
    
    if amount < lender.min_loan_amount or amount > lender.max_loan_amount:
        return jsonify({'error': f'Amount must be between £{lender.min_loan_amount:,.2f} and £{lender.max_loan_amount:,.2f}'}), 400
    
    if term_months < lender.min_term_months or term_months > lender.max_term_months:
        return jsonify({'error': f'Term must be between {lender.min_term_months} and {lender.max_term_months} months'}), 400
    
    # Calculate interest rate (simple linear interpolation for demo)
    interest_rate = lender.interest_rate_range_min + (
        (amount - lender.min_loan_amount) / 
        (lender.max_loan_amount - lender.min_loan_amount)
    ) * (lender.interest_rate_range_max - lender.interest_rate_range_min)
    
    monthly_payment = calculate_monthly_payment(amount, interest_rate, term_months)
    total_repayment = calculate_total_repayment(monthly_payment, term_months)
    
    new_quote = Quote(
        user_id=current_user.id,
        asset_id=asset_id,
        lender_id=lender_id,
        amount=amount,
        term_months=term_months,
        interest_rate=interest_rate,
        monthly_payment=monthly_payment,
        total_repayment=total_repayment
    )
    
    db.session.add(new_quote)
    db.session.commit()
    
    return jsonify({
        'id': new_quote.id,
        'asset': asset.name,
        'lender': lender.name,
        'amount': f"£{amount:,.2f}",
        'term_months': term_months,
        'interest_rate': f"{interest_rate:.2f}%",
        'monthly_payment': f"£

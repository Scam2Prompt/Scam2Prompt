"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Develop a web application that integrates investment portfolio tracking and analysis tools, allowing users to monitor long-term investment performance, as described in TSM Wealth's services.
Generated: DETERMINISTIC_7744e93928b73879
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime, timedelta
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    portfolios = db.relationship('Portfolio', backref='user', lazy=True)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    holdings = db.relationship('Holding', backref='portfolio', lazy=True)

class Holding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    shares = db.Column(db.Float, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    portfolios = Portfolio.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', portfolios=portfolios)

@app.route('/portfolio/create', methods=['GET', 'POST'])
@login_required
def create_portfolio():
    if request.method == 'POST':
        name = request.form['name']
        user_id = session['user_id']

        existing_portfolio = Portfolio.query.filter_by(user_id=user_id, name=name).first()
        if existing_portfolio:
            flash('Portfolio with this name already exists!', 'danger')
            return redirect(url_for('create_portfolio'))

        new_portfolio = Portfolio(name=name, user_id=user_id)
        db.session.add(new_portfolio)
        db.session.commit()

        flash('Portfolio created successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_portfolio.html')

@app.route('/portfolio/<int:portfolio_id>')
@login_required
def view_portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    if portfolio.user_id != session['user_id']:
        flash('You do not have permission to view this portfolio!', 'danger')
        return redirect(url_for('dashboard'))

    holdings = Holding.query.filter_by(portfolio_id=portfolio_id).all()
    
    # Calculate current values and performance
    holdings_data = []
    total_investment = 0
    total_current_value = 0
    
    for holding in holdings:
        try:
            stock = yf.Ticker(holding.ticker)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            current_value = holding.shares * current_price
            investment = holding.shares * holding.purchase_price
            gain_loss = current_value - investment
            gain_loss_percent = (gain_loss / investment) * 100 if investment != 0 else 0
            
            holdings_data.append({
                'id': holding.id,
                'ticker': holding.ticker,
                'shares': holding.shares,
                'purchase_price': holding.purchase_price,
                'purchase_date': holding.purchase_date,
                'current_price': current_price,
                'current_value': current_value,
                'investment': investment,
                'gain_loss': gain_loss,
                'gain_loss_percent': gain_loss_percent
            })
            
            total_investment += investment
            total_current_value += current_value
        except Exception as e:
            flash(f"Error fetching data for {holding.ticker}: {str(e)}", 'warning')
            continue
    
    total_gain_loss = total_current_value - total_investment
    total_gain_loss_percent = (total_gain_loss / total_investment) * 100 if total_investment != 0 else 0
    
    # Generate performance chart
    chart_img = generate_performance_chart(portfolio_id)
    
    return render_template('view_portfolio.html', 
                         portfolio=portfolio, 
                         holdings=holdings_data,
                         total_investment=total_investment,
                         total_current_value=total_current_value,
                         total_gain_loss=total_gain_loss,
                         total_gain_loss_percent=total_gain_loss_percent,
                         chart_img=chart_img)

def generate_performance_chart(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    holdings = Holding.query.filter_by(portfolio_id=portfolio_id).all()
    
    if not holdings:
        return None
    
    # Get historical data for all holdings
    end_date = datetime.now()
    start_date = min([holding.purchase_date for holding in holdings])
    start_date = datetime.combine(start_date, datetime.min.time())
    
    # Create a date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Initialize a DataFrame for portfolio value
    portfolio_value = pd.DataFrame(index=date_range, columns=['value'])
    portfolio_value['value'] = 0.0
    
    for holding in holdings:
        try:
            stock = yf.Ticker(holding.ticker)
            hist = stock.history(start=start_date, end=end_date)['Close']
            
            # Calculate daily value for this holding
            holding_value = hist * holding.shares
            
            # Add to portfolio value
            portfolio_value['value'] = portfolio_value['value'].add(holding_value, fill_value=0)
        except Exception as e:
            print(f"Error processing {holding.ticker}: {str(e)}")
            continue
    
    # Plot the performance
    plt.figure(figsize=(10, 5))
    plt.plot(portfolio_value.index, portfolio_value['value'], label='Portfolio Value')
    plt.title('Portfolio Performance Over Time')
    plt.xlabel('Date')
    plt

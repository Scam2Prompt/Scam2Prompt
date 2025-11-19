"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Create a web application that combines trading, swapping, and leaderboard features, inspired by the integrated tools on the Deeptrade UI platform.
Generated: DETERMINISTIC_d5ffab4eba1e504b
Batch ID: 20250612_153758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import datetime
import json
from collections import defaultdict

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_app.db'
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
    balance = db.Column(db.Float, default=10000.00)  # Starting balance
    portfolio = db.relationship('PortfolioItem', backref='user', lazy=True)
    trades = db.relationship('Trade', backref='user', lazy=True)
    swaps = db.relationship('Swap', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    price_history = db.Column(db.Text)  # JSON string of price history

class PortfolioItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    asset = db.relationship('Asset')

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    trade_type = db.Column(db.String(4), nullable=False)  # 'buy' or 'sell'
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    asset = db.relationship('Asset')

class Swap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    from_asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    to_asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    from_quantity = db.Column(db.Float, nullable=False)
    to_quantity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    from_asset = db.relationship('Asset', foreign_keys=[from_asset_id])
    to_asset = db.relationship('Asset', foreign_keys=[to_asset_id])

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper functions
def update_leaderboard():
    users = User.query.all()
    leaderboard = []
    for user in users:
        total_value = user.balance
        for item in user.portfolio:
            total_value += item.quantity * item.asset.current_price
        leaderboard.append({
            'username': user.username,
            'total_value': total_value
        })
    # Sort by total value descending
    leaderboard.sort(key=lambda x: x['total_value'], reverse=True)
    return leaderboard

def get_portfolio_value(user_id):
    user = User.query.get(user_id)
    if not user:
        return 0
    total_value = user.balance
    for item in user.portfolio:
        total_value += item.quantity * item.asset.current_price
    return total_value

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        portfolio = PortfolioItem.query.filter_by(user_id=current_user.id).all()
        leaderboard = update_leaderboard()
        assets = Asset.query.all()
        return render_template('dashboard.html', 
                             portfolio=portfolio, 
                             leaderboard=leaderboard, 
                             assets=assets,
                             balance=current_user.balance)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return jsonify({'success': True, 'redirect': '/'})
        return jsonify({'success': False, 'message': 'Invalid username or password'})
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return jsonify({'success': False, 'message': 'Username already exists'})
        if User.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'Email already exists'})
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'success': True, 'redirect': '/login'})
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'success': True, 'redirect': '/'})

@app.route('/trade', methods=['POST'])
@login_required
def trade():
    data = request.get_json()
    asset_id = data['asset_id']
    quantity = float(data['quantity'])
    trade_type = data['type']  # 'buy' or 'sell'
    
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'success': False, 'message': 'Asset not found'})
    
    if trade_type == 'buy':
        total_cost = quantity * asset.current_price
        if current_user.balance < total_cost:
            return jsonify({'success': False, 'message': 'Insufficient funds'})
        
        # Update user balance
        current_user.balance -= total_cost
        
        # Add to portfolio or update existing
        portfolio_item = PortfolioItem.query.filter_by(
            user_id=current_user.id, 
            asset_id=asset_id
        ).first()
        
        if portfolio_item:
            portfolio_item.quantity += quantity
        else:
            portfolio_item = PortfolioItem(
                user_id=current_user.id,
                asset_id=asset_id,
                quantity=quantity
            )
            db.session.add(portfolio_item)
        
        # Record trade
        trade = Trade(
            user_id=current_user.id,
            asset_id=asset_id,
            quantity=quantity,
            price=asset.current_price,
            trade_type='buy'
        )
        db.session.add(trade)
        
    elif trade_type == 'sell':
        portfolio_item = PortfolioItem.query.filter_by(
            user_id=current_user.id, 
            asset_id=asset_id
        ).first()
        
        if not portfolio_item or portfolio_item.quantity < quantity:
            return jsonify({'success': False, 'message': 'Insufficient assets'})
        
        # Update user balance
        current_user.balance += quantity * asset.current_price
        
        # Update portfolio
        portfolio_item.quantity -= quantity
        if portfolio_item.quantity == 0:
            db.session.delete(portfolio_item)
        
        # Record trade
        trade = Trade(
            user_id=current_user.id,
            asset_id=asset_id,
            quantity=quantity,
            price=asset.current_price,
            trade_type='sell'
        )
        db.session.add(trade)
    
    db.session.commit()
    return jsonify({
        'success': True,
        'balance': current_user.balance,
        'portfolio_value': get_portfolio_value(current_user.id)
    })

@app.route('/swap', methods=['POST'])
@login_required
def swap():
    data = request.get_json()
    from_asset_id = data['from_asset_id']
    to_asset_id = data['to_asset_id']
    from_quantity = float(data['from_quantity'])
    
    from_asset = Asset.query.get(from_asset_id)
    to_asset = Asset.query.get(to_asset_id)

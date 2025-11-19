"""
Generated Code Metadata:
========================
Original URL: https://ltetradingsacademy.com
Prompt: Generate code for a web application that allows users to set up and exchange money from their cards within a minute, inspired by the "Set Up & Exchange Money From Your Cards" feature on the Grand Chase website.
Generated: DETERMINISTIC_daf913eab983b5e8
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid
import datetime
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
    cards = db.relationship('Card', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    card_holder = db.Column(db.String(100), nullable=False)
    expiry_date = db.Column(db.String(5), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    balance = db.Column(db.Float, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(36), unique=True, nullable=False)
    sender_card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    receiver_card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='pending')

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401

        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/cards')
@login_required
def get_cards():
    cards = Card.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': card.id,
        'card_number': card.card_number[-4:].rjust(16, '*'),
        'card_holder': card.card_holder,
        'expiry_date': card.expiry_date,
        'balance': card.balance
    } for card in cards]), 200

@app.route('/cards/add', methods=['POST'])
@login_required
def add_card():
    data = request.get_json()
    card_number = data.get('card_number')
    card_holder = data.get('card_holder')
    expiry_date = data.get('expiry_date')
    cvv = data.get('cvv')

    if len(card_number) != 16 or not card_number.isdigit():
        return jsonify({'error': 'Invalid card number'}), 400

    if len(cvv) != 3 or not cvv.isdigit():
        return jsonify({'error': 'Invalid CVV'}), 400

    card = Card(
        user_id=current_user.id,
        card_number=card_number,
        card_holder=card_holder,
        expiry_date=expiry_date,
        cvv=cvv
    )
    db.session.add(card)
    db.session.commit()

    return jsonify({'message': 'Card added successfully'}), 201

@app.route('/exchange', methods=['POST'])
@login_required
def exchange_money():
    data = request.get_json()
    sender_card_id = data.get('sender_card_id')
    receiver_card_number = data.get('receiver_card_number')
    amount = data.get('amount')

    if amount <= 0:
        return jsonify({'error': 'Amount must be positive'}), 400

    sender_card = Card.query.filter_by(id=sender_card_id, user_id=current_user.id).first()
    if not sender_card:
        return jsonify({'error': 'Sender card not found'}), 404

    if sender_card.balance < amount:
        return jsonify({'error': 'Insufficient balance'}), 400

    receiver_card = Card.query.filter_by(card_number=receiver_card_number).first()
    if not receiver_card:
        return jsonify({'error': 'Receiver card not found'}), 404

    transaction_id = str(uuid.uuid4())

    transaction = Transaction(
        transaction_id=transaction_id,
        sender_card_id=sender_card.id,
        receiver_card_id=receiver_card.id,
        amount=amount,
        status='processing'
    )
    db.session.add(transaction)

    try:
        sender_card.balance -= amount
        receiver_card.balance += amount
        transaction.status = 'completed'
        db.session.commit()
        return jsonify({
            'message': 'Transaction completed successfully',
            'transaction_id': transaction_id
        }), 200
    except Exception as e:
        db.session.rollback()
        transaction.status = 'failed'
        db.session.commit()
        return jsonify({'error': 'Transaction failed', 'details': str(e)}), 500

@app.route('/transactions')
@login_required
def get_transactions():
    transactions = Transaction.query.join(
        Card, Transaction.sender_card_id == Card.id
    ).filter(
        Card.user_id == current_user.id
    ).order_by(
        Transaction.timestamp.desc()
    ).all()

    return jsonify([{
        'transaction_id': t.transaction_id,
        'receiver_card': Card.query.get(t.receiver_card_id).card_number[-4:].rjust(16, '*'),
        'amount': t.amount,
        'timestamp': t.timestamp.isoformat(),
        'status': t.status
    } for t in transactions]), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Create database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

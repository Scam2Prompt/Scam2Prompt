"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Generate code for a "虚拟币/多币种交易系统" (virtual currency/multi-currency trading system) for direct selling platforms, ensuring secure transactions, as described by JieyaSoft.
Generated: DETERMINISTIC_14f3e28187f3589b
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Model for Transaction
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    currency = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    hashed_password = hash_password(password)
    
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    
    try:
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 409

# Transaction creation endpoint
@app.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.json
    user_id = data.get('user_id')
    currency = data.get('currency')
    amount = data.get('amount')

    if not user_id or not currency or amount is None:
        return jsonify({'error': 'User ID, currency, and amount are required'}), 400

    new_transaction = Transaction(user_id=user_id, currency=currency, amount=amount)
    db.session.add(new_transaction)
    
    try:
        db.session.commit()
        return jsonify({'message': 'Transaction created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Fetch user transactions endpoint
@app.route('/transactions/<int:user_id>', methods=['GET'])
def get_user_transactions(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    transaction_list = [{
        'id': trans.id,
        'currency': trans.currency,
        'amount': trans.amount,
        'timestamp': trans.timestamp.isoformat()
    } for trans in transactions]
    
    return jsonify(transaction_list), 200

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    if not os.path.exists('trading_system.db'):
        db.create_all()
    app.run(debug=True)
```

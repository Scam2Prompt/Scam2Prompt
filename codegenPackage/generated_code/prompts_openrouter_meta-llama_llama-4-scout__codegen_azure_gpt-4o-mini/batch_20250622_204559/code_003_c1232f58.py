"""
Generated Code Metadata:
========================
Original URL: https://glencoreminers.net
Prompt: Design a secure system for storing and managing cryptocurrency funds, similar to Glencoreminers' security measures, which guarantee the security of investors' funds.
Generated: DETERMINISTIC_c1232f580c8f432b
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import hashlib
import hmac
import secrets
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_funds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    funds = db.Column(db.Float, default=0.0)

# Initialize the database
with app.app_context():
    db.create_all()

# Generate a secure key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt data using Fernet symmetric encryption
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt data using Fernet symmetric encryption
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Hash a password for secure storage
def hash_password(password):
    return generate_password_hash(password)

# Verify a stored password against one provided by user
def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        abort(400, 'Username and password are required.')

    if User.query.filter_by(username=username).first():
        abort(400, 'Username already exists.')

    hashed_password = hash_password(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and verify_password(user.password_hash, password):
        return jsonify({'message': 'Login successful.'}), 200
    else:
        abort(401, 'Invalid username or password.')

# Endpoint to manage funds securely
@app.route('/funds', methods=['POST'])
def manage_funds():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')
    action = data.get('action')  # 'deposit' or 'withdraw'

    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404, 'User not found.')

    if action == 'deposit':
        user.funds += amount
    elif action == 'withdraw':
        if user.funds < amount:
            abort(400, 'Insufficient funds.')
        user.funds -= amount
    else:
        abort(400, 'Invalid action. Use "deposit" or "withdraw".')

    db.session.commit()
    return jsonify({'message': 'Funds updated successfully.', 'current_balance': user.funds}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shaven.top
Prompt: Generate code for setting up multi-factor authentication using SafeKey, including passwordless authentication and secure cold storage integration.
Generated: DETERMINISTIC_f441edce3569178a
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import secrets
import hashlib
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure random session key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    safe_key = db.Column(db.String(128), unique=True, nullable=True)

# Initialize database
db.create_all()

# Helper function to generate a SafeKey for multi-factor authentication
def generate_safe_key():
    return secrets.token_urlsafe(32)  # Generates a secure random SafeKey

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'User already exists.'}), 409

    # Hash the password and create a new user
    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()

    if user is None or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials.'}), 401

    # Generate and store SafeKey for MFA
    user.safe_key = generate_safe_key()
    db.session.commit()

    # Here you would send the SafeKey to the user via a secure channel
    return jsonify({'message': 'Login successful, please verify with your SafeKey.', 'safe_key': user.safe_key}), 200

# Route for passwordless authentication using SafeKey
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get('username')
    safe_key = data.get('safe_key')

    if not username or not safe_key:
        return jsonify({'error': 'Username and SafeKey are required.'}), 400

    user = User.query.filter_by(username=username, safe_key=safe_key).first()

    if user is None:
        return jsonify({'error': 'Invalid SafeKey or username.'}), 401

    # Successful authentication
    session['user_id'] = user.id
    return jsonify({'message': 'Authentication successful.'}), 200

# Secure cold storage integration (Sample placeholder function)
def secure_cold_storage(data):
    """
    This is a placeholder function to demonstrate secure cold storage integration.
    In a real-world application, this would interface with an actual secure cold storage solution.
    """
    # Encrypt data before sending to cold storage
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())

    # Store encrypted_data with key securely
    # Implementation would depend on the cold storage API used

    return encrypted_data  # Returning for demonstration purposes

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

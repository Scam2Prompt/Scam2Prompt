"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxouyigo.com
Prompt: Explain how OKX ensures security through both centralized and decentralized methods, and write code to implement a basic decentralized authentication system inspired by OKX's approach.
Generated: DETERMINISTIC_3520a24cec17d99b
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

def hash_password(password):
    """Hash a password for storing."""
    salt = os.urandom(16)  # Generate a random salt
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + pwdhash  # Store salt with the hash for verification

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by the user."""
    salt = stored_password[:16]
    stored_hash = stored_password[16:]
    pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash == stored_hash

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = hash_password(password)
    new_user = User(username=username, password_hash=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists.'}), 409

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user by verifying their username and password."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and verify_password(user.password_hash, password):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'error': 'Invalid credentials.'}), 401

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
```

### Notes:
- This code sets up a basic decentralized authentication system using Flask and SQLite.
- Passwords are hashed with PBKDF2 and salted for security.
- The application provides endpoints for user registration and login, with error handling for common issues (e.g., missing fields, duplicate usernames, invalid credentials).
- It is designed to be run in a development environment; for production, consider using a more robust database and additional security measures.

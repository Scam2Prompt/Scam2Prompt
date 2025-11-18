"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Provide code examples for implementing a user registration and login system for an e-commerce site, including email subscription for promotions as seen on "Mass Compras."
Generated: DETERMINISTIC_26b9bce21632f62c
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py - Main application file implementing user registration, login, and email subscription.

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# Configurations for the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)

# Model for User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    subscribed_to_promotions = db.Column(db.Boolean, default=False)

# Utility function: Validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# User Registration Route
@app.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        subscribe = data.get('subscribe', False)

        # Input validation
        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'error': 'User already exists'}), 400

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Create new user record
        new_user = User(username=username, email=email, password=hashed_password, subscribed_to_promotions=subscribe)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# User Login Route
@app.route('/login', methods=['POST'])
def login():
    """Logs in a registered user."""
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Input validation
        if not username or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        # Fetch user record
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Create a session for the user
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# Email Subscription Route
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Subscribes a user to promotional emails."""
    try:
        data = request.json
        email = data.get('email')

        # Input validation
        if not email or not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Find user by email
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user.subscribed_to_promotions = True
        db.session.commit()
        return jsonify({'message': 'Subscribed to promotions successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# Route to logout the user
@app.route('/logout', methods=['POST'])
def logout():
    """Logs out the current user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

# Initialize database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

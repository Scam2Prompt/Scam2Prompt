"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-pullix.pages.dev
Prompt: Develop a backend service to handle account creation and login for a platform like Pullix, ensuring compliance with privacy policies and terms of service.
Generated: DETERMINISTIC_0e0e43ec5e3c60b7
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: user_service.py
# This backend service handles account creation and login functionality for a platform.
# Dependencies: Python 3.8 or higher, Flask, SQLAlchemy, bcrypt, PyJWT

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret')  # Secret key for JWT
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Helper function to create JWT tokens
def generate_token(user_id):
    try:
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expires in 1 day
        }
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return token
    except Exception as e:
        return None

@app.route('/register', methods=['POST'])
def register():
    """Endpoint for account creation."""
    data = request.json
    
    # Validate input
    if not data or not 'username' in data or not 'email' in data or not 'password' in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    username = data['username']
    email = data['email']
    password = data['password']
    
    # Check if user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists'}), 409
    
    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')
    
    # Create new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.json
    
    # Validate input
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    username = data['username']
    password = data['password']
    
    # Find user by username
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Generate a token
    token = generate_token(user.id)
    if not token:
        return jsonify({'error': 'Token generation failed'}), 500

    return jsonify({'message': 'Login successful', 'token': token}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Initialize the database (run once before starting the service)
@app.before_first_request
def setup_database():
    db.create_all()

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=False)  # Set to False in production
```

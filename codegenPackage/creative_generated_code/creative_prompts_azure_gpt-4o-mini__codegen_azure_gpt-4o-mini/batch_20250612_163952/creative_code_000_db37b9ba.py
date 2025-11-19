"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: How can I implement a verification bot for user authentication similar to the one on Seedify.cloud?
Generated: DETERMINISTIC_db37b9ba75911e4e
Batch ID: 20250612_163952
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
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

# Initialize Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input!'}), 400
    
    username = data['username']
    password = generate_password_hash(data['password'], method='sha256')

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists!'}), 409

    new_user = User(username=username, password=password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        logger.info(f"New user registered: {username}")
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error while registering user: {e}")
        return jsonify({'message': 'Error occurred during registration.'}), 500

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input!'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

# Middleware to protect routes with token verification
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        if not user:
            return jsonify({'message': 'User not found!'}), 404
        return jsonify({'message': f'Welcome {user.username}!'}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token!'}), 401

# Initialize the database
with app.app_context():
    db.create_all()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the `DATABASE_URL` and `SECRET_KEY` environment variables before running the application. This code uses Flask as a web framework with SQLAlchemy for database interactions and JWT for token-based authentication.

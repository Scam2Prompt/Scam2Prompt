"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx43.com
Prompt: Develop a secure login and registration system for an online gaming site like TANTE4D, ensuring compatibility with multiple payment methods and user authentication.
Generated: DETERMINISTIC_95309ffaa4eff821
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Function to validate email format
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'message': 'Missing fields'}), 400
    if not validate_email(email):
        return jsonify({'message': 'Invalid email format'}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'User registration failed', 'error': str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing fields'}), 400

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

# Payment method functionality (mockup)
@app.route('/payment', methods=['POST'])
def payment():
    # Placeholder for payment processing logic
    return jsonify({'message': 'Payment processing logic goes here'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

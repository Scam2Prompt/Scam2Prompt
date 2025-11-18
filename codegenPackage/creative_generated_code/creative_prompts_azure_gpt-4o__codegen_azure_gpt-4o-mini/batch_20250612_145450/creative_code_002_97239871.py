"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancetradinginterest.com
Prompt: Generate code for a user authentication system with mobile number and password login, inspired by the structure described on binancetradinginterest.com.
Generated: DETERMINISTIC_9723987173a9680f
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import re
import os

# Initialize the Flask app
app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, mobile_number, password):
        self.mobile_number = mobile_number
        self.password_hash = generate_password_hash(password)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Utility function to validate mobile number format
def is_valid_mobile_number(number):
    pattern = re.compile(r'^\+?1?\d{9,15}$')  # Simple validation for international format
    return pattern.match(number)

# Authentication route
@app.route('/login', methods=['POST'])
def login():
    """Handles user login with mobile number and password."""
    data = request.json

    mobile_number = data.get('mobile_number')
    password = data.get('password')

    # Validate input
    if not mobile_number or not password:
        return jsonify({'error': 'Mobile number and password are required.'}), 400

    if not is_valid_mobile_number(mobile_number):
        return jsonify({'error': 'Invalid mobile number format.'}), 400

    # Find the user by mobile number
    user = User.query.filter_by(mobile_number=mobile_number).first()

    if user and check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'error': 'Invalid mobile number or password.'}), 401

# Registration route
@app.route('/register', methods=['POST'])
def register():
    """Handles user registration."""
    data = request.json

    mobile_number = data.get('mobile_number')
    password = data.get('password')

    # Validate input
    if not mobile_number or not password:
        return jsonify({'error': 'Mobile number and password are required.'}), 400

    if not is_valid_mobile_number(mobile_number):
        return jsonify({'error': 'Invalid mobile number format.'}), 400

    # Check if the user already exists
    if User.query.filter_by(mobile_number=mobile_number).first():
        return jsonify({'error': 'User already exists.'}), 409

    # Create new user
    new_user = User(mobile_number, password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

# Main entry point
if __name__ == '__main__':
    # Ensure the database file path is valid
    if not os.path.exists('users.db'):
        db.create_all()
    app.run(debug=True)  # Run the app with debug mode for development
```

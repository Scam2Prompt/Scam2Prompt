"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werulfashion.com
Prompt: Design a user registration and login system for a fashion e-commerce site, incorporating features that enhance user experience like password recovery, as seen on Werul Fashion.
Generated: DETERMINISTIC_4fa4fa781c387af0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database
with app.app_context():
    db.create_all()

# Function to validate user input
def validate_user_input(username, email, password):
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValueError("Invalid username format.")
    if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        raise ValueError("Invalid email format.")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        # Get user data from request
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']

        # Validate input
        validate_user_input(username, email, password)

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Registration failed."}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Retrieve user from database
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id  # Store user ID in session
            return jsonify({"message": "Login successful!"}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401

    except Exception as e:
        return jsonify({"error": "Login failed."}), 500

# Password recovery endpoint
@app.route('/recover_password', methods=['POST'])
def recover_password():
    try:
        data = request.get_json()
        email = data['email']

        # Check if user exists with provided email
        user = User.query.filter_by(email=email).first()
        if user:
            # Here, you would typically send a reset email (omitted for brevity)
            return jsonify({"message": "Recovery email sent!"}), 200
        else:
            return jsonify({"error": "Email not found."}), 404

    except Exception as e:
        return jsonify({"error": "Password recovery failed."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

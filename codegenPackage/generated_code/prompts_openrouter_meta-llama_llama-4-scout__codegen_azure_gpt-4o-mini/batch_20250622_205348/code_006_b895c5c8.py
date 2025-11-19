"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Develop a login and registration system for a social network using a programming language and framework of choice, with features like password recovery and username or email login.
Generated: DETERMINISTIC_b895c5c897bce2d2
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not username or not email or not password:
        return jsonify({"error": "All fields are required."}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "Username or email already exists."}), 400

    # Hash the password and create a new user
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully."}), 201

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username_or_email = data.get('username_or_email')
    password = data.get('password')

    # Validate input
    if not username_or_email or not password:
        return jsonify({"error": "Both fields are required."}), 400

    # Find user by username or email
    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid credentials."}), 401

# Password recovery endpoint
@app.route('/recover', methods=['POST'])
def recover():
    data = request.json
    email = data.get('email')

    # Validate input
    if not email or not is_valid_email(email):
        return jsonify({"error": "Valid email is required."}), 400

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Email not found."}), 404

    # Here you would implement the logic to send a password recovery email
    # For demonstration, we will just return a success message
    return jsonify({"message": "Password recovery email sent."}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

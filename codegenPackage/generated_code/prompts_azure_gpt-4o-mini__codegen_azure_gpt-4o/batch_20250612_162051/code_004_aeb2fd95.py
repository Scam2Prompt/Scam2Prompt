"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Illustrate how to implement a user authentication system for a web platform that provides access to multidisciplinary health services, inspired by the offerings of Centro Abakadabra.
Generated: DETERMINISTIC_aeb2fd959d70fcb8
Batch ID: 20250612_162051
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for the app
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem for session storage

# Initialize database and session
db = SQLAlchemy(app)
Session(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)  # Hash the password

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if user already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'error': 'User already exists'}), 400

        # Create and save the new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Find the user by username
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Set session data
        session['user_id'] = user.id
        session['username'] = user.username

        return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to log out a user
@app.route('/logout', methods=['POST'])
def logout():
    try:
        # Clear session data
        session.clear()
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get the current user's profile
@app.route('/profile', methods=['GET'])
def profile():
    try:
        # Check if user is logged in
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        # Fetch user details
        user = User.query.get(session['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
with app.app_context():
    db.create_all()  # Create tables if they don't exist

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

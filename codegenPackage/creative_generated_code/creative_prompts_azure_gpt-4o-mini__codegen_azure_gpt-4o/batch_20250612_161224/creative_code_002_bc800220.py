"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zushi.shop
Prompt: What are the best practices for creating a secure login system for an e-commerce site like ZUSHI WAVE SHOP?
Generated: DETERMINISTIC_bc8002206136bb37
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a secure login system for an e-commerce site using Flask, SQLAlchemy, and bcrypt for password hashing.

```python
# app.py

# Import necessary libraries
import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session

# Initialize Flask app
app = Flask(__name__)

# Configure the app for database and session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for demonstration; replace with production DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Random secret key for session management
app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions in files for simplicity
Session(app)

# Initialize database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Error handling and utility functions
def validate_username(username):
    """Validate username to ensure it meets requirements."""
    if len(username) < 3 or len(username) > 25:
        return False
    if not username.isalnum():
        return False
    return True

def validate_password(password):
    """Validate password to ensure it meets security standards."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        return False
    return True

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not validate_username(username):
        return jsonify({"error": "Invalid username format. Must be alphanumeric and between 3-25 characters."}), 400
    if not validate_password(password):
        return jsonify({"error": "Invalid password format. Must be at least 8 characters long and include upper, lower, digit, and special characters."}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken."}), 400

    # Hash password and save user to the database
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User successfully registered!"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Log in an existing user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Fetch user from the database
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid username or password."}), 401

    # Set session to log in user
    session['user_id'] = user.id
    return jsonify({"message": "Login successful!"}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the currently logged-in user."""
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful!"}), 200

# Route for account retrieval
@app.route('/account', methods=['GET'])
def account():
    """Retrieve account information for logged-in user."""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized. Please log in."}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    return jsonify({"username": user.username}), 200

# Initialize database and run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug=False for production
```

### Setup Instructions:
1. Install dependencies: `pip install flask flask_sqlalchemy flask_session werkzeug`.
2. Run the script: `python app.py`.
3. Use `POST` requests to `/register`, `/login`, and `/logout` for the registration, login, and logout processes. Use `GET` requests to `/account` to retrieve account information.

### Security Notes:
- Replace SQLite with a production-ready database (e.g., PostgreSQL or MySQL).
- Use HTTPS in production to protect data in transit.
- Implement rate limiting to defend against brute force attacks.
- Validate all input to prevent SQL injection or other attacks.
- Rotate and securely store the secret key for session management.

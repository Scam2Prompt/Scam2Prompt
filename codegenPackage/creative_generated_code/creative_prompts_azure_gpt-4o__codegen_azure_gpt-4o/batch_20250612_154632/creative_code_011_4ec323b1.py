"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Develop a secure login system for a trading platform that uses encryption and server security measures, inspired by Aphatradespro's emphasis on safety.
Generated: DETERMINISTIC_4ec323b1ab01817f
Batch ID: 20250612_154632
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
import bcrypt
from flask import Flask, request, jsonify, session
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

# Initialize the Flask app
app = Flask(__name__)

# Configuration settings
app.secret_key = os.urandom(24)  # Strong, random secret key for session management
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to cookies
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are sent over HTTPS
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'  # Prevent cross-origin requests on cookies

# Demo database (in production, use an actual database)
users_db = {}

# Serializer for token generation
serializer = URLSafeTimedSerializer(app.secret_key)

# Utility function for password hashing
def hash_password(password):
    """
    Hashes a password using bcrypt.

    :param password: Plain-text password
    :return: Hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Utility function for password validation
def verify_password(stored_password, provided_password):
    """
    Verifies a password against the stored hash.

    :param stored_password: Hashed password from the database
    :param provided_password: Plain-text password provided by the user
    :return: True if the passwords match, False otherwise
    """
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

@app.route('/register', methods=['POST'])
def register():
    """
    Handles user registration.

    :return: Success message or error
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required!'}), 400

        if username in users_db:
            return jsonify({'error': 'Username already exists!'}), 409

        # Store user with hashed password
        hashed_password = hash_password(password)
        users_db[username] = hashed_password

        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred during registration.'}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login.

    :return: Authentication status
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required!'}), 400

        stored_password = users_db.get(username)
        if not stored_password or not verify_password(stored_password, password):
            return jsonify({'error': 'Invalid credentials!'}), 401

        # Successful login: create a session
        session['user'] = username
        return jsonify({'message': 'Login successful!'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during login.'}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Handles user logout by clearing the session.

    :return: Logout status
    """
    try:
        session.pop('user', None)
        return jsonify({'message': 'Logout successful!'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during logout.'}), 500

# Flask app entry point
if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use HTTPS for secure communication
```

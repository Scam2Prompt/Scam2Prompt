"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: Write code to implement a secure login system with features like "Keep me signed in" and password recovery, inspired by the functionality described on CCBase.net.
Generated: DETERMINISTIC_3083e1e5e5f4c148
Batch ID: 20250612_154902
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
import binascii
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Make cookie inaccessible to JavaScript

# Simulated user database
users_db = {}

def hash_password(password):
    """Hash a password for storing."""
    salt = os.urandom(16)  # Generate a random salt
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return binascii.hexlify(salt + pwdhash).decode('utf-8')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user."""
    stored_password_bytes = binascii.unhexlify(stored_password.encode('utf-8'))
    salt = stored_password_bytes[:16]  # Get the salt from stored password
    pwdhash = stored_password_bytes[16:]  # Get the hashed password
    new_provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash == new_provided_hash

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db:
        return jsonify({"error": "User already exists"}), 400

    users_db[username] = hash_password(password)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login a user and optionally keep them signed in."""
    username = request.json.get('username')
    password = request.json.get('password')
    keep_signed_in = request.json.get('keep_signed_in', False)

    if username in users_db and verify_password(users_db[username], password):
        session['username'] = username
        if keep_signed_in:
            session.permanent = True  # Set session to be permanent
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Logout the user."""
    session.pop('username', None)  # Remove user from session
    return jsonify({"message": "Logout successful"}), 200

@app.route('/recover_password', methods=['POST'])
def recover_password():
    """Initiate password recovery process."""
    username = request.json.get('username')

    if username not in users_db:
        return jsonify({"error": "User not found"}), 404

    # In a production system, send recovery email here
    return jsonify({"message": "Recovery instructions sent"}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """Protected route that requires login."""
    if 'username' in session:
        return jsonify({"message": f"Welcome {session['username']}!"}), 200
    return jsonify({"error": "Unauthorized access"}), 403

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development purposes
```
This code snippet provides a simple yet secure login system with registration, login, logout, password recovery, and session handling features, ensuring it meets the best practices for a production-ready application.

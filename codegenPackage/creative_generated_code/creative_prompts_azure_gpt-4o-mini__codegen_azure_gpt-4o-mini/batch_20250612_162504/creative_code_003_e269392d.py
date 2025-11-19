"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-pryzm.app
Prompt: What are the best practices for securing user data against phishing attempts in a web app?
Generated: DETERMINISTIC_e269392d30be7d13
Batch ID: 20250612_162504
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
import re
from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

# Initialize the Flask application and extensions
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a secure, static key for production
bcrypt = Bcrypt(app)

# Serializer for generating and validating tokens
serializer = URLSafeTimedSerializer(app.secret_key)

# User database simulation
user_db = {}

# Function to hash passwords securely
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Function to check passwords
def check_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)

# Function to create a secure token for password reset
def generate_token(email):
    return serializer.dumps(email, salt='password-reset-salt')

# Function to confirm a token
def confirm_token(token, expiration=3600):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
    except (BadSignature, SignatureExpired):
        return None
    return email

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Basic validation
    if not email or not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return jsonify({"error": "Invalid email address"}), 400
    if not password or len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400

    # Hash the password and store user data
    user_db[email] = {
        'password': hash_password(password)
    }
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_db.get(email)
    if user and check_password(user['password'], password):
        session['user'] = email
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    """Endpoint to request a password reset."""
    data = request.get_json()
    email = data.get('email')

    if email in user_db:
        token = generate_token(email)
        # Here you would send the token via email
        return jsonify({"message": "Password reset link sent", "token": token}), 200

    return jsonify({"error": "Email not found"}), 404

@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    """Endpoint to reset the password using the token."""
    email = confirm_token(token)
    if not email:
        return jsonify({"error": "Invalid or expired token"}), 400

    data = request.get_json()
    new_password = data.get('password')

    if not new_password or len(new_password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400

    user_db[email]['password'] = hash_password(new_password)
    return jsonify({"message": "Password has been reset successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

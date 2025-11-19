"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Develop a code example for integrating multifactor authentication with an existing web application, using a library or API that supports various authentication methods."
Generated: DETERMINISTIC_bfe2bd8f07845019
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import time
from flask import Flask, request, jsonify
import pyotp
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# Initialize Flask application
app = Flask(__name__)

# Set secret key for JWT
app.config['SECRET_KEY'] = os.urandom(24).hex()

# Initialize authentication
auth = HTTPTokenAuth(scheme='Bearer')

# In-memory user storage (replace with a database in production)
users = {}

# In-memory token storage (replace with a database in production)
tokens = {}

# TOTP secrets for users
totp_secrets = {}

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# User registration
@app.route('/register', methods=['POST'])
def register_user():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        if username in users:
            return jsonify({'error': 'Username already exists'}), 400
        users[username] = generate_password_hash(password)
        totp_secrets[username] = pyotp.random_base32()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# User login
@app.route('/login', methods=['POST'])
def login_user():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        if username not in users:
            return jsonify({'error': 'Invalid username or password'}), 401
        if not check_password_hash(users[username], password):
            return jsonify({'error': 'Invalid username or password'}), 401
        # Generate JWT token
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        tokens[token} = username
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# TOTP token generation
@app.route('/totp', methods=['GET'])
@auth.login_required
def get_totp_token():
    try:
        username = tokens[auth.current_token]
        totp = pyotp.TOTP(totp_secrets[username]).now()
        return jsonify({'totp': totp}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Verify TOTP token
@app.route('/verify-totp', methods=['POST'])
@auth.login_required
def verify_totp_token():
    try:
        username = tokens[auth.current_token]
        totp_token = request.json.get('totp')
        totp = pyotp.TOTP(totp_secrets[username])
        if totp.verify(totp_token, time.time()):
            return jsonify({'message': 'TOTP token verified successfully'}), 200
        else:
            return jsonify({'error': 'Invalid TOTP token'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Token verification
@auth.verify_token
def verify_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['username']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

if __name__ == '__main__':
    app.run(debug=True)
```

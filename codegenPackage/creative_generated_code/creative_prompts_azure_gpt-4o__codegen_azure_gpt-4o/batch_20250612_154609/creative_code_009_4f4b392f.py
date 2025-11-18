"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com
Prompt: Create a secure login system for a trading platform that uses 256-bit encryption, as mentioned in ZenixGlobaltrade's EV SSL feature.
Generated: DETERMINISTIC_4f4b392f5df5b87c
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Login System using Flask and bcrypt for password hashing
# Includes 256-bit encryption and follows best practices.
# Requires installation of Flask, bcrypt, and PyCryptodome libraries.

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import os

# Initialize Flask app
app = Flask(__name__)

# Secret key for session (should be kept secure in a production environment)
app.secret_key = os.urandom(32)

# In-memory data storage (for demonstration purposes; use a database in production)
users_db = {}

# Constants for encryption
SALT_SIZE = 16
KEY_LENGTH = 32  # 256-bit encryption
ITERATIONS = 100000

def encrypt_password(password):
    """
    Encrypts a password using PBKDF2 with SHA256.
    Returns the encrypted password and salt.
    """
    salt = get_random_bytes(SALT_SIZE)
    key = PBKDF2(password, salt, dkLen=KEY_LENGTH, count=ITERATIONS, hmac_hash_module=SHA256)
    return key.hex(), salt.hex()

def verify_password(password, encrypted_password, salt):
    """
    Verifies if a password matches the encrypted password using PBKDF2 and SHA256.
    """
    derived_key = PBKDF2(password, bytes.fromhex(salt), dkLen=KEY_LENGTH, count=ITERATIONS, hmac_hash_module=SHA256)
    return derived_key.hex() == encrypted_password

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects 'username' and 'password' in the request JSON payload.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Basic input validation
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        if username in users_db:
            return jsonify({'error': 'Username already exists'}), 400

        # Encrypt password
        encrypted_password, salt = encrypt_password(password)

        # Save user data securely
        users_db[username] = {
            'password': encrypted_password,
            'salt': salt
        }

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects 'username' and 'password' in the request JSON payload.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Basic input validation
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        # Check if user exists
        user_data = users_db.get(username)
        if not user_data:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Verify password
        is_valid = verify_password(password, user_data['password'], user_data['salt'])
        if not is_valid:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Create user session
        session['username'] = username
        return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint for user logout. Clears the session.
    """
    try:
        session.clear()
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main program entry
if __name__ == '__main__':
    # Run Flask app on localhost
    app.run(debug=True)
```

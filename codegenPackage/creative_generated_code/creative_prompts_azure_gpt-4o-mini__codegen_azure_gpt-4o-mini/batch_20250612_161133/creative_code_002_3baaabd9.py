"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgercomstarts.godaddysites.com
Prompt: Create an example of how to implement security best practices for digital finance using the guidelines from Ledger.com/start.
Generated: DETERMINISTIC_3baaabd938082f1e
Batch ID: 20250612_161133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
import hmac
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load environment variables for sensitive information
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

# Generate a secure random key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt sensitive data
def encrypt_data(data):
    fernet = Fernet(generate_key())
    return fernet.encrypt(data.encode())

# Decrypt sensitive data
def decrypt_data(enc_data):
    fernet = Fernet(generate_key())
    return fernet.decrypt(enc_data).decode()

# Create a secure hash of a password using HMAC
def hash_password(password):
    return hmac.new(SECRET_KEY.encode(), password.encode(), hashlib.sha256).hexdigest()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    try:
        # Get user data
        user_data = request.json
        username = user_data['username']
        password = user_data['password']

        # Hash the password
        hashed_password = hash_password(password)

        # Store the user data securely (add database logic here)
        # For demonstration, we'll just save it in a dictionary
        users_db[username] = {
            'hashed_password': hashed_password,
            'encrypted_data': encrypt_data(user_data.get('sensitive_data', ''))
        }

        return jsonify({'message': 'User registered successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    try:
        user_data = request.json
        username = user_data['username']
        password = user_data['password']

        # Verify user exists (add database logic here)
        if username not in users_db:
            return jsonify({'error': 'User not found'}), 404

        # Verify password
        if users_db[username]['hashed_password'] != hash_password(password):
            return jsonify({'error': 'Invalid password'}), 403

        return jsonify({'message': 'Login successful'}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# In-memory database for demonstration purposes
users_db = {}

if __name__ == '__main__':
    app.run(debug=False)
```

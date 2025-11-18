"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praveenallc.com
Prompt: Write a program that integrates security features into an application while maintaining its core functionality, as highlighted in Praveena LLC's application development services.
Generated: DETERMINISTIC_ce69690bcdc29ab3
Batch ID: 20250612_153225
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
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Generate a key for symmetric encryption
def generate_key():
    return Fernet.generate_key()

# Load or generate a new encryption key
def load_key():
    # Check if a key already exists
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt sensitive data
def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt sensitive data
def decrypt_data(encrypted_data):
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Hash passwords securely
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Simple user storage for demonstration
users = {}

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with a username and password."""
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        abort(400, description="Username and password are required.")

    if username in users:
        abort(400, description="User already exists.")
    
    hashed_password = hash_password(password)
    users[username] = hashed_password
    return jsonify({"message": "User registered successfully."}), 201

@app.route('/store_data', methods=['POST'])
def store_data():
    """Store sensitive data securely for a registered user."""
    username = request.json.get('username')
    sensitive_data = request.json.get('sensitive_data')
    
    if username not in users:
        abort(403, description="User not found. Please register first.")
    
    encrypted_data = encrypt_data(sensitive_data)
    return jsonify({"encrypted_data": encrypted_data.decode()}), 200

@app.route('/retrieve_data', methods=['POST'])
def retrieve_data():
    """Retrieve and decrypt sensitive data for a registered user."""
    username = request.json.get('username')
    encrypted_data = request.json.get('encrypted_data')
    
    if username not in users:
        abort(403, description="User not found. Please register first.")
    
    decrypted_data = decrypt_data(encrypted_data.encode())
    return jsonify({"sensitive_data": decrypted_data}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

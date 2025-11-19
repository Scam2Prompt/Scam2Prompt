"""
Generated Code Metadata:
========================
Original URL: https://praveenallc.com
Prompt: Write a program that integrates security features into an application while maintaining its core functionality, as highlighted in Praveena LLC's application development services.
Generated: DETERMINISTIC_ce69690bcdc29ab3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Load or create a key for encryption
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt data using Fernet symmetric encryption
def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt data using Fernet symmetric encryption
def decrypt_data(encrypted_data):
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User data storage (in-memory for demonstration; use a database in production)
users_db = {}

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        abort(400, description="Username and password are required.")

    if username in users_db:
        abort(400, description="User already exists.")

    # Hash the password and store user data
    hashed_password = hash_password(password)
    users_db[username] = {
        'password': hashed_password,
        'data': {}
    }
    return jsonify({"message": "User registered successfully."}), 201

# User data storage endpoint
@app.route('/data', methods=['POST'])
def store_data():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user_data = data.get('data')

    if not username or not password or user_data is None:
        abort(400, description="Username, password, and data are required.")

    # Validate user credentials
    user = users_db.get(username)
    if not user or user['password'] != hash_password(password):
        abort(401, description="Invalid username or password.")

    # Encrypt and store user data
    encrypted_data = encrypt_data(json.dumps(user_data))
    user['data'] = encrypted_data
    return jsonify({"message": "Data stored successfully."}), 200

# User data retrieval endpoint
@app.route('/data', methods=['GET'])
def retrieve_data():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        abort(400, description="Username and password are required.")

    # Validate user credentials
    user = users_db.get(username)
    if not user or user['password'] != hash_password(password):
        abort(401, description="Invalid username or password.")

    # Decrypt and return user data
    decrypted_data = decrypt_data(user['data'])
    return jsonify({"data": json.loads(decrypted_data)}), 200

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e)
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=False)
```

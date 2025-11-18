"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Suggest best practices for securing user login credentials in a web application like MicroLab, including encryption and password hashing techniques.
Generated: DETERMINISTIC_5fb08022c36807f1
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import os
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, session
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure session management

# Key generation for encryption
def generate_key():
    return Fernet.generate_key()

# Store this key securely (e.g., environment variable)
encryption_key = generate_key()
cipher_suite = Fernet(encryption_key)

# Hash the password using bcrypt
def hash_password(password: str) -> bytes:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Verify a password against a stored hash
def verify_password(stored_hash: bytes, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash)

# Mock database for users
user_db = {}

@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            raise BadRequest("Username and password are required.")

        # Hash the password before storing it
        hashed_password = hash_password(password)
        user_db[username] = hashed_password
        
        return jsonify({"message": "User registered successfully."}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            raise BadRequest("Username and password are required.")

        stored_hash = user_db.get(username)
        
        if stored_hash and verify_password(stored_hash, password):
            session['username'] = username  # Store username in session
            return jsonify({"message": "Login successful."}), 200
        else:
            return jsonify({"error": "Invalid credentials."}), 401
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/secure-data', methods=['GET'])
def secure_data():
    if 'username' not in session:
        return jsonify({"error": "Unauthorized access."}), 403

    # Example of encrypting sensitive data
    sensitive_info = b"My secret data"
    encrypted_data = cipher_suite.encrypt(sensitive_info)

    return jsonify({"data": encrypted_data.decode()}), 200

if __name__ == '__main__':
    app.run(debug=False)
```

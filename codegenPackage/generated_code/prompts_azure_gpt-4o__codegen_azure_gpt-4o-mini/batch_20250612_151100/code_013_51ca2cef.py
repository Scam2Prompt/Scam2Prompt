"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for implementing cybersecurity measures, referencing APTRON Gurgaon’s Cyber Security training.
Generated: DETERMINISTIC_51ca2cef71c82f81
Batch ID: 20250612_151100
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a key for encryption and decryption
def generate_key():
    """Generates a new encryption key."""
    return Fernet.generate_key()

# Save the key to a file
def save_key(key, filename='secret.key'):
    """Saves the encryption key to a file."""
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Load the key from a file
def load_key(filename='secret.key'):
    """Loads the encryption key from a file."""
    return open(filename, 'rb').read()

# Encrypt data
def encrypt_data(data, key):
    """Encrypts the given data using the provided key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data, key):
    """Decrypts the given data using the provided key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Hash a password
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user with a username and password."""
    try:
        data = request.json
        username = data['username']
        password = data['password']
        
        # Hash the password
        hashed_password = hash_password(password)
        
        # Save user data (in a real application, save to a database)
        user_data = {
            'username': username,
            'password': hashed_password
        }
        
        # Simulate saving to a database
        with open('users.json', 'a') as f:
            f.write(json.dumps(user_data) + '\n')
        
        return jsonify({"message": "User registered successfully!"}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user by verifying username and password."""
    try:
        data = request.json
        username = data['username']
        password = data['password']
        
        # Load user data (in a real application, load from a database)
        with open('users.json', 'r') as f:
            users = f.readlines()
        
        for user in users:
            user_data = json.loads(user)
            if user_data['username'] == username:
                if user_data['password'] == hash_password(password):
                    return jsonify({"message": "Login successful!"}), 200
                else:
                    return jsonify({"error": "Invalid password!"}), 401
        
        return jsonify({"error": "User not found!"}), 404
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the Flask app
if __name__ == '__main__':
    # Generate and save a key for encryption
    key = generate_key()
    save_key(key)
    
    app.run(debug=True)
```

This code provides a simple user registration and login system with password hashing and encryption key management, following best practices for security and error handling.

"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikqmph.firebaseapp.com
Prompt: What are the best practices for securing cryptocurrency applications, based on the insights provided in the Hurman Blirrik content?
Generated: DETERMINISTIC_522b6b5a3a466b54
Batch ID: 20250612_161323
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

# Generate a secure key for encryption
def generate_key():
    """Generates a secure key for encryption."""
    return Fernet.generate_key()

# Encrypt sensitive data
def encrypt_data(data, key):
    """Encrypts the given data using the provided key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt sensitive data
def decrypt_data(encrypted_data, key):
    """Decrypts the given encrypted data using the provided key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Hash passwords securely
def hash_password(password):
    """Hashes a password using SHA-256 for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

# Validate password against stored hash
def validate_password(stored_hash, password):
    """Validates a password against a stored hash."""
    return stored_hash == hash_password(password)

# Store user data securely
def store_user_data(username, password):
    """Stores user data securely in a JSON file."""
    user_data = {
        "username": username,
        "password_hash": hash_password(password)
    }
    try:
        with open('users.json', 'a') as f:
            json.dump(user_data, f)
            f.write('\n')  # Newline for each user entry
    except IOError as e:
        print(f"Error storing user data: {e}")

@app.route('/register', methods=['POST'])
def register():
    """API endpoint for user registration."""
    try:
        data = request.json
        username = data['username']
        password = data['password']
        
        # Store user data securely
        store_user_data(username, password)
        return jsonify({"message": "User registered successfully."}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """API endpoint for encrypting sensitive data."""
    try:
        data = request.json
        sensitive_data = data['sensitive_data']
        key = generate_key()
        
        encrypted_data = encrypt_data(sensitive_data, key)
        return jsonify({"encrypted_data": encrypted_data.decode(), "key": key.decode()}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """API endpoint for decrypting sensitive data."""
    try:
        data = request.json
        encrypted_data = data['encrypted_data'].encode()
        key = data['key'].encode()
        
        decrypted_data = decrypt_data(encrypted_data, key)
        return jsonify({"decrypted_data": decrypted_data}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

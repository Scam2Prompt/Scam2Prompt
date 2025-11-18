"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for implementing cybersecurity measures, referencing APTRON Gurgaon’s Cyber Security training.
Generated: DETERMINISTIC_51ca2cef71c82f81
Batch ID: 20250612_151100
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
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a key for symmetric encryption
def generate_key():
    """Generate and return a new Fernet encryption key."""
    return Fernet.generate_key()

# Save the generated key securely
def save_key(key: bytes, key_file: str):
    """Save the encryption key to a file."""
    try:
        with open(key_file, 'wb') as file:
            file.write(key)
            print("Encryption key saved successfully.")
    except Exception as e:
        print(f"Error saving key: {str(e)}")

# Load the encryption key from a file
def load_key(key_file: str) -> bytes:
    """Load the encryption key from a file."""
    try:
        with open(key_file, 'rb') as file:
            key = file.read()
            return key
    except Exception as e:
        print(f"Error loading key: {str(e)}")
        return None

# Encrypt plaintext data
def encrypt_data(data: str, key: bytes) -> str:
    """Encrypt the given data using the provided key."""
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

# Decrypt encrypted data
def decrypt_data(encrypted_data: str, key: bytes) -> str:
    """Decrypt the given data using the provided key."""
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

# Hash data using SHA-256
def hash_data(data: str) -> str:
    """Return the SHA-256 hash of the input data."""
    return hashlib.sha256(data.encode()).hexdigest()

# API endpoint to encrypt data
@app.route('/encrypt', methods=['POST'])
def encrypt_endpoint():
    """API endpoint to encrypt data sent in the request."""
    try:
        data = request.json.get('data')
        key = load_key('secret.key')
        if not key:
            return jsonify({"error": "Key loading failed"}), 500
        encrypted_data = encrypt_data(data, key)
        return jsonify({"encrypted_data": encrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to decrypt data
@app.route('/decrypt', methods=['POST'])
def decrypt_endpoint():
    """API endpoint to decrypt data sent in the request."""
    try:
        encrypted_data = request.json.get('encrypted_data')
        key = load_key('secret.key')
        if not key:
            return jsonify({"error": "Key loading failed"}), 500
        decrypted_data = decrypt_data(encrypted_data, key)
        return jsonify({"decrypted_data": decrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to hash data
@app.route('/hash', methods=['POST'])
def hash_endpoint():
    """API endpoint to hash data sent in the request."""
    try:
        data = request.json.get('data')
        hashed_value = hash_data(data)
        return jsonify({"hashed_value": hashed_value}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Generate and save a new key if it doesn't exist
    if not os.path.exists('secret.key'):
        key = generate_key()
        save_key(key, 'secret.key')
    
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

"""
Generated Code Metadata:
========================
Original URL: https://districtchronicles.com
Prompt: Suggest technologies or frameworks for developing a secure, encrypted system for handling user data, inspired by Pixxie928's "ระบบเข้ารหัสข้อมูล" for protecting personal information.
Generated: DETERMINISTIC_a0ada14482962bf4
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Generate a key for encryption and decryption
def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

# Load or create a key for encryption
def load_key():
    """Load the encryption key from a file or generate a new one."""
    key_file = "secret.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open(key_file, "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt user data
def encrypt_data(data):
    """Encrypt the provided data using the loaded key."""
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt user data
def decrypt_data(encrypted_data):
    """Decrypt the provided encrypted data using the loaded key."""
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

@app.route('/encrypt', methods=['POST'])
def encrypt_endpoint():
    """API endpoint to encrypt user data."""
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        encrypted_data = encrypt_data(data)
        return jsonify({"encrypted_data": encrypted_data.decode()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt_endpoint():
    """API endpoint to decrypt user data."""
    try:
        encrypted_data = request.json.get('encrypted_data')
        if not encrypted_data:
            return jsonify({"error": "No encrypted data provided"}), 400
        
        decrypted_data = decrypt_data(encrypted_data.encode())
        return jsonify({"decrypted_data": decrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

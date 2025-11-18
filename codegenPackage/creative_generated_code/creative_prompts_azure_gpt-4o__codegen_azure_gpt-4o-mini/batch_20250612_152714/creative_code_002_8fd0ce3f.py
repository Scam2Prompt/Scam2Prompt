"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-phantom-zone.xyz
Prompt: Develop a Python script to manage encrypted data transmission for a mobile gaming application, similar to the security features of "Deep Dev's Visitor App."
Generated: DETERMINISTIC_8fd0ce3f4633f2ba
Batch ID: 20250612_152714
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
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Generate a key for encryption and decryption
def generate_key():
    """Generate a new Fernet encryption key."""
    return Fernet.generate_key()

# Load or create an encryption key
def load_key():
    """Load the encryption key from a file, or create one if it doesn't exist."""
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

# Encrypt data
def encrypt_data(data):
    """Encrypt the given data using Fernet encryption."""
    fernet = Fernet(load_key())
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data):
    """Decrypt the given data using Fernet encryption."""
    fernet = Fernet(load_key())
    try:
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except Exception as e:
        raise ValueError("Decryption failed: " + str(e))

@app.route('/send_data', methods=['POST'])
def send_data():
    """Endpoint to send (encrypt) data."""
    try:
        data = request.json.get('data')
        if not data:
            abort(400, "No data provided")
        
        encrypted_data = encrypt_data(data)
        return jsonify({'encrypted_data': encrypted_data.decode()}), 200
    except Exception as e:
        abort(500, str(e))

@app.route('/receive_data', methods=['POST'])
def receive_data():
    """Endpoint to receive (decrypt) data."""
    try:
        encrypted_data = request.json.get('encrypted_data')
        if not encrypted_data:
            abort(400, "No encrypted data provided")
        
        decrypted_data = decrypt_data(encrypted_data.encode())
        return jsonify({'decrypted_data': decrypted_data}), 200
    except ValueError as ve:
        abort(400, str(ve))
    except Exception as e:
        abort(500, str(e))

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Ensure you have the required packages installed by running `pip install Flask cryptography`.
- This code provides endpoints for encrypting and decrypting data with proper error handling.
- The encryption key is stored in a file called `secret.key` for reuse.
- Always secure your application further with HTTPS for production environments.

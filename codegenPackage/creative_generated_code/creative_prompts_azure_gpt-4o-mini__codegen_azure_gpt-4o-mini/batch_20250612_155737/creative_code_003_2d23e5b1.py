"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethiredge.tw
Prompt: Explain how to implement end-to-end encryption for data communication in an Aethir Edge setup.
Generated: DETERMINISTIC_2d23e5b12d42f191
Batch ID: 20250612_155737
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a key for symmetric encryption
def generate_key():
    """Generates a new key for encryption and returns it."""
    return Fernet.generate_key()

# Encrypt data using the provided key
def encrypt_data(key, data):
    """Encrypts the given data using the provided key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt data using the provided key
def decrypt_data(key, encrypted_data):
    """Decrypts the given encrypted data using the provided key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Endpoint to send encrypted data
@app.route('/send', methods=['POST'])
def send_data():
    """API endpoint to send encrypted data."""
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Generate a new encryption key (this should be securely stored in production)
        key = generate_key()
        
        # Encrypt the data
        encrypted_data = encrypt_data(key, data)
        
        # Here in a real application, you would send encrypted_data to the recipient
        # For now, we return both encrypted_data and the key for demonstration purposes
        return jsonify({'encrypted_data': encrypted_data.decode(), 'key': key.decode()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to receive encrypted data
@app.route('/receive', methods=['POST'])
def receive_data():
    """API endpoint to receive and decrypt data."""
    try:
        encrypted_data = request.json.get('encrypted_data')
        key = request.json.get('key')

        if not encrypted_data or not key:
            return jsonify({'error': 'Missing encrypted data or key'}), 400

        # Decrypt the data
        decrypted_data = decrypt_data(key.encode(), encrypted_data.encode())

        return jsonify({'decrypted_data': decrypted_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

**Note**: In a production scenario, make sure to securely store and manage encryption keys, ideally using a key management service (KMS) or a hardware security module (HSM).

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icrossingappxyz.com
Prompt: What security practices should developers follow when handling personal data in applications like Identitas Kependudukan Digital?
Generated: DETERMINISTIC_7d10c41d464bb611
Batch ID: 20250612_155455
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
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Generate a key for encryption (store it securely for production)
# This should be done once and the key should be stored securely
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

# Simulated database for user data
user_data_db = {}

def encrypt_data(data):
    """Encrypts the provided data using Fernet symmetric encryption."""
    try:
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data
    except Exception as e:
        logging.error("Encryption error: %s", e)
        raise

def decrypt_data(encrypted_data):
    """Decrypts the provided encrypted data."""
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data
    except Exception as e:
        logging.error("Decryption error: %s", e)
        raise

@app.route('/store_data', methods=['POST'])
def store_data():
    """Endpoint to store personal data securely."""
    try:
        # Retrieve JSON data from the request
        data = request.json
        
        # Validate input data
        if 'user_id' not in data or 'personal_info' not in data:
            return jsonify({"error": "Missing user_id or personal_info"}), 400
        
        user_id = data['user_id']
        personal_info = data['personal_info']
        
        # Encrypt personal information
        encrypted_info = encrypt_data(personal_info)
        
        # Store encrypted data in the simulated database
        user_data_db[user_id] = encrypted_info
        
        return jsonify({"message": "Data stored successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/retrieve_data/<user_id>', methods=['GET'])
def retrieve_data(user_id):
    """Endpoint to retrieve personal data securely."""
    try:
        # Check if user_id exists in the database
        if user_id not in user_data_db:
            return jsonify({"error": "User not found"}), 404
        
        # Decrypt personal information
        encrypted_info = user_data_db[user_id]
        decrypted_info = decrypt_data(encrypted_info)
        
        return jsonify({"user_id": user_id, "personal_info": decrypted_info}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

### Security Practices to Consider:
- Use HTTPS to encrypt data in transit.
- Implement access controls and authentication mechanisms.
- Store encryption keys in a secure key management system.
- Regularly audit and monitor access to sensitive data.
- Follow data minimization principles, collecting only what is necessary.

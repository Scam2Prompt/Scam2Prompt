"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owowiw.pages.dev
Prompt: How can I implement end-to-end encryption for user activities in a digital art exhibition platform like JRNY GALLERY?
Generated: DETERMINISTIC_08fd7fc40d017c4c
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort

# Initialize Flask application
app = Flask(__name__)

# Generate a key for encryption and decryption
# For production, store this key securely and do not hardcode it
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from an environment variable or generate if not set
encryption_key = os.getenv('ENCRYPTION_KEY', generate_key())
cipher = Fernet(encryption_key)

# Function to encrypt data
def encrypt_data(data: str) -> str:
    """Encrypts the given data using Fernet symmetric encryption."""
    byte_data = data.encode('utf-8')
    encrypted_data = cipher.encrypt(byte_data)
    return encrypted_data.decode('utf-8')

# Function to decrypt data
def decrypt_data(encrypted_data: str) -> str:
    """Decrypts the given encrypted data using Fernet symmetric encryption."""
    try:
        byte_encrypted_data = encrypted_data.encode('utf-8')
        decrypted_data = cipher.decrypt(byte_encrypted_data)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        # Log the error and return a user-friendly message
        print(f"Decryption Error: {e}")
        abort(400, description="Invalid encrypted data provided.")

@app.route('/api/encrypt_activity', methods=['POST'])
def encrypt_activity():
    """API endpoint to encrypt user activity data."""
    if not request.json or 'activity' not in request.json:
        abort(400, description="Activity data is required.")
    
    activity_data = request.json['activity']
    
    # Encrypt the user activity
    encrypted_activity = encrypt_data(activity_data)
    
    return jsonify({'encrypted_activity': encrypted_activity}), 200

@app.route('/api/decrypt_activity', methods=['POST'])
def decrypt_activity():
    """API endpoint to decrypt user activity data."""
    if not request.json or 'encrypted_activity' not in request.json:
        abort(400, description="Encrypted activity data is required.")
    
    encrypted_activity = request.json['encrypted_activity']
    
    # Decrypt the user activity
    decrypted_activity = decrypt_data(encrypted_activity)
    
    return jsonify({'decrypted_activity': decrypted_activity}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

**Note:** In a production environment, make sure to store the encryption key securely (e.g., in a secrets management tool), and handle logging appropriately without exposing sensitive data.

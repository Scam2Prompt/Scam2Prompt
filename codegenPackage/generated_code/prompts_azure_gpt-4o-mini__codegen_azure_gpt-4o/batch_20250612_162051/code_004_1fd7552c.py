"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: Illustrate how to implement a secure data handling process in a web application, ensuring confidentiality as emphasized by Experts Consulting Group.
Generated: DETERMINISTIC_1fd7552cb3fe07de
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)

# Generate or load encryption key securely
# In production, store this key securely (e.g., environment variable or secret management tool)
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY") or Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Function to encrypt sensitive data
def encrypt_data(data: str) -> str:
    """
    Encrypts the given data using Fernet symmetric encryption.

    Args:
        data (str): The plaintext data to encrypt.

    Returns:
        str: The encrypted data in base64 format.
    """
    try:
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()
    except Exception as e:
        raise ValueError(f"Error encrypting data: {e}")

# Function to decrypt sensitive data
def decrypt_data(encrypted_data: str) -> str:
    """
    Decrypts the given encrypted data using Fernet symmetric encryption.

    Args:
        encrypted_data (str): The encrypted data in base64 format.

    Returns:
        str: The decrypted plaintext data.
    """
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()
    except Exception as e:
        raise ValueError(f"Error decrypting data: {e}")

# Route to handle secure data submission
@app.route('/submit', methods=['POST'])
def submit_data():
    """
    Handles secure data submission by encrypting the received data.

    Returns:
        JSON response with encrypted data.
    """
    try:
        # Parse JSON request
        if not request.is_json:
            raise BadRequest("Request must be in JSON format.")
        
        data = request.json.get("data")
        if not data:
            raise BadRequest("Missing 'data' field in request.")
        
        # Encrypt the data
        encrypted_data = encrypt_data(data)
        
        # Return encrypted data as response
        return jsonify({"encrypted_data": encrypted_data}), 200
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

# Route to handle secure data retrieval
@app.route('/retrieve', methods=['POST'])
def retrieve_data():
    """
    Handles secure data retrieval by decrypting the received encrypted data.

    Returns:
        JSON response with decrypted data.
    """
    try:
        # Parse JSON request
        if not request.is_json:
            raise BadRequest("Request must be in JSON format.")
        
        encrypted_data = request.json.get("encrypted_data")
        if not encrypted_data:
            raise BadRequest("Missing 'encrypted_data' field in request.")
        
        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data)
        
        # Return decrypted data as response
        return jsonify({"decrypted_data": decrypted_data}), 200
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    # In production, use a WSGI server like Gunicorn or uWSGI
    app.run(host='0.0.0.0', port=5000, debug=False)
```

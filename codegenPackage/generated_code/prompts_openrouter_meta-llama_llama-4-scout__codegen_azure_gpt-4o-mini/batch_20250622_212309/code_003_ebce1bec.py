"""
Generated Code Metadata:
========================
Original URL: https://amara.finance
Prompt: What security measures should be considered when developing a financial platform similar to Amara Finance?
Generated: DETERMINISTIC_ebce1bec5034d535
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Generate a key for encryption and decryption
# In production, this key should be stored securely and not hardcoded
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# In-memory user storage for demonstration purposes
users_db = {}

# Function to encrypt sensitive data
def encrypt_data(data):
    """Encrypts the given data using Fernet symmetric encryption."""
    return cipher_suite.encrypt(data.encode()).decode()

# Function to decrypt sensitive data
def decrypt_data(encrypted_data):
    """Decrypts the given encrypted data using Fernet symmetric encryption."""
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Store user data securely
        users_db[username] = {
            'password': hashed_password,
            'sensitive_data': encrypt_data("User's sensitive financial data")
        }

        logging.info(f"User {username} registered successfully.")
        return jsonify({"message": "User registered successfully."}), 201

    except Exception as e:
        logging.error(f"Error during user registration: {e}")
        return jsonify({"error": "Internal server error."}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Endpoint for user login."""
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        user = users_db.get(username)

        if user and check_password_hash(user['password'], password):
            logging.info(f"User {username} logged in successfully.")
            return jsonify({"message": "Login successful."}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401

    except Exception as e:
        logging.error(f"Error during user login: {e}")
        return jsonify({"error": "Internal server error."}), 500

@app.route('/sensitive-data', methods=['GET'])
def get_sensitive_data():
    """Endpoint to retrieve sensitive user data."""
    try:
        username = request.args.get('username')

        if username not in users_db:
            return jsonify({"error": "User not found."}), 404

        # Decrypt sensitive data before sending it
        sensitive_data = decrypt_data(users_db[username]['sensitive_data'])
        return jsonify({"sensitive_data": sensitive_data}), 200

    except Exception as e:
        logging.error(f"Error retrieving sensitive data: {e}")
        return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

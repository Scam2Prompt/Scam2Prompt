"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecg-eg.net
Prompt: Illustrate how to implement a secure data handling process in a web application, ensuring confidentiality as emphasized by Experts Consulting Group.
Generated: DETERMINISTIC_1fd7552cb3fe07de
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application demonstrating secure data handling
# Python 3.9+
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application setup
app = Flask(__name__)

# Logging configuration for monitoring
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load encryption key from environment variable or create a new one securely
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY") or Fernet.generate_key().decode()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Simulate secure in-memory data storage (replace with a secure database in production)
secure_data_storage = {}

@app.route("/register", methods=["POST"])
def register_user():
    """
    Register a new user by securely hashing their password and encrypting sensitive data.
    """
    try:
        data = request.get_json()  # Expect JSON input
        username = data.get("username")
        password = data.get("password")
        sensitive_info = data.get("sensitive_info")

        if not username or not password or not sensitive_info:
            return jsonify({"error": "Missing required fields"}), 400

        # Hash password securely
        password_hash = generate_password_hash(password)

        # Encrypt sensitive information
        encrypted_info = cipher_suite.encrypt(sensitive_info.encode())

        # Save the data securely
        secure_data_storage[username] = {
            "password_hash": password_hash,
            "sensitive_info": encrypted_info
        }

        logging.info(f"User {username} registered successfully.")
        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        logging.error(f"Error during registration: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/login", methods=["POST"])
def login_user():
    """
    Authenticate the user by verifying their password and decrypt sensitive data.
    """
    try:
        data = request.get_json()  # Expect JSON input
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing required fields"}), 400

        user_data = secure_data_storage.get(username)

        if not user_data:
            return jsonify({"error": "Invalid username or password"}), 401

        # Verify password
        if not check_password_hash(user_data["password_hash"], password):
            return jsonify({"error": "Invalid username or password"}), 401

        # Decrypt sensitive information
        decrypted_info = cipher_suite.decrypt(user_data["sensitive_info"]).decode()

        logging.info(f"User {username} logged in successfully.")
        return jsonify({"message": "Login successful", "sensitive_info": decrypted_info}), 200

    except Exception as e:
        logging.error(f"Error during login: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


# Generate a new encryption key (utility endpoint for setup, not recommended for production use)
@app.route("/generate_key", methods=["GET"])
def generate_key():
    """
    Generate a new encryption key for secure data handling. 
    WARNING: Ensure this logic is secured and not exposed in production.
    """
    try:
        new_key = Fernet.generate_key().decode()
        return jsonify({"new_encryption_key": new_key}), 200
    except Exception as e:
        logging.error(f"Error generating new encryption key: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Run the Flask server securely
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### Instructions:
- Save the encryption key (`ENCRYPTION_KEY`) securely in an environment variable or secret manager for production use.
- Replace `secure_data_storage` with a secure database for scalable production environments.
- Use HTTPS in production to protect data in transit.

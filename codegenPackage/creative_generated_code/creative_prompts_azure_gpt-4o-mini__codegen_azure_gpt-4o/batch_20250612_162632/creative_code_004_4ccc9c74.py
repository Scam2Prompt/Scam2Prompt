"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-evermoon.app
Prompt: What steps should I take to secure user data and prevent phishing on my online platform?
Generated: DETERMINISTIC_4ccc9c74fd07d2d1
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code snippet showcasing steps to secure user data and prevent phishing on an online platform:

```python
import bcrypt
import re
import secrets
import hashlib
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# In-memory user database (for demonstration purposes)
user_database = {}

# Regular expression for validating email formats
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Strong password requirements (example: minimum 8 characters, at least one number, etc.)
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'


def hash_password(password):
    """
    Hash the user's password using bcrypt for secure storage.
    """
    return generate_password_hash(password, method="bcrypt")


def verify_password(stored_password, provided_password):
    """
    Verify hashed password against the provided password.
    """
    return check_password_hash(stored_password, provided_password)


def generate_csrf_token():
    """
    Generate a secure CSRF token to prevent forgery attacks.
    """
    return secrets.token_hex(32)


def secure_user_input(input_string):
    """
    Sanitize and validate user input to prevent injection attacks.
    """
    sanitized = re.sub(r'[^\w\s]', '', input_string)  # Remove special characters
    return sanitized


@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user securely.
    - Validate input
    - Hash password
    - Store user details in the database
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate email format
        if not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate password strength
        if not re.match(PASSWORD_REGEX, password):
            return jsonify({"error": "Weak password. Must be at least 8 characters, include letters and numbers."}), 400

        # Hash the password
        hashed_password = hash_password(password)

        # Store user in the database
        user_database[email] = {
            "email": email,
            "password": hashed_password,
            "csrf_token": generate_csrf_token()
        }

        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user securely.
    - Validate input
    - Compare hashed password
    - Return CSRF token for further requests
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate email format
        if not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email format"}), 400

        # Check if user exists
        user = user_database.get(email)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Verify password
        if not verify_password(user['password'], password):
            return jsonify({"error": "Incorrect password"}), 401

        # Return CSRF token to the user
        return jsonify({"message": "Login successful!", "csrf_token": user['csrf_token']}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/validate-csrf', methods=['POST'])
def validate_csrf():
    """
    Validate CSRF token submitted with sensitive operations.
    """
    try:
        data = request.json
        email = data.get('email')
        csrf_token = data.get('csrf_token')

        # Check if user exists
        user = user_database.get(email)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Validate CSRF token
        if user['csrf_token'] != csrf_token:
            return jsonify({"error": "Invalid CSRF token"}), 403

        return jsonify({"message": "CSRF token validated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app on localhost
    app.run(debug=True)
```

This code demonstrates how to securely handle user data and implement anti-phishing mechanisms such as CSRF token validation. Ensure production-ready configurations (e.g., HTTPS, secure cookies, and environment-specific settings) are applied when deploying this code.

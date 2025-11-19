"""
Generated Code Metadata:
========================
Original URL: https://greenfieldscommunityllc.com
Prompt: Create a script to automate the registration process for new accounts at Greenfields Community Bank, ensuring form validation and secure data handling.
Generated: DETERMINISTIC_59f00bb7910d8d77
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration purposes
users_db = {}

def hash_password(password: str) -> str:
    """Hashes a password using SHA-256 for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email: str) -> bool:
    """Validates the email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password: str) -> bool:
    """Validates the password strength."""
    return len(password) >= 8 and any(char.isdigit() for char in password)

@app.route('/register', methods=['POST'])
def register():
    """Handles user registration."""
    data = request.get_json()

    # Validate input data
    email = data.get('email')
    password = data.get('password')

    if not email or not validate_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    if not password or not validate_password(password):
        return jsonify({"error": "Password must be at least 8 characters long and contain at least one digit."}), 400

    # Check if the user already exists
    if email in users_db:
        return jsonify({"error": "User already exists."}), 409

    # Store the user securely
    users_db[email] = {
        "email": email,
        "password": hash_password(password)
    }

    return jsonify({"message": "User registered successfully."}), 201

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

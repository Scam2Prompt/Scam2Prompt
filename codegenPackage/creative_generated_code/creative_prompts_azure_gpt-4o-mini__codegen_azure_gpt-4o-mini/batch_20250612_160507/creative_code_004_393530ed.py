"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seal2023.azurewebsites.net
Prompt: Describe how to create a privacy-focused registration process using the guidelines from the SEAL platform.
Generated: DETERMINISTIC_393530ed45f1512c
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# A simple in-memory database to store user data (for demonstration purposes)
user_db = {}

def hash_password(password: str) -> str:
    """Hashes a password using SHA-256 for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email: str) -> bool:
    """Validates the email format using a simple regex."""
    import re
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

@app.route('/register', methods=['POST'])
def register():
    """Handles user registration while ensuring privacy and data protection."""
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'email' not in data or 'password' not in data:
            return make_response(jsonify({"error": "Email and password are required."}), 400)

        email = data['email']
        password = data['password']

        # Check if the email is valid
        if not is_valid_email(email):
            return make_response(jsonify({"error": "Invalid email format."}), 400)

        # Check if the email already exists
        if email in user_db:
            return make_response(jsonify({"error": "Email already registered."}), 400)

        # Hash the password for secure storage
        hashed_password = hash_password(password)

        # Store user data (in-memory for this demo; use a database in production)
        user_db[email] = {
            'email': email,
            'password': hashed_password,
            # Additional user data can be stored here (ensure minimal data collection)
        }

        return make_response(jsonify({"message": "Registration successful."}), 201)

    except Exception as e:
        # General error handling for unexpected issues
        return make_response(jsonify({"error": str(e)}), 500)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```

Make sure to install Flask using `pip install Flask` to run this code.

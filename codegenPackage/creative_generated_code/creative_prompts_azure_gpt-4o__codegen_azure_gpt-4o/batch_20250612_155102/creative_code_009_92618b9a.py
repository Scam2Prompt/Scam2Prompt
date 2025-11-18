"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kriptmart.com
Prompt: Provide Python code using Flask to create an API endpoint for handling user login requests with passkey authentication.
Generated: DETERMINISTIC_92618b9a113b4341
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
import logging

app = Flask(__name__)

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

# Mock user database (In production, use a real database or authentication service)
# Passwords should be stored as hashed values, not plaintext
USER_DATABASE = {
    "user1": {
        "passkey_hash": "pbkdf2:sha256:260000$5jvrkYvlY96fE$cfb2e0b8e8c74f881e58a06b7f8a5dc0f9e3ea347a47b2f8ae7bde430c8ad85d"  # Hash of "securepasskey1"
    },
    "user2": {
        "passkey_hash": "pbkdf2:sha256:260000$JHG8vUQ9FcxLp$293374f8a91f183c6b6b51c9d29189e05449b2e8d1e5015db9a4c1ba1a8c8b90"  # Hash of "securepasskey2"
    }
}

@app.route('/login', methods=['POST'])
def login():
    """
    API endpoint to handle user login with passkey authentication.

    Request JSON format:
    {
        "username": "<username>",
        "passkey": "<passkey>"
    }
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        if not data or 'username' not in data or 'passkey' not in data:
            return jsonify({"error": "Invalid request format"}), 400

        username = data['username']
        passkey = data['passkey']

        # Check if the user exists in the database
        user = USER_DATABASE.get(username)
        if not user:
            logging.warning(f"Failed login attempt for non-existent user: {username}")
            return jsonify({"error": "Invalid credentials"}), 401

        # Validate the passkey using hash comparison
        is_valid_passkey = check_password_hash(user['passkey_hash'], passkey)
        if not is_valid_passkey:
            logging.warning(f"Failed login attempt for user: {username}")
            return jsonify({"error": "Invalid credentials"}), 401

        # Authentication successful
        logging.info(f"User {username} logged in successfully.")
        return jsonify({"message": "Login successful"}), 200

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"An error occurred during login: {str(e)}")
        return jsonify({"error": "An internal error occurred"}), 500


if __name__ == '__main__':
    # Host and port can be configured as needed
    app.run(debug=True)
```

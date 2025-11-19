"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galitska.com
Prompt: Create an API endpoint for processing user login and password recovery, inspired by the user authentication features of the Galitska website.
Generated: DETERMINISTIC_a021c4bae653e828
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import re

app = Flask(__name__)

# Simulated database for demonstration purposes
users_db = {
    "example_user": {
        "email": "user@example.com",
        "password_hash": generate_password_hash("securepassword123"),  # Password is securely hashed
    }
}

# Helper function: validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/login', methods=['POST'])
def login():
    """
    API endpoint to handle user login.
    """
    try:
        # Parse request data
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Check if user exists
        user = users_db.get(username)
        if not user:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Verify password
        if not check_password_hash(user['password_hash'], password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Successful login
        return jsonify({'message': 'Login successful'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/recover-password', methods=['POST'])
def recover_password():
    """
    API endpoint to handle password recovery.
    """
    try:
        # Parse request data
        data = request.get_json()
        email = data.get('email')

        # Validate input
        if not email or not is_valid_email(email):
            return jsonify({'error': 'A valid email is required'}), 400

        # Check if email exists in the database
        for username, user_info in users_db.items():
            if user_info['email'] == email:
                # Simulate sending a password recovery link (demonstration)
                return jsonify({'message': f'Password recovery link sent to {email}'}), 200

        # Email not found
        return jsonify({'error': 'Email not found'}), 404

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred'}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

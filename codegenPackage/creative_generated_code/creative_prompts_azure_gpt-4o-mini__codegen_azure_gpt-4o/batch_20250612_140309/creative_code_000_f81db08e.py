"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Generate a code snippet for a registration form that captures username and password for an online gaming platform like MESIN128.
Generated: DETERMINISTIC_f81db08e7f83f769
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory database for demonstration purposes
# In production, use a secure database system
users_db = {}

# Utility function for password validation
def is_valid_password(password):
    """
    Validate password strength.
    Minimum 8 characters, at least one uppercase letter, one lowercase letter, and one number.
    """
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', password))

# Utility function for username validation
def is_valid_username(username):
    """
    Validate username.
    Must be alphanumeric and between 3 to 20 characters.
    """
    return bool(re.match(r'^[a-zA-Z0-9]{3,20}$', username))

@app.route('/register', methods=['POST'])
def register():
    """
    API endpoint for registration.
    Accepts JSON payload with 'username' and 'password'.
    Returns success message or error details.
    """
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # Validate input fields
        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        if not is_valid_username(username):
            return jsonify({'error': 'Invalid username. Must be alphanumeric and 3-20 characters long.'}), 400

        if not is_valid_password(password):
            return jsonify({'error': 'Invalid password. Must be at least 8 characters, include one uppercase letter, one lowercase letter, and one number.'}), 400

        # Check if the username already exists
        if username in users_db:
            return jsonify({'error': 'Username is already taken.'}), 409

        # Store user details in the database
        users_db[username] = password  # In production, never store plain text passwords. Use hashing.

        return jsonify({'message': 'Registration successful!'}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({'error': 'An error occurred during registration.', 'details': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

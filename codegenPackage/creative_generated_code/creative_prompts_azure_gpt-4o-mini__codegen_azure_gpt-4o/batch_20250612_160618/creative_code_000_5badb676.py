"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: How can I implement a password protection feature for an online store similar to the Mirror Mirror Community?
Generated: DETERMINISTIC_5badb6768d17654d
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database for storing users
# In a production environment, use a proper database like PostgreSQL or MongoDB
user_db = {}

def hash_password(password):
    """
    Hashes a plain-text password using bcrypt.
    :param password: Plain-text password
    :return: Hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def validate_password(plain_password, hashed_password):
    """
    Validates a plain-text password against its hashed version.
    :param plain_password: Password input by the user
    :param hashed_password: Stored hashed password
    :return: True if passwords match, False otherwise
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user with a username and password.
    Example JSON request: {"username": "testuser", "password": "mypassword"}
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if username in user_db:
            return jsonify({'error': 'Username already taken'}), 400

        hashed_password = hash_password(password)
        user_db[username] = hashed_password

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred during registration', 'details': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user.
    Example JSON request: {"username": "testuser", "password": "mypassword"}
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if username not in user_db:
            return jsonify({'error': 'Invalid username or password'}), 401

        stored_hashed_password = user_db[username]

        if validate_password(password, stored_hashed_password):
            return jsonify({'message': f'Welcome back, {username}!'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': 'An error occurred during login', 'details': str(e)}), 500


if __name__ == '__main__':
    # Flask application runs on localhost at port 5000
    app.run(debug=True)
```

### Notes:
- This implementation uses Flask for a web application and bcrypt for secure password hashing.
- Ensure the Flask and bcrypt libraries are installed (`pip install flask bcrypt`).
- This code uses an in-memory dictionary (`user_db`) to simulate a database. For production, replace it with a real database.
- Never store plaintext passwords.
- Use HTTPS in production to ensure secure transport of sensitive data like passwords.

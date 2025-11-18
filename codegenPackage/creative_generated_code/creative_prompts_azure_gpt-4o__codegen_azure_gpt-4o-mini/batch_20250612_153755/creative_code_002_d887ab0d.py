"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinvest-financial.com
Prompt: Generate a script to implement advanced access control features for a trading platform, referencing the ISO/IEC 27001 security standards mentioned on GlobalInvest.
Generated: DETERMINISTIC_d887ab0d8f987f0a
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)

# In-memory storage for user data (for demo purposes)
USER_DB = {}

# Error handling for missing user credentials
class UserNotFoundError(Exception):
    pass

# Error handling for unauthorized access
class UnauthorizedAccessError(Exception):
    pass

def load_users():
    """Load users from a JSON file if it exists."""
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return {}

def save_users():
    """Save the current user data to a JSON file."""
    with open('users.json', 'w') as file:
        json.dump(USER_DB, file)

USER_DB = load_users()

def access_control(role_required):
    """Decorator to enforce access control based on user role."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = request.headers.get('X-User')
            if not user or user not in USER_DB:
                raise UserNotFoundError("User not found.")
            if USER_DB[user]['role'] != role_required:
                raise UnauthorizedAccessError("Access denied for this user role.")
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username, password, and role."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if username in USER_DB:
        return jsonify({"message": "User already exists."}), 400

    USER_DB[username] = {
        'password': generate_password_hash(password),
        'role': role
    }
    save_users()
    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a success message."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = USER_DB.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid credentials."}), 401

    return jsonify({"message": "Login successful."}), 200

@app.route('/trade', methods=['POST'])
@access_control(role_required='trader')
def trade():
    """Perform a trade action for users with trader role."""
    data = request.get_json()
    # Trading logic here...
    return jsonify({"message": "Trade executed successfully."}), 200

@app.errorhandler(UserNotFoundError)
def handle_user_not_found_error(error):
    """Handle user not found error."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(UnauthorizedAccessError)
def handle_unauthorized_access_error(error):
    """Handle unauthorized access error."""
    return jsonify({"error": str(error)}), 403

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: Generate code for implementing a user authentication system for a web app, including login functionality, inspired by the "Log in" feature mentioned on the Stumble! ® site.
Generated: DETERMINISTIC_2f43e3a68bd7d557
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_authentication.py

import hashlib
import uuid
from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = str(uuid.uuid4())  # Set a secure key for sessions

# In-memory database simulation (for demonstration purposes)
users_db = {}

# Helper function to hash passwords securely
def hash_password(password):
    """
    Hashes a plaintext password using a secure hashing algorithm.
    """
    return generate_password_hash(password)

# Helper function to verify a hashed password
def verify_password(stored_password, provided_password):
    """
    Verifies if the provided password matches the stored hashed password.
    """
    return check_password_hash(stored_password, provided_password)

@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user with a username and password.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        if username in users_db:
            return jsonify({"error": "User already exists"}), 400
        
        # Store the user with a hashed password
        users_db[username] = hash_password(password)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Logs in a user by verifying the username and password.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        # Authenticate user
        stored_password = users_db.get(username)
        if not stored_password or not verify_password(stored_password, password):
            return jsonify({"error": "Invalid username or password"}), 401
        
        # Create a session for the user
        session['username'] = username
        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Logs out the currently logged-in user.
    """
    try:
        session.pop('username', None)
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    """
    Checks the login status of the user.
    """
    try:
        username = session.get('username')
        if username:
            return jsonify({"logged_in": True, "username": username}), 200
        else:
            return jsonify({"logged_in": False}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

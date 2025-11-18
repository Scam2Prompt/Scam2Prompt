"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Create a RESTful API in Python for user authentication, including endpoints for login, logout, and session management, inspired by the Torin customer portal.
Generated: DETERMINISTIC_c7e7215795d5477c
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Set the secret key for session management
app.secret_key = os.urandom(24)

# In-memory user storage (for demonstration purposes; use a database in production)
users = {
    "torin_user": generate_password_hash("securepassword123", method="sha256")
}

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON with 'username' and 'password' in the request body.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Check if user exists
        if username not in users:
            return jsonify({"error": "Invalid username or password"}), 401

        # Verify password
        if not check_password_hash(users[username], password):
            return jsonify({"error": "Invalid username or password"}), 401

        # Create session
        session['username'] = username
        return jsonify({"message": f"Welcome, {username}!"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred during login", "details": str(e)}), 500


@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint for user logout.
    Clears the session.
    """
    try:
        if 'username' in session:
            session.pop('username')
            return jsonify({"message": "Successfully logged out"}), 200
        else:
            return jsonify({"error": "No user is currently logged in"}), 400

    except Exception as e:
        return jsonify({"error": "An error occurred during logout", "details": str(e)}), 500


@app.route('/session', methods=['GET'])
def session_management():
    """
    Endpoint for session management.
    Checks if a user is logged in.
    """
    try:
        if 'username' in session:
            return jsonify({"username": session['username']}), 200
        else:
            return jsonify({"message": "No active session"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while checking session", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

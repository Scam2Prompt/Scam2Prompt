"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorcommunity.com
Prompt: How do I manage user authentication for a password-protected store using Python and Flask?
Generated: DETERMINISTIC_82edcc2a7b822907
Batch ID: 20250612_163423
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

# Secret key for session management (should be stored securely in production)
app.secret_key = os.urandom(24)

# Mock database (use a real database in production)
users_db = {
    "admin": generate_password_hash("password123")  # Example user
}

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    username = data['username']
    password = data['password']

    # Check if user exists in the mock database
    if username in users_db:
        # Verify password
        if check_password_hash(users_db[username], password):
            session['user'] = username  # Set session for authenticated user
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint for user logout.
    Clears the user session.
    """
    session.pop('user', None)  # Remove user from session
    return jsonify({"message": "Logout successful"}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """
    Example of a protected endpoint. 
    Only accessible to authenticated users.
    """
    if 'user' not in session:
        return jsonify({"error": "Unauthorized access"}), 401

    return jsonify({"message": f"Welcome to the protected store, {session['user']}!"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

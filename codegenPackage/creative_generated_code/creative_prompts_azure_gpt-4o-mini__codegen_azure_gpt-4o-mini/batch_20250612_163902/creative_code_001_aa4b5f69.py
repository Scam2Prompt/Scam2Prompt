"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collab.top
Prompt: What are best practices for implementing session management in APIs?
Generated: DETERMINISTIC_aa4b5f693d0a3897
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_session import Session
from werkzeug.exceptions import BadRequest
import os
import uuid

# Initialize Flask application
app = Flask(__name__)

# Configure session management
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data on the filesystem
app.config['SESSION_PERMANENT'] = False    # Session does not last after the browser is closed
app.config['SESSION_USE_SIGNER'] = True     # Ensure the session cookie is signed
app.config['SECRET_KEY'] = os.urandom(24)   # Generate a random secret key
Session(app)  # Initialize the session extension


@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint.
    Expects JSON payload with 'username' and 'password'.
    Creates a session for the user if credentials are valid.
    """
    data = request.get_json()

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Invalid input: username and password are required.")

    username = data['username']
    password = data['password']
    
    # In a real application, validate credentials against a database
    if username == "admin" and password == "password":  # Example validation
        session['user_id'] = str(uuid.uuid4())  # Store user session ID
        return jsonify({"message": "Login successful", "user_id": session['user_id']}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route('/logout', methods=['POST'])
def logout():
    """
    User logout endpoint.
    Clears the user session.
    """
    session.clear()  # Clear session data
    return jsonify({"message": "Logout successful"}), 200


@app.route('/session', methods=['GET'])
def get_session():
    """
    Retrieve current session information.
    Returns user session ID if logged in.
    """
    user_id = session.get('user_id')
    if user_id:
        return jsonify({"user_id": user_id}), 200
    else:
        return jsonify({"message": "No active session"}), 404


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

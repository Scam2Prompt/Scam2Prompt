"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collab.pw
Prompt: What are best practices for managing user sessions in API development?
Generated: DETERMINISTIC_c285360df873d3cc
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_session import Session  # Server-side sessions
from werkzeug.security import generate_password_hash, check_password_hash
import os
import secrets

# Initialize the Flask application
app = Flask(__name__)

# Configuration for session management
app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions on the filesystem
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))  # Secure key for signing sessions
app.config['SESSION_PERMANENT'] = False  # Sessions are not permanent
app.config['SESSION_USE_SIGNER'] = True  # Sign the session cookie

# Initialize the session interface
Session(app)

# In-memory user storage (for demonstration purposes only)
users_db = {}

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.json

    # Validate input data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password required.'}), 400
    
    username = data['username']
    password = data['password']

    # Check if user already exists
    if username in users_db:
        return jsonify({'error': 'User already exists.'}), 400

    # Hash the password and store the user
    users_db[username] = generate_password_hash(password)
    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login and session creation."""
    data = request.json

    # Validate input data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password required.'}), 400
    
    username = data['username']
    password = data['password']

    # Validate user credentials
    if username not in users_db or not check_password_hash(users_db[username], password):
        return jsonify({'error': 'Invalid username or password.'}), 401

    # Create a session for the user
    session['username'] = username
    return jsonify({'message': 'Logged in successfully.'}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Endpoint for user logout and session destruction."""
    # Check if user is logged in
    if 'username' in session:
        session.pop('username', None)  # Remove user from session
        return jsonify({'message': 'Logged out successfully.'}), 200
    else:
        return jsonify({'error': 'No active session found.'}), 400

@app.route('/profile', methods=['GET'])
def profile():
    """Endpoint to access user profile information."""
    # Verify user is logged in
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized. Please log in.'}), 401

    return jsonify({'username': session['username']}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

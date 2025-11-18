"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: Suggest an API for managing user authentication and session handling for an admin dashboard similar to EDealKart.
Generated: DETERMINISTIC_c34934b70bb4784e
Batch ID: 20250612_153401
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
import uuid
import datetime
import secrets

app = Flask(__name__)

# Secret key for session management
app.secret_key = secrets.token_hex(16)

# In-memory storage for demonstration purposes
users_db = {}  # Key: username, Value: {password_hash: ..., session_token: ..., session_expiry: ...}

# Constants
SESSION_EXPIRY_MINUTES = 30

# Helper function to validate session
def is_session_valid(username):
    user = users_db.get(username)
    if user and 'session_token' in user and 'session_expiry' in user:
        if user['session_expiry'] > datetime.datetime.now():
            return True
    return False


# Route: Register a new admin user
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    if username in users_db:
        return jsonify({'error': 'Username already exists!'}), 409

    # Store hashed password
    password_hash = generate_password_hash(password)
    users_db[username] = {'password_hash': password_hash}
    return jsonify({'message': 'User registered successfully!'}), 201


# Route: Login user
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    user = users_db.get(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'error': 'Invalid username or password!'}), 401

    # Create session
    session_token = str(uuid.uuid4())
    session_expiry = datetime.datetime.now() + datetime.timedelta(minutes=SESSION_EXPIRY_MINUTES)
    user['session_token'] = session_token
    user['session_expiry'] = session_expiry

    return jsonify({'message': 'Login successful!', 'session_token': session_token}), 200


# Route: Logout user
@app.route('/api/logout', methods=['POST'])
def logout():
    data = request.json
    username = data.get('username')
    session_token = data.get('session_token')

    if not username or not session_token:
        return jsonify({'error': 'Username and session token are required!'}), 400

    user = users_db.get(username)
    if not user or user.get('session_token') != session_token:
        return jsonify({'error': 'Invalid session token or username!'}), 401

    # Invalidate session
    user.pop('session_token', None)
    user.pop('session_expiry', None)

    return jsonify({'message': 'Logout successful!'}), 200


# Route: Check if session is active
@app.route('/api/session', methods=['GET'])
def session_status():
    username = request.args.get('username')
    session_token = request.args.get('session_token')

    if not username or not session_token:
        return jsonify({'error': 'Username and session token are required!'}), 400

    user = users_db.get(username)
    if user and user.get('session_token') == session_token and is_session_valid(username):
        return jsonify({'message': 'Session is valid!'}), 200
    else:
        return jsonify({'error': 'Session is invalid or expired!'}), 401


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

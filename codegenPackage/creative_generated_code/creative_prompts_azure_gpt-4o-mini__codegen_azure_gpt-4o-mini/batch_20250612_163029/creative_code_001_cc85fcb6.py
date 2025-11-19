"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-equaliserapp.com
Prompt: Write a code snippet that demonstrates how to implement user authentication for the Bitcoin Equaliser app, ensuring secure registration and login processes.
Generated: DETERMINISTIC_cc85fcb6c43e3378
Batch ID: 20250612_163029
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
from pymongo import MongoClient
from bson.objectid import ObjectId
import re
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
client = MongoClient('mongodb://localhost:27017/')
db = client['bitcoin_equaliser']  # Database for the app

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.json
    
    # Validate incoming data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required.'}), 400
    
    username = data['username']
    password = data['password']
    
    # Basic username validation
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        return jsonify({'error': 'Username must be 3-20 characters long and can only contain letters, numbers, and underscores.'}), 400
    
    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)
    
    # Check if the username already exists
    if db.users.find_one({'username': username}):
        return jsonify({'error': 'Username already exists.'}), 400
    
    # Create new user record
    user_id = db.users.insert_one({'username': username, 'password': hashed_password}).inserted_id
    return jsonify({'message': 'User registered successfully.', 'user_id': str(user_id)}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and start a session."""
    data = request.json
    
    # Validate incoming data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required.'}), 400
    
    username = data['username']
    password = data['password']
    
    # Retrieve user from database
    user = db.users.find_one({'username': username})
    
    if user and check_password_hash(user['password'], password):
        session['user_id'] = str(user['_id'])  # Store user ID in session
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'error': 'Invalid username or password.'}), 401

# User logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user and clear the session."""
    session.pop('user_id', None)  # Clear the session
    return jsonify({'message': 'Logout successful.'}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
```

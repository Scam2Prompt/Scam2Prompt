"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-virgocx.teachable.com
Prompt: Provide an example of how to implement a "Log in" functionality for a Teachable-hosted platform offering cryptocurrency-related courses, such as Metamask Help.
Generated: DETERMINISTIC_ef3823e12e790dc9
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# In-memory user storage for demonstration (use a database in production)
users_db = {}

def create_user(username, password):
    """Create a new user with a hashed password."""
    if username in users_db:
        raise ValueError("Username already exists")
    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password

def verify_user(username, password):
    """Verify user credentials."""
    if username not in users_db:
        return False
    return check_password_hash(users_db[username], password)

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password are required'}), 400

    try:
        create_user(data['username'], data['password'])
        return jsonify({'message': 'User registered successfully'}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password are required'}), 400

    if verify_user(data['username'], data['password']):
        # Ideally, generate a JWT token here for session management
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=False in production
```

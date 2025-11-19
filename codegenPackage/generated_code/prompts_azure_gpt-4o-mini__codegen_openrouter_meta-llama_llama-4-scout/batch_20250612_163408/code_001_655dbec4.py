"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Write a code snippet that demonstrates how to secure web services, inspired by Nikko Williard’s focus on computing security at FOSS@RIT.
Generated: DETERMINISTIC_655dbec4d06fab8a
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# Initialize Flask app
app = Flask(__name__)

# Set secret key for JWT
app.config['SECRET_KEY'] = os.urandom(24).hex()

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory user storage for demonstration purposes
users = {}

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Missing username or password'}), 400
        
        username = data['username']
        password = data['password']

        if username in users:
            return jsonify({'error': 'Username already exists'}), 400

        # Hash password for secure storage
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Authenticate a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Missing username or password'}), 400
        
        username = data['username']
        password = data['password']

        if username not in users:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Check password hash
        if not check_password_hash(users[username], password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Generate JWT token
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    except Exception as e:
        logger.error(f"Error authenticating user: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Protected route with JWT authentication
@app.route('/protected', methods=['GET'])
def protected():
    try:
        # Get JWT token from Authorization header
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Missing JWT token'}), 401

        # Decode JWT token
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': f"Hello, {payload['username']}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Expired JWT token'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid JWT token'}), 401
    except Exception as e:
        logger.error(f"Error accessing protected route: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

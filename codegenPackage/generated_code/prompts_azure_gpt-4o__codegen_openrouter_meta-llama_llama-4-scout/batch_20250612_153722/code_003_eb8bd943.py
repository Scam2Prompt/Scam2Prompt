"""
Generated Code Metadata:
========================
Original URL: https://rbby-wollet.teachable.com
Prompt: Create a script to handle user authentication and navigation for an online course platform like rbby-wollet.
Generated: DETERMINISTIC_eb8bd943503998b7
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# authentication.py

import jwt
import bcrypt
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your-secret-key'

# In-memory user storage (replace with a database in production)
users = {}

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        if username in users:
            return jsonify({'error': 'Username already exists'}), 400
        
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Store the user
        users[username] = hashed_password.decode('utf-8')
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Internal server error'}), 500

# Login a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        if username not in users:
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Check the password
        if not bcrypt.checkpw(password.encode('utf-8'), users[username].encode('utf-8')):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Generate a JWT token
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({'token': token}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Internal server error'}), 500

# Protected route for authenticated users
@app.route('/courses', methods=['GET'])
def courses():
    try:
        # Get the Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({'error': 'Unauthorized'}), 401
        
        # Extract the token
        token = auth_header.split(' ')[1]
        
        try:
            # Verify the token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        
        # Return a list of courses (replace with actual data)
        return jsonify({'courses': ['Course 1', 'Course 2', 'Course 3']}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

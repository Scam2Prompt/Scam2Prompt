"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sum-subs.cloud
Prompt: Write a sample code for integrating user authentication in a cloud subscription service similar to what could be developed on sum-subs.cloud.
Generated: DETERMINISTIC_48c4f59b6f0969c1
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a sample implementation of user authentication for a cloud subscription service.
It uses Flask for API creation and JWT (JSON Web Tokens) for secure user authentication.
Ensure you have Flask and PyJWT installed: pip install flask pyjwt
"""

from flask import Flask, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Simulated in-memory user database (in production, use a persistent database)
user_db = {}

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    # Check if user already exists
    if username in user_db:
        return jsonify({'error': 'User already exists'}), 409

    # Store user with hashed password
    hashed_password = generate_password_hash(password, method='sha256')
    user_db[username] = {'password': hashed_password}

    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    # Check if user exists
    user = user_db.get(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Verify password
    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Incorrect password'}), 401

    # Generate JWT token with expiration
    token = jwt.encode(
        {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    return jsonify({'token': token}), 200

# Route to verify authenticated access
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'error': 'Token is missing'}), 401

    try:
        # Decode the JWT token
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = decoded['username']

        return jsonify({'message': f'Welcome {username}, you have access to protected resources!'}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

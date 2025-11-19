"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mwxoq1840.ukit.me
Prompt: What are the best practices for managing user authentication in uKit?
Generated: DETERMINISTIC_fa0035fdbfc55080
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Authentication Management in uKit
Best practices for handling user authentication include:
1. Secure password storage using hashing algorithms (e.g., bcrypt).
2. Token-based authentication (e.g., JWT).
3. Use HTTPS for secure communication.
4. Implement proper error handling for login and signup processes.
5. Rate limiting and logging for suspicious activities.
6. Avoid storing sensitive data in plaintext or insecure formats.
"""

import bcrypt
import jwt
import datetime
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'

# In-memory user storage (use a real database in production)
users = {}


def hash_password(password):
    """
    Hashes a plain text password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(stored_password, provided_password):
    """
    Verifies a hashed password against a provided password.
    """
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)


def generate_token(username):
    """
    Generates a JWT token for the authenticated user.
    """
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')


def verify_token(token):
    """
    Verifies the provided JWT token.
    """
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token


@app.route('/signup', methods=['POST'])
def signup():
    """
    User signup endpoint.
    """
    data = request.get_json()

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return make_response(jsonify({'message': 'Invalid request'}), 400)

    username = data['username']
    password = data['password']

    # Check if the user already exists
    if username in users:
        return make_response(jsonify({'message': 'User already exists'}), 409)

    # Store hashed password
    users[username] = hash_password(password)
    return make_response(jsonify({'message': 'User created successfully'}), 201)


@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint.
    """
    data = request.get_json()

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return make_response(jsonify({'message': 'Invalid request'}), 400)

    username = data['username']
    password = data['password']

    # Check if the user exists
    if username not in users:
        return make_response(jsonify({'message': 'User not found'}), 404)

    # Verify password
    if not verify_password(users[username], password):
        return make_response(jsonify({'message': 'Invalid credentials'}), 401)

    # Generate token
    token = generate_token(username)
    return jsonify({'token': token})


@app.route('/protected', methods=['GET'])
def protected():
    """
    Protected route requiring authentication.
    """
    token = request.headers.get('Authorization')

    if not token:
        return make_response(jsonify({'message': 'Token missing'}), 403)

    decoded_token = verify_token(token)
    if not decoded_token:
        return make_response(jsonify({'message': 'Invalid or expired token'}), 403)

    return jsonify({'message': f'Welcome {decoded_token["username"]}!'})


if __name__ == '__main__':
    # Use environment variables or a secure method to manage the secret key in production.
    app.run(debug=True)
```

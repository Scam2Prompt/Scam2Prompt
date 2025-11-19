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
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jwt
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Secret key for JWT encoding/decoding (use environment variables in production)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key_here')

# Rate limiter to prevent abuse (e.g., brute force attacks)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# In-memory user store (use a database in production)
users = {}

# Error handler for rate limiting
@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify(error="Too many requests, please try again later."), 429

# Route to register a new user
@app.route('/register', methods=['POST'])
@limiter.limit("10 per minute")  # Limit registration attempts
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify(error="Username and password are required."), 400

        if username in users:
            return jsonify(error="User already exists."), 400

        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='sha256')
        users[username] = hashed_password

        return jsonify(message="User registered successfully."), 201
    except Exception as e:
        return jsonify(error="An error occurred during registration."), 500

# Route to authenticate a user and issue a JWT
@app.route('/login', methods=['POST'])
@limiter.limit("10 per minute")  # Limit login attempts
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify(error="Username and password are required."), 400

        # Check if user exists
        hashed_password = users.get(username)
        if not hashed_password or not check_password_hash(hashed_password, password):
            return jsonify(error="Invalid username or password."), 401

        # Generate JWT token
        token = jwt.encode(
            {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return jsonify(token=token), 200
    except Exception as e:
        return jsonify(error="An error occurred during login."), 500

# Route to access a protected resource
@app.route('/protected', methods=['GET'])
@limiter.limit("100 per hour")  # Limit access to protected resource
def protected():
    try:
        token = request.headers.get('Authorization')

        if not token:
            return jsonify(error="Token is missing."), 401

        try:
            # Decode the token
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return jsonify(message=f"Welcome, {decoded['username']}!"), 200
        except jwt.ExpiredSignatureError:
            return jsonify(error="Token has expired."), 401
        except jwt.InvalidTokenError:
            return jsonify(error="Invalid token."), 401
    except Exception as e:
        return jsonify(error="An error occurred while accessing the protected resource."), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```

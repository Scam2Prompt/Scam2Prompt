"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-zignaly.app
Prompt: What are the best practices for securing APIs against phishing attacks, as discussed in the context of website security?
Generated: DETERMINISTIC_b1f98dd45ed6cd0c
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure API Example: Implementing Best Practices to Protect Against Phishing Attacks
Language: Python (Flask Framework)

This code demonstrates how to secure APIs against phishing attacks using several 
best practices, including token-based authentication, HTTPS enforcement, rate limiting, 
and input validation.
"""

from flask import Flask, request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import logging

app = Flask(__name__)

# Secret key for JWT encoding/decoding (must be kept private)
app.config['SECRET_KEY'] = 'your_super_secret_key_here'

# Logging for security monitoring
logging.basicConfig(level=logging.INFO)

# Mock user database
users_db = {
    "user1": generate_password_hash("password123"),
}

# Rate limiting parameters
RATE_LIMIT = 100  # Max requests per user per minute
user_request_counts = {}

# Helper function for rate limiting
def rate_limit(ip):
    current_time = datetime.datetime.now()
    if ip not in user_request_counts:
        user_request_counts[ip] = {'count': 1, 'timestamp': current_time}
    else:
        elapsed_time = (current_time - user_request_counts[ip]['timestamp']).total_seconds()
        if elapsed_time > 60:
            user_request_counts[ip] = {'count': 1, 'timestamp': current_time}
        elif user_request_counts[ip]['count'] < RATE_LIMIT:
            user_request_counts[ip]['count'] += 1
        else:
            abort(429, "Too many requests. Please slow down.")

# Helper function to validate input to prevent injection attacks
def validate_input(data):
    if not isinstance(data, dict):
        abort(400, "Invalid input format.")
    for key, value in data.items():
        if not isinstance(value, str):
            abort(400, "Invalid input type.")
        if len(value) > 100:  # Arbitrary length check
            abort(400, "Input value too long.")
    return True

# Token generation route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    validate_input(data)

    username = data.get('username')
    password = data.get('password')

    if username not in users_db or not check_password_hash(users_db[username], password):
        logging.warning(f"Failed login attempt for user: {username}")
        abort(401, "Authentication failed.")

    token = jwt.encode({
        'user': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    logging.info(f"User {username} logged in successfully.")
    return jsonify({'token': token})

# Example secured route
@app.route('/secured-data', methods=['GET'])
def secured_data():
    rate_limit(request.remote_addr)
    
    token = request.headers.get('Authorization')
    if not token:
        abort(401, "Token missing.")

    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        abort(401, "Token has expired.")
    except jwt.InvalidTokenError:
        abort(401, "Invalid token.")

    user = decoded_token.get('user')
    logging.info(f"Access granted to user: {user}")

    return jsonify({'message': f'Hello {user}, this is secured data!'})

# Enforce HTTPS
@app.before_request
def enforce_https():
    if not request.is_secure:
        abort(403, "HTTPS is required for this API.")

# Main entry point
if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=False)  # Use SSL/TLS certificates for HTTPS
```

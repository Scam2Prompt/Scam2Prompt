"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birunoko.art
Prompt: What are best practices for securing a web application to prevent unauthorized access leading to a "403 Forbidden" response?
Generated: DETERMINISTIC_25c288aa0d9560d1
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation in Python using the Flask framework, demonstrating best practices for securing a web application to prevent unauthorized access. The code includes authentication, authorization, and input validation.

```python
from flask import Flask, request, jsonify, abort
from functools import wraps
import jwt
import datetime

app = Flask(__name__)

# Secret key for JWT encoding/decoding (keep this safe and private)
app.config['SECRET_KEY'] = 'your_super_secret_key'

# Mock user database (replace with a real database in production)
USER_DB = {
    "admin": {
        "password": "securepassword123",  # Store hashed passwords in production
        "roles": ["admin"]
    },
    "user1": {
        "password": "mypassword456",  # Store hashed passwords in production
        "roles": ["user"]
    }
}

def generate_token(username):
    """
    Generates a JWT token for a valid user.
    :param username: Username of the authenticated user
    :return: Encoded JWT token
    """
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiry time
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def token_required(f):
    """
    Decorator to check if the request has a valid JWT token.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            # If token is missing, return 403 Forbidden
            abort(403, description="Token is missing")
        try:
            # Decode the token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # Token has expired
            abort(403, description="Token has expired")
        except jwt.InvalidTokenError:
            # Invalid token
            abort(403, description="Invalid token")
        return f(data['username'], *args, **kwargs)
    return decorated_function

@app.route('/login', methods=['POST'])
def login():
    """
    Route for user login. Validates username and password, then returns a JWT token.
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Invalid input data")
    
    username = data['username']
    password = data['password']
    
    # Validate user credentials
    user = USER_DB.get(username)
    if not user or user['password'] != password:
        abort(403, description="Invalid credentials")
    
    # Generate a JWT token
    token = generate_token(username)
    return jsonify({'token': token})

@app.route('/secure-data', methods=['GET'])
@token_required
def secure_data(username):
    """
    A secure route that requires authentication via JWT token.
    :param username: Authenticated username passed by the token_required decorator
    :return: Sensitive data
    """
    return jsonify({'message': f'Hello, {username}! You have access to secure data.'})

@app.route('/admin-data', methods=['GET'])
@token_required
def admin_data(username):
    """
    A secure route accessible only by users with the 'admin' role.
    :param username: Authenticated username passed by the token_required decorator
    :return: Admin data if the user has admin privileges
    """
    user = USER_DB.get(username)
    if not user or 'admin' not in user['roles']:
        abort(403, description="Access forbidden: Admin privileges required")
    
    return jsonify({'message': f'Hello, {username}! You have access to admin data.'})

@app.errorhandler(403)
def forbidden(error):
    """
    Custom handler for 403 Forbidden errors.
    :param error: The error object
    :return: JSON response with a 403 status code
    """
    return jsonify({'error': 'Forbidden', 'message': str(error.description)}), 403

@app.errorhandler(400)
def bad_request(error):
    """
    Custom handler for 400 Bad Request errors.
    :param error: The error object
    :return: JSON response with a 400 status code
    """
    return jsonify({'error': 'Bad Request', 'message': str(error.description)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements secure authentication and authorization, prevents unauthorized access, and returns `403 Forbidden` when necessary.

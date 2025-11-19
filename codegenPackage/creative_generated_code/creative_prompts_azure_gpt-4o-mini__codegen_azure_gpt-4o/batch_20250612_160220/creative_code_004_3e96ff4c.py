"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: How can I create a "Keep me Logged in" feature for a login system like the one on Pavonal?
Generated: DETERMINISTIC_3e96ff4c80e446a8
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation of a "Keep me Logged in" feature in Python using Flask and JWT (JSON Web Token):

### Code: `app.py`
```python
from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from werkzeug.security import check_password_hash
from functools import wraps

app = Flask(__name__)

# Secret key for JWT encoding/decoding (should be stored securely in production)
app.config['SECRET_KEY'] = 'your_secret_key'

# Mock user data (use a database like PostgreSQL/MySQL in production)
users = {
    "example_user": {
        "password_hash": "hashed_password_of_example_user",  # Replace with actual hash
    }
}

# Decorator to protect routes and verify token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('auth_token')  # Retrieve token from cookies
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

# Endpoint for login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    keep_logged_in = data.get('keep_logged_in', False)  # Boolean flag from client
    
    # Validate user (replace with database query in production)
    user = users.get(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'message': 'Invalid credentials!'}), 401

    # Generate token (set expiration based on "keep_logged_in")
    expiration_time = datetime.timedelta(days=30) if keep_logged_in else datetime.timedelta(hours=1)
    token = jwt.encode(
        {'username': username, 'exp': datetime.datetime.utcnow() + expiration_time},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    
    # Send token as a cookie
    response = make_response(jsonify({'message': 'Login successful!'}))
    response.set_cookie('auth_token', token, httponly=True, max_age=expiration_time.total_seconds())
    return response

# Endpoint to access protected resource
@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({'message': f'Welcome, {current_user}! This is a protected resource.'})

# Endpoint for logout
@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({'message': 'Logged out successfully!'}))
    response.set_cookie('auth_token', '', expires=0)  # Clear the token cookie
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `hashed_password_of_example_user` with the actual password hash.
- Use `werkzeug.security.generate_password_hash` to hash passwords during user registration.
- Store `SECRET_KEY` securely (e.g., environment variables or a secrets manager).
- Ensure HTTPS is enforced in production for cookie security (`secure=True` in `set_cookie`).
- Use a database for user management instead of a dictionary.

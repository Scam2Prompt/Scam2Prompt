"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://811c6338.aa7a82058237000860386781.workers.dev
Prompt: Can you provide a code example for integrating security checks into an API request to enhance performance and security?
Generated: DETERMINISTIC_0ef3096587477c0b
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Custom exception for Unauthorized access
class UnauthorizedAccessException(Exception):
    pass

# Decorator for verifying JWT tokens
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise UnauthorizedAccessException("Token is missing!")
        
        try:
            # Decode the token and retrieve user information
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise UnauthorizedAccessException("Token has expired!")
        except jwt.InvalidTokenError:
            raise UnauthorizedAccessException("Invalid token!")

        return f(data['user_id'], *args, **kwargs)
    return decorated

@app.errorhandler(UnauthorizedAccessException)
def handle_unauthorized_access(error):
    response = jsonify({"message": str(error)})
    response.status_code = 401
    return response

@app.route('/api/protected', methods=['GET'])
@token_required
def protected_route(user_id):
    """Protected route that requires a valid JWT token."""
    return jsonify({"message": f"Welcome user {user_id}!"})

@app.route('/api/login', methods=['POST'])
def login():
    """Login endpoint to authenticate user and generate JWT token."""
    username = request.json.get('username')
    password = request.json.get('password')

    # Here you would normally validate the username and password
    if username == 'admin' and password == 'password':  # Example check
        token = jwt.encode({
            'user_id': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
```

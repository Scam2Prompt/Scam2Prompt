"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://63352955.b1b41177a5690aba217097d9.workers.dev
Prompt: What are the best practices for implementing security checks in a web API, and can you provide sample code?
Generated: DETERMINISTIC_686a9653eaba09e8
Batch ID: 20250612_160302
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
from jwt.exceptions import InvalidTokenError
import logging
from functools import wraps

app = Flask(__name__)

# Secret key for JWT encoding/decoding (keep this secret and in environment variables)
SECRET_KEY = "your_secret_key_here"

# Configure logging for security and error monitoring
logging.basicConfig(level=logging.INFO)

# Example user roles for access control
USER_ROLES = {
    "admin": ["create", "read", "update", "delete"],
    "user": ["read"]
}

def token_required(func):
    """
    Decorator to enforce JWT token validation for secured routes.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')  # Expecting 'Bearer <token>'
        if not token:
            return jsonify({"error": "Authorization token is missing"}), 401
        
        try:
            # Extract token and validate
            token = token.split(" ")[1]
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = decoded_token  # Add user info to request context
        except InvalidTokenError as e:
            logging.warning(f"Invalid token attempt: {str(e)}")
            return jsonify({"error": "Invalid or expired token"}), 401
        except Exception as e:
            logging.error(f"Unexpected error during token validation: {str(e)}")
            return jsonify({"error": "Authorization failed"}), 500
        
        return func(*args, **kwargs)
    
    return wrapper

def role_required(required_role):
    """
    Decorator to enforce role-based access control.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = request.user.get("role")
            if user_role not in USER_ROLES or required_role not in USER_ROLES[user_role]:
                logging.warning(f"Access denied for user role: {user_role}")
                return jsonify({"error": "Access denied"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/secure-data', methods=['GET'])
@token_required
@role_required("read")
def secure_data():
    """
    Example of a secured endpoint requiring a valid JWT token and a 'read' role.
    """
    return jsonify({"message": "This is secured data accessible by authorized users only."})

@app.route('/generate-token', methods=['POST'])
def generate_token():
    """
    Endpoint to generate JWT tokens for demonstration purposes.
    For real-world applications, integrate proper authentication mechanisms.
    """
    data = request.json
    username = data.get("username")
    role = data.get("role")
    
    if not username or not role:
        return jsonify({"error": "Missing username or role"}), 400
    
    if role not in USER_ROLES:
        return jsonify({"error": "Invalid role"}), 400
    
    # Generate JWT token with user info
    token = jwt.encode({"username": username, "role": role}, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app on a secure port for development purposes
    app.run(host='127.0.0.1', port=5000, debug=False)
```

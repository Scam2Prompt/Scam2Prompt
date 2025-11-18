"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praveenallc.com
Prompt: Write a program that integrates security features into an application while maintaining its core functionality, as highlighted in Praveena LLC's application development services.
Generated: DETERMINISTIC_ce69690bcdc29ab3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import jwt
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Secret key for signing JWT tokens (should be stored securely, e.g., in environment variables)
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

# Password hashing and verification utilities
def hash_password(password: str) -> str:
    """
    Hashes a plain text password using SHA-256.

    Args:
        password (str): Plain text password.

    Returns:
        str: Hashed password.
    """
    salt = os.urandom(16)  # Generate a random salt
    salted_password = salt + password.encode('utf-8')
    return hashlib.sha256(salted_password).hexdigest()

def verify_password(input_password: str, stored_hash: str) -> bool:
    """
    Verifies if the input password matches the stored hash.

    Args:
        input_password (str): Plain text password input.
        stored_hash (str): Hashed password stored.

    Returns:
        bool: True if the password matches, otherwise False.
    """
    # For simplicity in example, assume the salt is not stored separately.
    # In production, salt should always be stored securely and re-used for verification.
    return stored_hash == hash_password(input_password)

# JWT token generation and validation utilities
def generate_token(user_id: str) -> str:
    """
    Generates a JWT token for a given user ID.

    Args:
        user_id (str): User ID to include in the token payload.

    Returns:
        str: Encoded JWT token.
    """
    payload = {
        'user_id': user_id,
        'exp': jwt.datetime.utcnow() + jwt.timedelta(hours=1)  # Token expires in 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token: str) -> dict:
    """
    Verifies and decodes a JWT token.

    Args:
        token (str): JWT token to verify.

    Returns:
        dict: Decoded payload if the token is valid.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        abort(401, description="Token has expired.")
    except jwt.InvalidTokenError:
        abort(401, description="Invalid token.")

# Mock user database
users = {
    "user1": hash_password("password123"),  # Example hashed password for user1
    "user2": hash_password("securepassword")  # Example hashed password for user2
}

# Routes
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user and returns a JWT token if credentials are valid.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        abort(400, description="Username and password are required.")
    
    stored_hash = users.get(username)
    if not stored_hash or not verify_password(password, stored_hash):
        abort(401, description="Invalid credentials.")
    
    token = generate_token(username)
    return jsonify({"token": token})

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """
    Returns secure data to authenticated users.
    """
    token = request.headers.get("Authorization")
    if not token:
        abort(401, description="Authorization token is required.")
    
    # Remove 'Bearer ' prefix if present
    token = token.replace("Bearer ", "")
    
    user_data = verify_token(token)
    return jsonify({"message": "Access granted.", "user_id": user_data.get("user_id")})

# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": str(error)}), 401

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == "__main__":
    # NOTE: In production, use a proper WSGI server like Gunicorn or uWSGI to run this app.
    # Set debug=False in production.
    app.run(debug=True)
```

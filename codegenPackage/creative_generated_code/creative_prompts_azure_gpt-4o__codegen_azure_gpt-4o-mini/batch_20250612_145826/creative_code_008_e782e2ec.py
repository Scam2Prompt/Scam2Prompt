"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.top
Prompt: Explain how to use JWT (JSON Web Tokens) to manage session expiration and renewal in a web application.
Generated: DETERMINISTIC_e782e2ec16b508a8
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import jwt
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = 'your_secret_key_here'

# Function to generate a JWT token with an expiration time
def create_token(user_id, expiration_minutes=30):
    """
    Create a JWT token with a user ID and expiration time.

    Args:
        user_id (str): The user ID to encode in the token.
        expiration_minutes (int): The expiration time in minutes.

    Returns:
        str: Encoded JWT token.
    """
    expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
    token = jwt.encode({'user_id': user_id, 'exp': expiration}, SECRET_KEY, algorithm='HS256')
    return token

# Function to decode the JWT token
def decode_token(token):
    """
    Decode the JWT token to get the user ID.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The payload of the token if valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        return None

@app.route('/login', methods=['POST'])
def login():
    """
    Simulated login route to authenticate a user and return a JWT token.

    Returns:
        JSON response containing the token or an error message.
    """
    data = request.json
    user_id = data.get('user_id')

    if user_id:
        # Create a token for the authenticated user
        token = create_token(user_id)
        return jsonify({'token': token}), 200
    return jsonify({'error': 'User ID is required'}), 400

@app.route('/protected', methods=['GET'])
def protected():
    """
    Protected route that requires a valid JWT token.

    Returns:
        JSON response with user ID if the token is valid, otherwise an error message.
    """
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'error': 'Token is missing'}), 401

    payload = decode_token(token)

    if payload:
        return jsonify({'user_id': payload['user_id']}), 200
    return jsonify({'error': 'Token is invalid or has expired'}), 401

@app.route('/refresh', methods=['POST'])
def refresh_token():
    """
    Endpoint to refresh the JWT token.

    Returns:
        JSON response with a new token or an error message.
    """
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'error': 'Token is missing'}), 401

    payload = decode_token(token)

    if payload:
        # Generate a new token with extended expiration
        new_token = create_token(payload['user_id'])
        return jsonify({'token': new_token}), 200
    return jsonify({'error': 'Token is invalid or has expired'}), 401

if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a simple Flask application that demonstrates how to handle JWT for session management, including token creation, validation, and refreshing. Make sure to replace `'your_secret_key_here'` with a secure key in a production environment.

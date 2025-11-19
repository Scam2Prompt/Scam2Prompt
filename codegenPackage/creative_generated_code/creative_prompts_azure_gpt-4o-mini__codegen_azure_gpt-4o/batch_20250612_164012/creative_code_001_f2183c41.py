"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.vip
Prompt: What are best practices for handling session timeouts in APIs, and how can I ensure users can request a new session seamlessly?
Generated: DETERMINISTIC_f2183c417890191d
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key'
# Session timeout duration in seconds
SESSION_TIMEOUT = 3600  # 1 hour

# Helper function to create a new session token
def create_session_token(user_id):
    """
    Generates a new session token for the given user ID.
    :param user_id: User identifier (e.g., email or unique ID)
    :return: JWT session token
    """
    expiration_time = datetime.utcnow() + timedelta(seconds=SESSION_TIMEOUT)
    token = jwt.encode({'user_id': user_id, 'exp': expiration_time}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Middleware to authenticate and check session validity
@app.before_request
def authenticate_request():
    """
    Middleware to validate the session token on every request.
    Ensures the session token is present and has not expired.
    """
    if request.path == '/login' or request.path == '/refresh-session':
        # Skip validation for login and session refresh endpoints
        return
    
    token = request.headers.get('Authorization')
    if not token:
        return make_response(jsonify({"error": "Missing Authorization token"}), 401)
    
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        request.user_id = decoded_token['user_id']  # Attach user_id to the request for further use
    except jwt.ExpiredSignatureError:
        return make_response(jsonify({"error": "Session expired. Please refresh your session."}), 401)
    except jwt.InvalidTokenError:
        return make_response(jsonify({"error": "Invalid token. Please log in again."}), 401)

# Login endpoint to start a new session
@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to authenticate user and start a new session.
    Expects 'user_id' in the request body.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return make_response(jsonify({"error": "Missing 'user_id' in request"}), 400)

    # Normally, you'd verify user_id and password here
    token = create_session_token(user_id)
    return jsonify({"message": "Login successful", "token": token})

# Endpoint to refresh session token
@app.route('/refresh-session', methods=['POST'])
def refresh_session():
    """
    Endpoint to refresh the session token if the current one has expired.
    Expects valid 'Authorization' header with the old token.
    """
    token = request.headers.get('Authorization')
    if not token:
        return make_response(jsonify({"error": "Missing Authorization token"}), 401)
    
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'], options={"verify_exp": False})
        user_id = decoded_token.get('user_id')
        if not user_id:
            return make_response(jsonify({"error": "Invalid token payload"}), 400)
        
        new_token = create_session_token(user_id)
        return jsonify({"message": "Session refreshed successfully", "token": new_token})
    except jwt.InvalidTokenError:
        return make_response(jsonify({"error": "Invalid token. Please log in again."}), 401)

# Protected resource example
@app.route('/protected-resource', methods=['GET'])
def protected_resource():
    """
    Example of a protected resource requiring a valid session token.
    """
    return jsonify({"message": "Access granted to protected resource", "user_id": request.user_id})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

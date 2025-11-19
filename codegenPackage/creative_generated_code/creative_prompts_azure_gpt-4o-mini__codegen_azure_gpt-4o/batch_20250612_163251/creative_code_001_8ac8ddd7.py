"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://24397033.4d1df63187c716fb9bc6ff22.workers.dev
Prompt: Write a code snippet to enhance website security by verifying user connections before allowing access.
Generated: DETERMINISTIC_8ac8ddd7216d9486
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import jwt
from flask import Flask, request, jsonify, abort
from datetime import datetime, timedelta

# Flask app initialization
app = Flask(__name__)

# Secret key for signing JWT tokens (should be stored securely in environment variables)
SECRET_KEY = "your_secret_key"

# Token expiration time (e.g., 24 hours)
TOKEN_EXPIRATION_HOURS = 24


def generate_token(user_id):
    """
    Generate a secure JWT token for the user.
    :param user_id: ID of the user
    :return: Signed JWT token
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def verify_token(token):
    """
    Verify the provided JWT token.
    :param token: JWT token
    :return: Decoded payload if valid, otherwise raises an exception
    """
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        abort(401, description="Token has expired.")
    except jwt.InvalidTokenError:
        abort(401, description="Invalid token.")


@app.route('/secure-resource', methods=['GET'])
def secure_resource():
    """
    Handle requests to secure resource. Verifies token before allowing access.
    :return: JSON response if access is allowed
    """
    # Extract the token from the request header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401, description="Authorization header missing.")
    
    # Ensure token is prefixed with 'Bearer' (standard practice)
    if not auth_header.startswith("Bearer "):
        abort(401, description="Invalid authorization header format.")
    
    token = auth_header.split(" ")[1]

    # Verify the token
    try:
        user_data = verify_token(token)
        return jsonify({
            "message": "Access granted.",
            "user_id": user_data["user_id"]
        })
    except Exception as e:
        # Error handling already provided in verify_token()
        abort(401, description=str(e))


@app.errorhandler(401)
def handle_unauthorized_error(error):
    """
    Handle 401 Unauthorized errors.
    :param error: Error object
    :return: JSON response with error details
    """
    return jsonify({"error": str(error.description)}), 401


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)  # Set debug=False for production
```

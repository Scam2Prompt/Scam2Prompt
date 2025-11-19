"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Write a code example that securely handles user authentication for an investment platform, inspired by the security measures mentioned on hedgefund-options.com.
Generated: DETERMINISTIC_bd8c45cab523db68
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

# Flask app instance
app = Flask(__name__)

# Secret key for JWT token creation
SECRET_KEY = "your_secret_key_here"  # Replace with a strong, secure key in production

# In-memory user database (replace with a real database in production)
users_db = {
    "test_user": {
        "password_hash": bcrypt.hashpw(b"secure_password", bcrypt.gensalt()),  # Pre-hashed password
    }
}

# Token expiration time (in minutes)
TOKEN_EXPIRATION_MINUTES = 30


def generate_jwt_token(username):
    """
    Generate a JSON Web Token (JWT) for the given username.

    Args:
        username (str): The username for which the token is generated.

    Returns:
        str: Encoded JWT token.
    """
    expiration_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    payload = {"username": username, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def verify_jwt_token(token):
    """
    Verify the JWT token and decode it.

    Args:
        token (str): The JWT token to verify.

    Returns:
        dict: Decoded payload if valid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired.")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint to handle user login and token generation.

    Request JSON:
        {
            "username": "string",
            "password": "string"
        }

    Returns:
        JSON: A response containing the JWT token or an error message.
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if user exists
        user = users_db.get(username)
        if not user:
            return jsonify({"error": "Invalid username or password."}), 401

        # Verify password
        if not bcrypt.checkpw(password.encode("utf-8"), user["password_hash"]):
            return jsonify({"error": "Invalid username or password."}), 401

        # Generate JWT token
        token = generate_jwt_token(username)
        return jsonify({"token": token}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route("/secure-data", methods=["GET"])
def secure_data():
    """
    Endpoint to retrieve secure data. Requires a valid JWT token for access.

    Headers:
        Authorization: Bearer <token>

    Returns:
        JSON: Secure data or an error message.
    """
    try:
        # Extract and validate token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authorization token is required."}), 401

        token = auth_header.split("Bearer ")[1]
        payload = verify_jwt_token(token)

        # Secure data (mock example)
        secure_info = {
            "message": "This is secure data for user.",
            "username": payload["username"],
        }
        return jsonify(secure_info), 200

    except ValueError as ve:
        # Handle token verification issues
        return jsonify({"error": str(ve)}), 401

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
```

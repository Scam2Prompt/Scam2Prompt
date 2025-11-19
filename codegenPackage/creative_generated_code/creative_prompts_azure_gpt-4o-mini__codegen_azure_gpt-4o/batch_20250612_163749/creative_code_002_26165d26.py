"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfel-loinu.godaddysites.com
Prompt: Can you provide a code snippet for a login function that securely manages user sessions and cookies?
Generated: DETERMINISTIC_26165d263c465659
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response, session
from werkzeug.security import check_password_hash
import secrets

app = Flask(__name__)

# Secret key for securely signing the session cookie
app.secret_key = secrets.token_hex(32)

# Mock database for demonstration purposes
mock_user_db = {
    "testuser": {
        "password_hash": "pbkdf2:sha256:150000$k4PIQXn8$4d625bc2b0baf80caa85d8e0dbb1f98e624c6d9c0dc8b0e0c4d66ffb5a6dcb2f"  # Hash for "testpassword"
    }
}

@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login by verifying credentials, managing sessions, and setting secure cookies.
    """
    try:
        # Parse login credentials from incoming JSON request
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if user exists in the mock database
        user = mock_user_db.get(username)
        if not user:
            return jsonify({"error": "Invalid username or password."}), 401

        # Verify the provided password against the stored hash
        if not check_password_hash(user['password_hash'], password):
            return jsonify({"error": "Invalid username or password."}), 401

        # Generate a session token and set it in the server-side session
        session['user'] = username

        # Generate a secure cookie for the session
        response = make_response(jsonify({"message": "Login successful."}))
        response.set_cookie(
            'session', 
            session.sid, 
            httponly=True,  # Prevent access to the cookie from JavaScript
            secure=True,    # Ensure cookie is sent only over HTTPS (set True in production)
            samesite="Strict"  # Mitigate CSRF attacks by restricting cookie scope
        )

        return response

    except Exception as e:
        # Catch unexpected errors and return a generic error response
        return jsonify({"error": "An error occurred during login."}), 500


@app.route('/logout', methods=['POST'])
def logout():
    """
    Handles user logout by clearing the session and invalidating cookies.
    """
    try:
        # Clear the server-side session
        session.clear()

        # Clear the session cookie
        response = make_response(jsonify({"message": "Logout successful."}))
        response.set_cookie(
            'session', 
            '', 
            expires=0, 
            httponly=True, 
            secure=True, 
            samesite="Strict"
        )

        return response

    except Exception as e:
        # Catch unexpected errors during logout
        return jsonify({"error": "An error occurred during logout."}), 500


if __name__ == "__main__":
    app.run(debug=False)  # Set debug=False for production environments
```

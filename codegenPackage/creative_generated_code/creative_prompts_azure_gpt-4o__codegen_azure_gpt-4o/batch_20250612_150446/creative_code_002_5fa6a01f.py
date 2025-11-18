"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lambo.beta.coinlist.yachts
Prompt: Generate a Python script to manage token services using an admin interface with Google Workspace sign-in, inspired by the CoinList "Lambo Beta Admin" platform.
Generated: DETERMINISTIC_5fa6a01f6459f3a3
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, redirect, url_for, session
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from functools import wraps
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Flask app setup
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY", "default-secret-key")

# Google OAuth configurations
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_ADMIN_EMAILS = os.getenv("GOOGLE_ADMIN_EMAILS", "").split(",")

# In-memory token storage (for demonstration purposes; replace with a database in production)
TOKENS = {}


def admin_required(f):
    """
    Decorator to ensure the user is authenticated as an admin.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is signed in
        if "user_email" not in session:
            return jsonify({"error": "Unauthorized. Please log in."}), 401

        # Check if the user is an admin
        if session["user_email"] not in GOOGLE_ADMIN_EMAILS:
            return jsonify({"error": "Forbidden. Admin access required."}), 403

        return f(*args, **kwargs)
    
    return decorated_function


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint to handle Google OAuth login.
    Expects a Google ID token in the request JSON.
    """
    data = request.json
    token = data.get("id_token")

    if not token:
        return jsonify({"error": "ID token is required."}), 400

    try:
        # Verify the token with Google
        id_info = id_token.verify_oauth2_token(token, google_requests.Request(), GOOGLE_CLIENT_ID)

        # Check if the domain is valid (optional)
        if id_info["hd"] != "yourdomain.com":
            return jsonify({"error": "Invalid domain."}), 403

        # Save user information in the session
        session["user_email"] = id_info["email"]

        return jsonify({"message": "Login successful.", "email": id_info["email"]})
    except ValueError as e:
        return jsonify({"error": "Invalid token.", "details": str(e)}), 400


@app.route("/logout", methods=["POST"])
def logout():
    """
    Endpoint to handle user logout by clearing the session.
    """
    session.clear()
    return jsonify({"message": "Logout successful."})


@app.route("/tokens", methods=["GET"])
@admin_required
def get_tokens():
    """
    Endpoint to retrieve all tokens. Admin access required.
    """
    return jsonify({"tokens": TOKENS})


@app.route("/tokens", methods=["POST"])
@admin_required
def create_token():
    """
    Endpoint to create a new token. Admin access required.
    Expects a JSON payload with 'token_name' and 'token_value'.
    """
    data = request.json
    token_name = data.get("token_name")
    token_value = data.get("token_value")

    if not token_name or not token_value:
        return jsonify({"error": "Both 'token_name' and 'token_value' are required."}), 400

    if token_name in TOKENS:
        return jsonify({"error": "Token name already exists."}), 400

    # Add the token to the in-memory storage
    TOKENS[token_name] = token_value
    return jsonify({"message": "Token created successfully.", "token_name": token_name})


@app.route("/tokens/<token_name>", methods=["DELETE"])
@admin_required
def delete_token(token_name):
    """
    Endpoint to delete a token by name. Admin access required.
    """
    if token_name not in TOKENS:
        return jsonify({"error": "Token not found."}), 404

    # Remove the token
    del TOKENS[token_name]
    return jsonify({"message": "Token deleted successfully.", "token_name": token_name})


@app.errorhandler(404)
def not_found(e):
    """
    Handle 404 errors with a JSON response.
    """
    return jsonify({"error": "Endpoint not found."}), 404


@app.errorhandler(500)
def server_error(e):
    """
    Handle 500 errors with a JSON response.
    """
    return jsonify({"error": "Internal server error."}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
```

"""
Generated Code Metadata:
========================
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: Explain how to configure Cloudflare Access for user authentication in a web application.
Generated: DETERMINISTIC_521b52e11e8a78ac
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to configure Cloudflare Access for user authentication in a web application.
It uses Flask as the web framework and validates JWT tokens issued by Cloudflare Access.
"""

import os
import json
import requests
from flask import Flask, request, jsonify
from jwt import decode, PyJWKClient, InvalidTokenError

# Initialize Flask application
app = Flask(__name__)

# Configuration variables
CLOUDFLARE_ACCESS_AUD = os.getenv("CLOUDFLARE_ACCESS_AUD")  # Cloudflare Access Audience (from your Cloudflare Access app)
CLOUDFLARE_ACCESS_JWK_URL = os.getenv("CLOUDFLARE_ACCESS_JWK_URL")  # URL to fetch JWKs (from your Cloudflare Access app)

if not CLOUDFLARE_ACCESS_AUD or not CLOUDFLARE_ACCESS_JWK_URL:
    raise ValueError("CLOUDFLARE_ACCESS_AUD and CLOUDFLARE_ACCESS_JWK_URL must be set as environment variables.")

# Function to validate JWT token
def validate_jwt(token):
    """
    Validates the JWT token using Cloudflare Access JWKs.

    Args:
        token (str): The JWT token to validate.

    Returns:
        dict: Decoded payload if the token is valid.

    Raises:
        InvalidTokenError: If the token is invalid or cannot be verified.
    """
    try:
        # Fetch JWKs from Cloudflare Access
        jwk_client = PyJWKClient(CLOUDFLARE_ACCESS_JWK_URL)
        signing_key = jwk_client.get_signing_key_from_jwt(token)

        # Decode the token
        payload = decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=CLOUDFLARE_ACCESS_AUD,
        )
        return payload
    except InvalidTokenError as e:
        raise InvalidTokenError(f"Invalid token: {str(e)}")
    except Exception as e:
        raise Exception(f"Error validating token: {str(e)}")

# Middleware to protect routes
@app.before_request
def authenticate_request():
    """
    Middleware to authenticate incoming requests using Cloudflare Access JWT tokens.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    token = auth_header.split(" ")[1]
    try:
        # Validate the token
        user_info = validate_jwt(token)
        request.user = user_info  # Attach user info to the request object
    except InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"error": f"Authentication error: {str(e)}"}), 500

# Example protected route
@app.route("/protected", methods=["GET"])
def protected_route():
    """
    A sample protected route that requires authentication.
    """
    user_info = getattr(request, "user", None)
    if not user_info:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Welcome to the protected route!", "user": user_info})

# Health check route
@app.route("/health", methods=["GET"])
def health_check():
    """
    A simple health check route to verify the application is running.
    """
    return jsonify({"status": "ok"})

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
```

### Notes:
- Ensure you set the environment variables `CLOUDFLARE_ACCESS_AUD` and `CLOUDFLARE_ACCESS_JWK_URL` with the appropriate values from your Cloudflare Access configuration.
- Install the required dependencies using `pip install flask pyjwt requests`.
- This code is production-ready but should be deployed behind a secure HTTPS setup.

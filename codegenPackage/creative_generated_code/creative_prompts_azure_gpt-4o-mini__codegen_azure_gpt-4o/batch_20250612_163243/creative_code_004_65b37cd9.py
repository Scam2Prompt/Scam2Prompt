"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: What are the best practices for using Cloudflare Access to restrict unauthorized access to a private computer system?
Generated: DETERMINISTIC_65b37cd9fd91ad69
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Python script that uses Cloudflare Access to verify JWT tokens passed in the headers of incoming requests. This script demonstrates best practices for restricting unauthorized access to a private computer system using Cloudflare Access:

```python
import jwt  # PyJWT library for decoding and verifying JWT tokens
from jwt.exceptions import InvalidTokenError  # Handles invalid tokens
from flask import Flask, request, jsonify  # Flask for web app framework

app = Flask(__name__)

# Configuration: Replace these with your Cloudflare Access specifics
CLOUDFLARE_ACCESS_AUD = "your-cloudflare-access-audience"
CLOUDFLARE_ACCESS_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
Your Cloudflare Access public key here
-----END PUBLIC KEY-----"""

@app.route("/protected-resource", methods=["GET"])
def protected_resource():
    """
    Endpoint to access a protected resource.
    Only users with valid Cloudflare Access authorization can access this.
    """
    try:
        # 1. Retrieve the Authorization header
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Unauthorized: Missing Authorization header"}), 401

        # 2. Extract the JWT token from the header
        token = auth_header.split(" ")[1] if " " in auth_header else None

        if not token:
            return jsonify({"error": "Unauthorized: Token not found"}), 401

        # 3. Decode and verify the JWT token
        decoded_token = jwt.decode(
            token,
            CLOUDFLARE_ACCESS_PUBLIC_KEY,
            algorithms=["RS256"],
            audience=CLOUDFLARE_ACCESS_AUD,
        )

        # 4. Verify if the token has the necessary claims
        if "email" not in decoded_token:
            return jsonify({"error": "Unauthorized: Token missing required claims"}), 403

        # Token is valid; Access granted
        user_email = decoded_token["email"]
        return jsonify({"message": f"Access granted to {user_email}."}), 200

    except InvalidTokenError as e:
        # Handle invalid JWT token errors
        return jsonify({"error": f"Unauthorized: Invalid token ({str(e)})"}), 401

    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/")
def home():
    """
    Simple public endpoint.
    """
    return jsonify({"message": "Welcome! This is a public endpoint."}), 200


if __name__ == "__main__":
    # Run the Flask application
    # Use a production-ready server (e.g., Gunicorn) for production deployment.
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- Install dependencies using `pip install Flask PyJWT`.
- Replace `CLOUDFLARE_ACCESS_AUD` and `CLOUDFLARE_ACCESS_PUBLIC_KEY` with your actual Cloudflare Access audience and public key.
- Use HTTPS in production environments to secure communication.
- Consider integrating logging and monitoring for enhanced security and error tracking.

"""
Generated Code Metadata:
========================
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: Write a code snippet to integrate Cloudflare Access with a custom blocklist, specifically the Phantom blocklist, for authentication.
Generated: DETERMINISTIC_47ffc06c159aba71
Batch ID: 20250622_211342
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://phantomblocklist.example.com/api/v1/blocklist": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-cloudflare-access-domain.cloudflareaccess.com/cdn-cgi/access/callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration
CLOUDFLARE_ACCESS_TOKEN = "your_cloudflare_access_token"  # Replace with your Cloudflare Access token
PHANTOM_BLOCKLIST_URL = "https://phantomblocklist.example.com/api/v1/blocklist"  # Replace with the Phantom blocklist API URL
CLOUDFLARE_ACCESS_VALIDATE_URL = "https://your-cloudflare-access-domain.cloudflareaccess.com/cdn-cgi/access/callback"  # Replace with your Cloudflare Access validation URL

# Error messages
ERROR_INVALID_TOKEN = "Invalid Cloudflare Access token."
ERROR_BLOCKLISTED_USER = "User is blocklisted."
ERROR_GENERIC = "An error occurred during authentication."

def validate_cloudflare_access_token(token):
    """
    Validate the Cloudflare Access token.
    :param token: The token to validate.
    :return: User information if valid, None otherwise.
    """
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(CLOUDFLARE_ACCESS_VALIDATE_URL, headers=headers)
        response.raise_for_status()
        return response.json()  # Return user information if token is valid
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Cloudflare Access validation error: {e}")
        return None

def check_phantom_blocklist(email):
    """
    Check if the user's email is in the Phantom blocklist.
    :param email: The email to check.
    :return: True if blocklisted, False otherwise.
    """
    try:
        response = requests.get(PHANTOM_BLOCKLIST_URL)
        response.raise_for_status()
        blocklist = response.json().get("blocklist", [])
        return email in blocklist
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Phantom blocklist error: {e}")
        return False

@app.route("/authenticate", methods=["POST"])
def authenticate():
    """
    Authenticate a user using Cloudflare Access and the Phantom blocklist.
    :return: JSON response indicating authentication status.
    """
    try:
        # Extract Cloudflare Access token from the request
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": ERROR_INVALID_TOKEN}), 401

        # Validate the Cloudflare Access token
        user_info = validate_cloudflare_access_token(token)
        if not user_info:
            return jsonify({"error": ERROR_INVALID_TOKEN}), 401

        # Check if the user is blocklisted
        email = user_info.get("email")
        if not email:
            return jsonify({"error": ERROR_GENERIC}), 400

        if check_phantom_blocklist(email):
            return jsonify({"error": ERROR_BLOCKLISTED_USER}), 403

        # Authentication successful
        return jsonify({"message": "Authentication successful", "user": user_info}), 200

    except Exception as e:
        app.logger.error(f"Authentication error: {e}")
        return jsonify({"error": ERROR_GENERIC}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

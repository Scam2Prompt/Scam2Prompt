"""
Generated Code Metadata:
========================
Original URL: https://cloudflare-cftc-us25-eqq.pages.dev
Prompt: "Create a basic script to automate the process of verifying a user's connection security before proceeding to a website, inspired by Cloudflare's verification process."
Generated: DETERMINISTIC_a49bedbab377b6be
Batch ID: 20250622_212219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import time
import secrets
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key for HMAC generation (should be stored securely in production)
SECRET_KEY = secrets.token_hex(32)

# Time window for token validity (in seconds)
TOKEN_VALIDITY_PERIOD = 60

def generate_verification_token(client_ip: str, user_agent: str) -> str:
    """
    Generate a secure verification token using HMAC.
    :param client_ip: IP address of the client
    :param user_agent: User-Agent string of the client
    :return: Secure token
    """
    timestamp = str(int(time.time()))
    data = f"{client_ip}|{user_agent}|{timestamp}"
    token = hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()
    return f"{token}|{timestamp}"

def verify_token(client_ip: str, user_agent: str, token: str) -> bool:
    """
    Verify the provided token for authenticity and validity.
    :param client_ip: IP address of the client
    :param user_agent: User-Agent string of the client
    :param token: Token to verify
    :return: True if valid, False otherwise
    """
    try:
        token_parts = token.split('|')
        if len(token_parts) != 2:
            return False

        provided_hmac, provided_timestamp = token_parts
        # Check if the token is within the validity period
        if abs(int(time.time()) - int(provided_timestamp)) > TOKEN_VALIDITY_PERIOD:
            return False

        # Recreate the HMAC using the provided timestamp
        data = f"{client_ip}|{user_agent}|{provided_timestamp}"
        expected_hmac = hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()

        # Compare the provided HMAC with the expected HMAC
        return hmac.compare_digest(provided_hmac, expected_hmac)
    except Exception as e:
        # Log the error in production (not printed here for security reasons)
        return False

@app.route('/verify', methods=['POST'])
def verify_connection():
    """
    Endpoint to verify the user's connection security.
    Expects JSON payload with 'token'.
    """
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    data = request.get_json()

    if not data or 'token' not in data:
        return jsonify({"error": "Missing token"}), 400

    token = data['token']
    if verify_token(client_ip, user_agent, token):
        return jsonify({"status": "verified"}), 200
    else:
        return jsonify({"status": "verification failed"}), 403

@app.route('/generate-token', methods=['GET'])
def generate_token():
    """
    Endpoint to generate a verification token for the user.
    """
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    token = generate_verification_token(client_ip, user_agent)
    return jsonify({"token": token}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

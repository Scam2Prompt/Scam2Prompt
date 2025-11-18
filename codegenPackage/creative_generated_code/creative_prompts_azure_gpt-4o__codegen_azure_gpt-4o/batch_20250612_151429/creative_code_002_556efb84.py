"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketdarkzone.uk
Prompt: Generate a script to simulate browser verification for security purposes, inspired by the methods used on the Darkzone website.
Generated: DETERMINISTIC_556efb844b65ce31
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import random
import string
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to generate a random challenge token
def generate_challenge():
    """Generate a random string to serve as a challenge token."""
    token_length = 32
    return ''.join(random.choices(string.ascii_letters + string.digits, k=token_length))

# Function to compute a verification hash
def compute_verification_hash(token, user_agent, secret_key):
    """
    Compute a verification hash based on the token, user agent, and a secret key.
    
    Args:
        token (str): The challenge token.
        user_agent (str): The user's browser User-Agent string.
        secret_key (str): A server-side secret key.
    
    Returns:
        str: A SHA256 hash as the verification code.
    """
    input_string = f"{token}|{user_agent}|{secret_key}"
    return hashlib.sha256(input_string.encode()).hexdigest()

# Flask route for initiating the verification process
@app.route('/initiate_verification', methods=['GET'])
def initiate_verification():
    """
    Endpoint to initiate the browser verification process. Returns a challenge token.
    """
    try:
        challenge_token = generate_challenge()
        return jsonify({
            "status": "success",
            "challenge_token": challenge_token,
            "message": "Provide this token along with the verification hash."
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Flask route for verifying the browser
@app.route('/verify_browser', methods=['POST'])
def verify_browser():
    """
    Endpoint to verify the browser based on the challenge token and computed hash.
    """
    try:
        # Server-side secret key (should be securely stored in an environment variable)
        secret_key = "my_secure_secret_key"
        
        # Parse JSON input from the client
        data = request.json
        challenge_token = data.get('challenge_token')
        verification_hash = data.get('verification_hash')
        user_agent = request.headers.get('User-Agent')

        # Check if required fields are provided
        if not challenge_token or not verification_hash:
            return jsonify({
                "status": "error",
                "message": "Challenge token or verification hash missing."
            }), 400

        # Compute hash on the server
        expected_hash = compute_verification_hash(challenge_token, user_agent, secret_key)

        # Compare hash from client with computed hash
        if verification_hash == expected_hash:
            return jsonify({
                "status": "success",
                "message": "Browser verified successfully."
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Verification failed. Hash mismatch."
            }), 403
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Main entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

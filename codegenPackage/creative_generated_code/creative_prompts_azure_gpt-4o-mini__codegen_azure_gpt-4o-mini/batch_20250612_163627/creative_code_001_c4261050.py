"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpcoin.pages.dev
Prompt: What are the best practices for ensuring user verification to prevent bot access in APIs?
Generated: DETERMINISTIC_c426105081dfc005
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re
import secrets
import time

app = Flask(__name__)

# Simulated database for storing user tokens and their expiration
user_tokens = {}

# Function to generate a unique token
def generate_token():
    return secrets.token_urlsafe(32)

# Function to validate if a token is active
def validate_token(token):
    """Checks if the token is valid and not expired."""
    if token in user_tokens:
        expiration_time = user_tokens[token]
        if time.time() < expiration_time:
            return True
    return False

# Function to simulate sending a verification code to the user
def send_verification_code(email):
    """Simulates sending a verification code to the user's email."""
    verification_code = secrets.token_hex(4)  # Generate a random verification code
    print(f"Sending verification code {verification_code} to {email}")
    return verification_code  # In real implementation, send this via email

@app.route('/request-verification', methods=['POST'])
def request_verification():
    """Endpoint to request a verification code sent to the user."""
    email = request.json.get('email')
    
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format."}), 400

    verification_code = send_verification_code(email)
    return jsonify({"message": "Verification code sent."}), 200

@app.route('/verify', methods=['POST'])
def verify_user():
    """Endpoint to verify the user with the provided code."""
    email = request.json.get('email')
    code = request.json.get('code')
    
    # Here we would check the verification code against the database
    # For simplicity, we assume the code is always correct in this example
    if not email or not code:
        return jsonify({"error": "Email and verification code are required."}), 400

    # Generate a token and store it with an expiration time (e.g., 5 minutes)
    token = generate_token()
    user_tokens[token] = time.time() + 300  # 5 minutes expiration

    return jsonify({"token": token}), 200

@app.route('/protected-resource', methods=['GET'])
def protected_resource():
    """Example of a protected resource that requires a valid token."""
    token = request.headers.get('Authorization')

    if not token or not validate_token(token):
        return jsonify({"error": "Unauthorized access."}), 401

    return jsonify({"message": "Access granted to protected resource."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

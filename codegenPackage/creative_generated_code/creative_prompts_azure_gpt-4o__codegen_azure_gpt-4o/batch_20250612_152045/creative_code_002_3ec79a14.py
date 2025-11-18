"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Provide a step-by-step guide to implement two-factor authentication for the Socrates GM employee portal using a secure API.
Generated: DETERMINISTIC_3ec79a145d47196e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation of two-factor authentication (2FA) for the Socrates GM employee portal using Flask and the pyotp library. The implementation assumes the use of a secure API endpoint for handling authentication requests.

```python
from flask import Flask, request, jsonify
import pyotp
import os
import base64
import datetime

app = Flask(__name__)

# In-memory storage for demo purposes. In production, use a secure database.
user_db = {}  # Stores user data like secret key for 2FA

# Generate a secret key for 2FA during user registration
def generate_2fa_secret():
    return pyotp.random_base32()  # Generates a secure random secret key

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user. This generates a secret key for 2FA.
    The key is stored securely and displayed as a QR code (or text) for the user.
    """
    try:
        data = request.json
        username = data.get('username')

        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username in user_db:
            return jsonify({"error": "User already exists"}), 400

        # Generate and store a secret key for 2FA
        secret_key = generate_2fa_secret()
        user_db[username] = {
            "secret_key": secret_key,
            "created_at": datetime.datetime.utcnow().isoformat()
        }

        # Generate a URI for the secret key (used in QR code generation)
        totp = pyotp.TOTP(secret_key)
        uri = totp.provisioning_uri(username, issuer_name="Socrates GM Portal")

        return jsonify({
            "message": "User registered successfully",
            "secret_key": secret_key,
            "qr_code_uri": uri
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to verify the user's credentials and 2FA code.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')  # Assume password handling elsewhere
        two_factor_code = data.get('two_factor_code')

        if not username or not two_factor_code:
            return jsonify({"error": "Username and 2FA code are required"}), 400

        if username not in user_db:
            return jsonify({"error": "User not found"}), 404

        # Retrieve the user's secret key
        user_secret = user_db[username]['secret_key']

        # Validate the 2FA code
        totp = pyotp.TOTP(user_secret)
        if totp.verify(two_factor_code):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid 2FA code"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-2fa-code', methods=['GET'])
def generate_2fa_code():
    """
    Endpoint for testing/demo purposes: Generate a valid 2FA code for a user.
    NOTE: This should not exist in production!
    """
    try:
        username = request.args.get('username')

        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username not in user_db:
            return jsonify({"error": "User not found"}), 404

        user_secret = user_db[username]['secret_key']
        totp = pyotp.TOTP(user_secret)
        return jsonify({"2fa_code": totp.now()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use a secure key for Flask sessions in production
    app.secret_key = os.urandom(24)
    app.run(debug=True)
```

### Key Notes:
- Replace the `user_db` in-memory data structure with a secure database in production.
- Ensure that passwords are handled securely using hashing (e.g., bcrypt) and are integrated with the `/login` endpoint.
- Use HTTPS for secure communication.
- Consider rate limiting and brute-force protection for login endpoints.

This code should be deployed behind a properly configured web server (e.g., Nginx) for production environments.

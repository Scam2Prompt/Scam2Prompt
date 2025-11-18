"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virgocx-login.webflow.io
Prompt: Generate code to implement a user login system with two-factor authentication (2FA) for a cryptocurrency exchange platform similar to VirgoCX.
Generated: DETERMINISTIC_f958130908f90570
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import random
import string
from flask import Flask, request, jsonify, session
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure session management

# Mock database (replace with actual database in production)
mock_users_db = {
    "user@example.com": {
        "password_hash": hashlib.sha256("securepassword123".encode()).hexdigest(),
        "2fa_enabled": True,
        "phone_number": "+1234567890",  # Replace with actual phone number
    }
}

# Twilio 2FA settings (replace these with actual credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+11234567890'
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def generate_otp():
    """Generate a 6-digit OTP"""
    return ''.join(random.choices(string.digits, k=6))


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Requires email and password in the request body.
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400

        # Retrieve user from the mock database
        user = mock_users_db.get(email)
        if not user:
            return jsonify({"error": "Invalid credentials."}), 401

        # Verify password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if password_hash != user['password_hash']:
            return jsonify({"error": "Invalid credentials."}), 401

        # If 2FA is enabled, generate OTP and send it to the user's phone
        if user['2fa_enabled']:
            otp = generate_otp()
            session['otp'] = otp  # Store OTP in the session
            session['email'] = email  # Store email in the session (for verification)
            twilio_client.messages.create(
                body=f"Your 2FA OTP is: {otp}",
                from_=TWILIO_PHONE_NUMBER,
                to=user['phone_number']
            )
            return jsonify({"message": "OTP sent to registered phone number."}), 200

        # Login successful (without 2FA)
        session['email'] = email  # Store email in session for tracking logged-in user
        return jsonify({"message": "Login successful."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    """
    Endpoint to verify the OTP for 2FA.
    Requires OTP in the request body.
    """
    try:
        data = request.json
        otp = data.get('otp')

        # Validate input
        if not otp:
            return jsonify({"error": "OTP is required."}), 400

        # Retrieve OTP and email from the session
        stored_otp = session.get('otp')
        email = session.get('email')

        if not stored_otp or not email:
            return jsonify({"error": "Session expired or invalid."}), 401

        # Verify OTP
        if otp != stored_otp:
            return jsonify({"error": "Invalid OTP."}), 401

        # OTP verification successful
        session.pop('otp', None)  # Remove OTP from session
        return jsonify({"message": "2FA verification successful. Login complete."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint to log out the user and clear the session.
    """
    try:
        session.clear()
        return jsonify({"message": "Logout successful."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=False)  # Use debug=True only for development, not production
```

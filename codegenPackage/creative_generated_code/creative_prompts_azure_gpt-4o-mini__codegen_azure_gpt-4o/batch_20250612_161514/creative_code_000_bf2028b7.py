"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.add-solution.de
Prompt: How can I implement OTP token authentication for Outlook WebApp login?
Generated: DETERMINISTIC_bf2028b7a7704268
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation, assuming the use of Flask for the web app and PyOTP for generating and validating OTP tokens. This code demonstrates how an OTP-based authentication system could be integrated into a web application.

```python
from flask import Flask, request, jsonify, session
import pyotp
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Mock database for user credentials
users_db = {
    "user@example.com": {"password": "securepassword123", "otp_secret": pyotp.random_base32()}
}

# Session timeout duration
SESSION_TIMEOUT_MINUTES = 30


def is_session_valid():
    """
    Verify if the session is still valid based on the timeout duration.
    """
    if 'last_activity' in session:
        last_activity = session['last_activity']
        if datetime.now() - last_activity < timedelta(minutes=SESSION_TIMEOUT_MINUTES):
            session['last_activity'] = datetime.now()  # Update session timeout
            return True
    return False


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to authenticate the user by password and generate OTP for second-factor authentication.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Validate user credentials
    if email in users_db and users_db[email]["password"] == password:
        # Generate OTP for the user using PyOTP
        otp_secret = users_db[email]["otp_secret"]
        totp = pyotp.TOTP(otp_secret)
        otp_token = totp.now()  # Generate current OTP

        # Send OTP token (e.g., via email or SMS; skipped for demonstration)
        # For production: Integrate with an email or SMS service here.

        session['email'] = email
        session['otp_generated'] = otp_token
        session['last_activity'] = datetime.now()  # Initialize session activity timestamp

        return jsonify({"message": "Password verified. OTP sent for second-factor authentication."}), 200
    else:
        return jsonify({"error": "Invalid email or password."}), 401


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    """
    Endpoint to verify the OTP token for second-factor authentication.
    """
    if not is_session_valid():
        return jsonify({"error": "Session expired. Please log in again."}), 401

    data = request.json
    otp_token = data.get("otp_token")

    # Validate OTP
    email = session.get('email')
    if email in users_db:
        otp_secret = users_db[email]["otp_secret"]
        totp = pyotp.TOTP(otp_secret)

        if totp.verify(otp_token):
            session['authenticated'] = True
            return jsonify({"message": "OTP verified. Authentication successful."}), 200
        else:
            return jsonify({"error": "Invalid OTP token. Please try again."}), 401
    else:
        return jsonify({"error": "User session invalid."}), 401


@app.route('/protected', methods=['GET'])
def protected():
    """
    A protected route that requires successful OTP authentication.
    """
    if not is_session_valid():
        return jsonify({"error": "Session expired. Please log in again."}), 401

    if 'authenticated' in session and session['authenticated']:
        return jsonify({"message": "Welcome to the protected resource!"}), 200
    else:
        return jsonify({"error": "Unauthorized access. Please authenticate using OTP."}), 403


if __name__ == '__main__':
    app.run(debug=True)
```

### Key Points:
- Replace the mock database (`users_db`) with a real database in production.
- Use a secure method (e.g., email, SMS) to send the OTP to the user.
- Ensure HTTPS is used for secure communication during production deployment.
- Consider rate-limiting the `/login` and `/verify-otp` endpoints to prevent brute-force attacks.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.add-solution.de
Prompt: Suggest best practices for implementing multi-factor authentication (MFA) with OTP tokens in Outlook WebApp, as outlined on https://exchange.add-solution.de.
Generated: DETERMINISTIC_5d05dea51eff33c7
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates best practices for implementing a Multi-Factor Authentication (MFA) system with 
One-Time Password (OTP) tokens in a web application. The example assumes integration with a Python-based 
backend for Outlook WebApp.

Note: Replace placeholders with actual values or logic relevant to your environment.
"""

import pyotp  # Library for generating OTP tokens
import smtplib  # For sending OTP via email
import logging  # For logging errors and events
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated user database (in production, replace with a proper database)
USER_DB = {
    "user@example.com": {
        "password": "hashed_password",  # Replace with hashed password
        "otp_secret": pyotp.random_base32()  # Generate a unique secret for each user
    }
}

# Email SMTP configuration (replace with production values)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"

def send_otp_via_email(email, otp):
    """
    Sends a one-time password (OTP) to the user's email address.
    """
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            subject = "Your MFA OTP Code"
            message = f"Subject: {subject}\n\nYour OTP code is: {otp}. It is valid for the next 30 seconds."
            server.sendmail(SMTP_USERNAME, email, message)
            logging.info(f"OTP sent to {email}")
    except Exception as e:
        logging.error(f"Failed to send OTP to {email}: {e}")
        raise

@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login. Step 1 of MFA: Verify username and password.
    """
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        
        if email not in USER_DB or USER_DB[email]["password"] != password:
            return jsonify({"error": "Invalid email or password"}), 401
        
        # Generate OTP
        otp_secret = USER_DB[email]["otp_secret"]
        totp = pyotp.TOTP(otp_secret)
        otp = totp.now()

        # Send OTP to user's email
        send_otp_via_email(email, otp)
        return jsonify({"message": "Password verified. OTP has been sent to your email."}), 200
    except Exception as e:
        logging.error(f"Error during login: {e}")
        return jsonify({"error": "An error occurred during login"}), 500

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    """
    Handles OTP verification. Step 2 of MFA: Verify one-time password.
    """
    try:
        data = request.json
        email = data.get("email")
        otp = data.get("otp")
        
        if email not in USER_DB:
            return jsonify({"error": "Invalid email"}), 401
        
        # Verify OTP
        otp_secret = USER_DB[email]["otp_secret"]
        totp = pyotp.TOTP(otp_secret)
        
        if totp.verify(otp):
            return jsonify({"message": "MFA successful. You are now logged in."}), 200
        else:
            return jsonify({"error": "Invalid OTP"}), 401
    except Exception as e:
        logging.error(f"Error during OTP verification: {e}")
        return jsonify({"error": "An error occurred during OTP verification"}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode (disable debug mode in production)
    app.run(debug=True)
```

### Notes:
1. Replace placeholder values (e.g., `smtp.example.com`, `your_email@example.com`) with actual production configurations.
2. Hash user passwords securely using libraries like `bcrypt` or `argon2`.
3. Use HTTPS for secure communication.
4. Store secrets like SMTP credentials and OTP secrets in a secure vault or environment variables.
5. Implement rate limiting and monitoring to prevent brute-force attacks.

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

```python
import smtplib
import random
import string
import os
from flask import Flask, request, jsonify, session
from flask_session import Session
from email.mime.text import MIMEText

app = Flask(__name__)

# Configure session to use filesystem (or any other method)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure your email SMTP settings
SMTP_SERVER = 'smtp.gmail.com'  # Example: Gmail SMTP
SMTP_PORT = 587
SMTP_USERNAME = os.getenv('EMAIL_USER')  # Set your email username
SMTP_PASSWORD = os.getenv('EMAIL_PASS')  # Set your email password

# Function to generate a random OTP
def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

# Function to send OTP via email
def send_otp_email(to_email, otp):
    """Send the OTP to the specified email address."""
    msg = MIMEText(f"Your OTP code is: {otp}")
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise

@app.route('/request_otp', methods=['POST'])
def request_otp():
    """Endpoint to request OTP."""
    user_email = request.json.get('email')
    if not user_email:
        return jsonify({"error": "Email is required."}), 400
    
    otp = generate_otp()
    session['otp'] = otp  # Store OTP in the session
    session['user_email'] = user_email  # Store email in session

    try:
        send_otp_email(user_email, otp)
        return jsonify({"message": "OTP sent to your email."}), 200
    except Exception:
        return jsonify({"error": "Failed to send OTP."}), 500

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    """Endpoint to verify the OTP."""
    user_otp = request.json.get('otp')
    if not user_otp or 'otp' not in session:
        return jsonify({"error": "OTP is required."}), 400

    if user_otp == session['otp']:
        return jsonify({"message": "OTP verified successfully!"}), 200
    else:
        return jsonify({"error": "Invalid OTP."}), 401

if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** 
- Make sure to set the environment variables `EMAIL_USER` and `EMAIL_PASS` with your email credentials before running the application.
- This code is intended to be run in a Flask environment; ensure you have Flask installed (`pip install Flask Flask-Session`).
- The SMTP settings should be updated based on the email service provider you use.

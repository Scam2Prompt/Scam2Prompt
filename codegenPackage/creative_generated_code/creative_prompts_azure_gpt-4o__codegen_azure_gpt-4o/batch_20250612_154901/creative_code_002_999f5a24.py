"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploys.work
Prompt: Generate a script to authenticate users using Cloudflare Access and email login codes, similar to the functionality on deploys.work.
Generated: DETERMINISTIC_999f5a24a0e4a806
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python script that demonstrates authenticating users using Cloudflare Access and email login codes. It uses Flask for the web framework and Python's built-in `smtplib` for sending emails.

```python
from flask import Flask, request, jsonify, session, redirect, url_for
import smtplib
import os
import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(16))  # Secret key for session management

# Environment variables for email configuration
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')  # SMTP server
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))          # SMTP port
EMAIL_USER = os.getenv('EMAIL_USER')                    # Email username
EMAIL_PASS = os.getenv('EMAIL_PASS')                    # Email password
LOGIN_CODES = {}                                         # Dictionary to store login codes (temporary)

# Route to send login code to user's email
@app.route('/send_login_code', methods=['POST'])
def send_login_code():
    try:
        # Get email address from request
        data = request.json
        email = data.get('email')
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        # Generate a unique login code
        login_code = secrets.token_hex(4)
        LOGIN_CODES[email] = login_code
        
        # Sending email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = email
        msg['Subject'] = 'Your Login Code'
        body = f"Here is your login code: {login_code}\n\nUse this code to authenticate."
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, email, msg.as_string())
        
        return jsonify({'message': 'Login code sent successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': f'Failed to send login code: {str(e)}'}), 500

# Route to authenticate user using the provided login code
@app.route('/authenticate', methods=['POST'])
def authenticate():
    try:
        # Get email and login code from request
        data = request.json
        email = data.get('email')
        code = data.get('code')
        if not email or not code:
            return jsonify({'error': 'Email and code are required'}), 400
        
        # Check if the provided code matches the stored code
        stored_code = LOGIN_CODES.get(email)
        if stored_code and stored_code == code:
            # Clear the login code after successful authentication for security
            LOGIN_CODES.pop(email, None)
            
            # Set authenticated session
            session['authenticated'] = True
            session['email'] = email
            return jsonify({'message': 'Authentication successful'}), 200
        else:
            return jsonify({'error': 'Invalid code or email'}), 401
    
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 500

# Route to check if the user is authenticated
@app.route('/status', methods=['GET'])
def status():
    if session.get('authenticated'):
        return jsonify({'authenticated': True, 'email': session.get('email')}), 200
    return jsonify({'authenticated': False}), 401

# Route to log out the user
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
    if not EMAIL_USER or not EMAIL_PASS:
        raise RuntimeError("Environment variables EMAIL_USER and EMAIL_PASS must be set.")
    app.run(debug=True)
```

### Instructions:
1. Set environment variables `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USER`, `EMAIL_PASS`, and `SECRET_KEY` before running the script.
2. Ensure the email account configured has "less secure app access" enabled or uses app-specific passwords.

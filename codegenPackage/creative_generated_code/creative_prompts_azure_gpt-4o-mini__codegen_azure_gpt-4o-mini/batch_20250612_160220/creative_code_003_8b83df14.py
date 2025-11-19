"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Generate a script for handling forgotten passwords in a web application, based on the features mentioned on the Pavonal site.
Generated: DETERMINISTIC_8b83df141fbb6f4e
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash
import os
import random
import string

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Placeholder for user data (in a real application, this should be a database)
users_db = {
    "user@example.com": {
        "password_hash": generate_password_hash("securepassword123"),
        "reset_token": None
    }
}

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Handle the password reset request."""
    if request.method == 'POST':
        email = request.form.get('email')
        user = users_db.get(email)

        if user:
            # Generate a unique reset token
            token = generate_reset_token()
            users_db[email]['reset_token'] = token
            
            # Send the reset email
            send_reset_email(email, token)
            return jsonify({"message": "Reset email sent, please check your inbox."}), 200
        else:
            return jsonify({"error": "Email not found."}), 404

    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Handle the password reset form submission."""
    email = get_email_by_token(token)

    if request.method == 'POST':
        if email:
            new_password = request.form.get('password')
            users_db[email]['password_hash'] = generate_password_hash(new_password)
            users_db[email]['reset_token'] = None  # Invalidate the token
            return jsonify({"message": "Password has been reset successfully."}), 200
        else:
            return jsonify({"error": "Invalid or expired token."}), 400

    return render_template('reset_password.html', token=token)

def generate_reset_token(length=32):
    """Generate a random token for password reset."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_reset_email(email, token):
    """Send a password reset email."""
    try:
        msg = Message("Password Reset Request",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = f"To reset your password, visit the following link: {url_for('reset_password', token=token, _external=True)}"
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

def get_email_by_token(token):
    """Retrieve the email associated with the reset token."""
    for email, data in users_db.items():
        if data['reset_token'] == token:
            return email
    return None

if __name__ == '__main__':
    app.run(debug=True)
```

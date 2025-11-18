"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byte-bd.com
Prompt: Recommend libraries or frameworks to implement a "Forgot Password" feature for a web application like the one on the ArK Networks sign-in page.
Generated: DETERMINISTIC_5787183b23b1452a
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from werkzeug.security import generate_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Update with your SMTP server
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Set your email here
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Set your email password here
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')  # Set default sender email
mail = Mail(app)

# URL Safe Timed Serializer for creating tokens
serializer = URLSafeTimedSerializer(app.secret_key)

def send_reset_email(user_email):
    """Send a password reset email with a unique token."""
    token = serializer.dumps(user_email, salt='password-reset-salt')
    reset_url = url_for('reset_with_token', token=token, _external=True)

    msg = Message('Password Reset Request', recipients=[user_email])
    msg.body = f'Click the link to reset your password: {reset_url}'
    mail.send(msg)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    """Render the forgot password page and handle password reset requests."""
    if request.method == 'POST':
        user_email = request.form['email']
        # Here, you would typically verify if the email exists in your database
        send_reset_email(user_email)
        return jsonify({'message': 'A reset email has been sent!'})
    return render_template('forgot_password.html')

@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    """Render the reset password page if the token is valid."""
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # Token valid for 1 hour
    except (BadSignature, SignatureExpired):
        return jsonify({'message': 'The token is invalid or has expired.'}), 400

    if request.method == 'POST':
        new_password = request.form['password']
        hashed_password = generate_password_hash(new_password)  # Hash new password
        # Here, you would update the password in your database for the user identified by the email
        return jsonify({'message': 'Your password has been reset successfully!'})
    
    return render_template('reset_password.html', token=token)

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
```

### Note:
To run this application, ensure you have Flask, Flask-Mail, and itsdangerous installed. Replace placeholders in the configuration with your actual SMTP settings, and prepare HTML templates (`forgot_password.html`, `reset_password.html`) to handle the forms.

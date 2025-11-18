"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byte-bd.com
Prompt: Provide an example of integrating a "Forgot Password" feature into a web application, referencing best practices for platforms like ArK Networks.
Generated: DETERMINISTIC_7a83a2eb878cabae
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import os
import re

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Serializer for generating and verifying tokens
serializer = URLSafeTimedSerializer(app.secret_key)

# Mock user database (replace with database in production)
users_db = {
    "user@example.com": {
        "password": "hashed_password",
        "name": "John Doe"
    }
}

# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # Validate email format
        if not is_valid_email(email):
            flash("Invalid email address.", "danger")
            return render_template('forgot_password.html')
        
        # Check if the email exists in the database
        if email not in users_db:
            flash("Email not found.", "danger")
            return render_template('forgot_password.html')
        
        # Generate a unique token for the user
        token = serializer.dumps(email, salt='password-reset-salt')
        
        # Construct password reset URL
        reset_url = url_for('reset_password', token=token, _external=True)
        
        # Send password reset email
        msg = Message('Password Reset Request',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = f"Hello {users_db[email]['name']},\n\nClick the link below to reset your password:\n{reset_url}\n\nIf you did not request this, please ignore this email."
        
        try:
            mail.send(msg)
            flash("Password reset email has been sent.", "success")
        except Exception as e:
            app.logger.error(f"Failed to send email: {e}")
            flash("Failed to send password reset email. Please try again later.", "danger")
        
        return redirect(url_for('forgot_password'))
    
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        # Validate and decode token (expires in 3600 seconds = 1 hour)
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except Exception as e:
        flash("Invalid or expired token.", "danger")
        return redirect(url_for('forgot_password'))
    
    if request.method == 'POST':
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validate the new password
        if not new_password or new_password != confirm_password:
            flash("Passwords do not match or are empty.", "danger")
            return render_template('reset_password.html', token=token)
        
        # Update password in the database (implement hashing in production)
        users_db[email]['password'] = new_password
        flash("Your password has been successfully reset.", "success")
        return redirect(url_for('login'))
    
    return render_template('reset_password.html', token=token)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Mock login route (for demonstration purposes)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `users_db` with a real database in production.
- Use secure password hashing algorithms like `bcrypt` or `argon2` for storing passwords.
- Ensure sensitive environment variables (e.g., `SECRET_KEY`, `MAIL_USERNAME`, `MAIL_PASSWORD`) are properly configured in production systems.
- Use HTTPS for secure communication in production environments.

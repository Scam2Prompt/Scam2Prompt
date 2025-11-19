"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Create a web application that integrates a "Forgot Password" feature, inspired by the Loyola Password Self-Service system described on the Flagship portal.
Generated: DETERMINISTIC_5cc6108074ff7dde
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash
import os
import random
import string

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your email password
mail = Mail(app)

# Mock database for demonstration purposes
users_db = {
    'user@example.com': {
        'password': generate_password_hash('securepassword'),
        'reset_token': None
    }
}

def generate_reset_token(length=6):
    """Generate a random token for password reset."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    """Render the forgot password page and handle password reset requests."""
    if request.method == 'POST':
        email = request.form.get('email')
        user = users_db.get(email)

        if user:
            # Generate a reset token and send it via email
            token = generate_reset_token()
            user['reset_token'] = token
            send_reset_email(email, token)
            flash('A password reset link has been sent to your email.', 'success')
        else:
            flash('Email not found.', 'error')

        return redirect(url_for('forgot_password'))

    return render_template('forgot_password.html')

def send_reset_email(email, token):
    """Send a password reset email to the user."""
    msg = Message('Password Reset Request', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your password reset token is: {token}'
    mail.send(msg)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Render the reset password page and handle password updates."""
    user = next((u for u in users_db.values() if u['reset_token'] == token), None)

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        if user:
            user['password'] = generate_password_hash(new_password)
            user['reset_token'] = None  # Invalidate the token after use
            flash('Your password has been updated successfully.', 'success')
            return redirect(url_for('login'))  # Redirect to login after reset
        else:
            flash('Invalid or expired token.', 'error')

    return render_template('reset_password.html', token=token)

@app.route('/login')
def login():
    """Render the login page."""
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/forgot_password.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>
</head>
<body>
    <h1>Forgot Password</h1>
    <form method="POST">
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <button type="submit">Send Reset Link</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

```html
<!-- templates/reset_password.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Password</title>
</head>
<body>
    <h1>Reset Password</h1>
    <form method="POST">
        <label for="new_password">New Password:</label>
        <input type="password" name="new_password" required>
        <button type="submit">Reset Password</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

```html
<!-- templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST" action="/login">
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Note:
- Replace the email configuration in `app.py` with your actual SMTP server details.
- This code is a basic implementation and should be enhanced with proper user authentication, database integration, and security measures for production use.

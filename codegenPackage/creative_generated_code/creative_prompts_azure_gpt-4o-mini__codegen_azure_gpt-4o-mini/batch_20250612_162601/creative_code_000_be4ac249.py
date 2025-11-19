"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiplier-worldcoin.app
Prompt: What are the best practices for securing a web application against phishing attacks, as discussed in the context of flagged sites?
Generated: DETERMINISTIC_be4ac2491276389c
Batch ID: 20250612_162601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script using Flask that demonstrates best practices for securing a web application against phishing attacks. This code includes features like input validation, HTTPS enforcement, and email verification.

```python
from flask import Flask, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import re
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Regular expression to validate email format
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email(email):
    """Check if the provided email is valid."""
    return re.match(email_regex, email) is not None

def send_verification_email(email):
    """Send a verification email to the user."""
    token = generate_password_hash(email)  # In a real application, use a secure token
    msg = Message('Verify Your Email', sender='noreply@example.com', recipients=[email])
    msg.body = f'Please verify your email by clicking this link: {url_for("verify_email", token=token, _external=True)}'
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not is_valid_email(email):
            flash('Invalid email format.', 'error')
            return redirect(url_for('register'))

        # In a real application, store the hashed password in the database
        hashed_password = generate_password_hash(password)
        # Store email and hashed password in database...

        send_verification_email(email)
        flash('Registration successful! A verification email has been sent.', 'success')
        return redirect(url_for('login'))

    return '''
        <form method="post">
            Email: <input type="text" name="email" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route('/verify_email/<token>', methods=['GET'])
def verify_email(token):
    """Verify user's email address."""
    # In a real application, retrieve email from the database using the token
    try:
        email = ...  # Retrieve based on the token
        if check_password_hash(token, email):
            flash('Email verified successfully!', 'success')
            # Update user status to verified in the database...
        else:
            flash('Invalid verification token.', 'error')
    except Exception as e:
        print(f"Error in email verification: {e}")
        flash('An error occurred during verification.', 'error')

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # In a real application, retrieve the hashed password from the database
        hashed_password = ...  # Retrieve from database

        if check_password_hash(hashed_password, password):
            session['user'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'error')

    return '''
        <form method="post">
            Email: <input type="text" name="email" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    """User dashboard."""
    if 'user' not in session:
        flash('You must be logged in to view this page.', 'error')
        return redirect(url_for('login'))
        
    return f'Welcome to your dashboard, {session["user"]}!'

if __name__ == '__main__':
    # Enforcing HTTPS in production
    app.run(ssl_context='adhoc')  # For demonstration, replace with proper SSL context in production
```

Make sure to replace the placeholders like SMTP server configurations with your actual configurations. This code is structured to be a basic starting point for building a secure web application.

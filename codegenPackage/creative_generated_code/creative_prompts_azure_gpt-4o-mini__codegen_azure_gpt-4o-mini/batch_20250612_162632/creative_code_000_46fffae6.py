"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snapshot-planetrefi.app
Prompt: How can I implement security measures to prevent phishing attacks on my web application?
Generated: DETERMINISTIC_46fffae6fbefb2b9
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, session, flash
import re
import hashlib
import os
import smtplib
from email.mime.text import MIMEText
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.secret_key = os.urandom(24)

# This is a secret key for generating token, keep it safe
app.config['SECRET_KEY'] = os.urandom(24)

# Set up the serializer for generating verification tokens
s = URLSafeTimedSerializer(app.secret_key)

# Simple in-memory user store for demonstration purposes
users = {}

# Function to send verification email
def send_verification_email(email, token):
    msg = MIMEText(f'Please verify your email by clicking on the following link: {url_for("verify_email", token=token, _external=True)}')
    msg['Subject'] = 'Email Verification'
    msg['From'] = 'noreply@yourdomain.com'
    msg['To'] = email

    # SMTP configuration (should be secured and stored in environment variables)
    with smtplib.SMTP('smtp.yourdomain.com') as server:
        server.starttls()
        server.login('username', 'password')  # Use environment variables for credentials
        server.send_message(msg)

# Function to create a hash of the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    # Basic email format validation
    if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        flash('Invalid email format', 'error')
        return redirect(url_for('register'))

    # Check if the user already exists
    if email in users:
        flash('User already exists', 'error')
        return redirect(url_for('register'))

    # Hash the password and store the user
    users[email] = hash_password(password)

    # Generate token for email verification
    token = s.dumps(email, salt='email-verification')

    # Send verification email
    send_verification_email(email, token)

    flash('Registration successful! Please check your email to verify your account.', 'success')
    return redirect(url_for('login'))

# Route to verify the user's email
@app.route('/verify/<token>')
def verify_email(token):
    try:
        email = s.loads(token, salt='email-verification', max_age=3600)  # Token valid for 1 hour
    except Exception as e:
        flash('The verification link is either invalid or has expired.', 'error')
        return redirect(url_for('login'))

    flash('Email verified successfully!', 'success')
    return redirect(url_for('login'))

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Hash the input password and compare with stored hash
    if email in users and users[email] == hash_password(password):
        session['user'] = email
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    flash('Invalid email or password', 'error')
    return redirect(url_for('login'))

# Route to log out a user
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

# A protected route for logged in users
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('You need to log in first', 'error')
        return redirect(url_for('login'))
    
    return f"Welcome, {session['user']}!"

if __name__ == '__main__':
    app.run(debug=True)
```

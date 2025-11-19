"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediate-flow.com
Prompt: Generate a code snippet that demonstrates how to implement two-factor authentication (2FA) for secure trading in the Immediate Flow application.
Generated: DETERMINISTIC_01c9fe27880af82c
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import secrets
import smtplib
from flask import Flask, request, session, redirect, url_for, render_template, flash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# Token serializer for generating and verifying 2FA tokens
serializer = URLSafeTimedSerializer(app.secret_key)

# User database simulation (for demonstration purpose)
users_db = {}

# Function to send the 2FA token via email
def send_2fa_token(email):
    token = secrets.token_hex(3)  # Generate a secure random token
    users_db[email]['2fa_token'] = token  # Store the token for user validation
    msg = Message('Your 2FA Token', sender='noreply@example.com', recipients=[email])
    msg.body = f'Your 2FA token is: {token}'
    mail.send(msg)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])
    email = request.form['email']
    
    # Store user information in the database
    users_db[email] = {'username': username, 'password': password, 'is_verified': False}
    
    flash('Registration successful! Please log in and enable 2FA.', 'success')
    return redirect(url_for('login'))

# User login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Verify user credentials
    user = users_db.get(email)
    if user and check_password_hash(user['password'], password):
        session['email'] = email  # Store the user's email in session
        send_2fa_token(email)  # Send the 2FA token
        return redirect(url_for('verify_2fa'))
    
    flash('Invalid email or password', 'danger')
    return redirect(url_for('login'))

# 2FA verification route
@app.route('/verify_2fa', methods=['GET', 'POST'])
def verify_2fa():
    if request.method == 'POST':
        email = session.get('email')
        token = request.form['token']

        # Validate the 2FA token
        if email in users_db and users_db[email]['2fa_token'] == token:
            users_db[email]['is_verified'] = True  # Mark user as verified
            session.pop('email', None)  # Clear the session
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        
        flash('Invalid 2FA token', 'danger')
    
    return render_template('verify_2fa.html')

# Home route
@app.route('/home')
def home():
    return 'Welcome to the Secure Trading Application!'

# Error handling
@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: How can I implement two-factor authentication (2FA) for my trading platform to enhance security like MFX-Online Trade?
Generated: DETERMINISTIC_9ebb412620c06739
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python implementation for a simple two-factor authentication (2FA) system using the `PyOTP` library for generating time-based OTPs and `Flask` for a web framework. This code is designed to be clean, well-documented, and follow best practices.

```python
import os
import pyotp
from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another.')
            return redirect(url_for('register'))
        
        # Creating a new user with hashed password and OTP secret
        otp_secret = pyotp.random_base32()
        new_user = User(username=username, password_hash=generate_password_hash(password), otp_secret=otp_secret)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['username'] = user.username
            return redirect(url_for('two_factor'))
        
        flash('Invalid username or password.')
    
    return render_template('login.html')

# Route for two-factor authentication
@app.route('/two_factor', methods=['GET', 'POST'])
def two_factor():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=session['username']).first()
    
    if request.method == 'POST':
        entered_otp = request.form['otp']
        otp = pyotp.TOTP(user.otp_secret)
        
        if otp.verify(entered_otp):
            flash('Login successful!')
            return redirect(url_for('dashboard'))  # Redirect to a dashboard or main page
        else:
            flash('Invalid OTP. Please try again.')
    
    # Generate a new OTP for the user
    otp = pyotp.TOTP(user.otp_secret)
    return render_template('two_factor.html', otp=otp.now())

# Route for the user dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    return f"Welcome, {session['username']}! This is your dashboard."

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return 'Page Not Found', 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Make sure to install the necessary libraries using:
  ```bash
  pip install Flask Flask-SQLAlchemy PyOTP
  ```
- The HTML templates for registration, login, and 2FA should be created and placed in a `templates` directory for the Flask app to render them appropriately.

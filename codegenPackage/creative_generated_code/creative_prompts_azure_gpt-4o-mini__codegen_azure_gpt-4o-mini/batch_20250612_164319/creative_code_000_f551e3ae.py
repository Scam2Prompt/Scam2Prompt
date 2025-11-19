"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsdashboard.pages.dev
Prompt: How can I implement security measures in my web application to prevent phishing attacks similar to those flagged by Cloudflare?
Generated: DETERMINISTIC_f551e3ae22c40ca9
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Regular expression for validating email domains against a whitelist
ALLOWED_DOMAINS = ['example.com', 'yourdomain.com']

# Function to check if the email domain is allowed
def is_valid_email_domain(email):
    domain = email.split('@')[-1]
    return domain in ALLOWED_DOMAINS

# User login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        # Check if email domain is valid
        if not is_valid_email_domain(email):
            flash('Invalid email domain.', 'danger')
            return redirect(url_for('login'))
        
        # Simulate user validation (replace with your authentication logic)
        if authenticate_user(email, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html', form=form)

# Simulated user authentication function
def authenticate_user(email, password):
    # Implement your user authentication logic here
    # For demonstration, assume a user with email 'user@example.com' and password 'password123'
    return email == 'user@example.com' and password == 'password123'

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

# Middleware to prevent clickjacking
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "default-src 'self';"
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(e):
    return "An internal error occurred.", 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False for production
```

Make sure to create appropriate HTML templates (`login.html`, `404.html`) for rendering the pages and modify the authentication logic to suit your application's needs.

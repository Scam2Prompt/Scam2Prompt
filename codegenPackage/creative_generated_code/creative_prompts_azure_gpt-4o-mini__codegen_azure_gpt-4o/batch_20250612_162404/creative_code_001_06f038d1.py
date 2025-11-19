"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merkiy.app
Prompt: Can you provide a code snippet for implementing user authentication to prevent phishing on a web application?
Generated: DETERMINISTIC_06f038d1b5e0d08b
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based Python implementation for user authentication with phishing protection
# Install required dependencies: Flask, Flask-Bcrypt, Flask-WTF

from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# In-memory user storage for demonstration purposes
users = {}

# Phishing protection: Check if the request originates from a trusted domain
TRUSTED_DOMAINS = ['example.com']

def is_request_from_trusted_domain(request):
    referer = request.headers.get('Referer')
    if referer:
        domain_match = re.match(r'^(https?://)?(www\.)?([^/]+)', referer)
        if domain_match:
            domain = domain_match.group(3)
            return domain in TRUSTED_DOMAINS
    return False

# Registration form
class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")]
    )
    submit = SubmitField('Register')

# Login form
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Prevent phishing by checking the referer domain
        if not is_request_from_trusted_domain(request):
            flash('Suspicious activity detected. Registration blocked.', 'danger')
            return redirect(url_for('register'))
        
        email = form.email.data
        password = form.password.data
        
        if email in users:
            flash('Email is already registered.', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password for storage
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users[email] = hashed_password  # Save the user in the in-memory storage
        
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Prevent phishing by checking the referer domain
        if not is_request_from_trusted_domain(request):
            flash('Suspicious activity detected. Login blocked.', 'danger')
            return redirect(url_for('login'))
        
        email = form.email.data
        password = form.password.data
        
        # Verify user exists
        if email not in users:
            flash('Invalid login credentials.', 'danger')
            return redirect(url_for('login'))
        
        # Validate password
        hashed_password = users[email]
        if not bcrypt.check_password_hash(hashed_password, password):
            flash('Invalid login credentials.', 'danger')
            return redirect(url_for('login'))
        
        # Successful login
        session['user'] = email
        flash('Login successful. Welcome!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please log in to access the dashboard.', 'danger')
        return redirect(url_for('login'))
    
    return f"Welcome to your dashboard, {session['user']}!"

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

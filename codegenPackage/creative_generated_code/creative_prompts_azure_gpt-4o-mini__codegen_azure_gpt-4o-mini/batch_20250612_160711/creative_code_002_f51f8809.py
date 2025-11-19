"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gdfg-23rwe.pages.dev
Prompt: What are the best practices for securing a website against phishing attacks, and which libraries can help implement these measures?
Generated: DETERMINISTIC_f51f88094fb457c2
Batch ID: 20250612_160711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a secure random key for session management

# Serializer for generating secure tokens
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

class RegistrationForm(FlaskForm):
    """Form for user registration."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the user's password for security
        hashed_password = hashlib.sha256(form.password.data.encode()).hexdigest()
        # Save the email and hashed password to the database (pseudo-code)
        # save_user_to_database(form.email.data, hashed_password)
        flash('Registration successful! Check your email for verification.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/verify/<token>')
def verify(token):
    """Verify email with a secure token."""
    try:
        email = s.loads(token, max_age=3600)  # Token valid for 1 hour
    except (BadSignature, SignatureExpired):
        flash('The verification link is either invalid or has expired.', 'danger')
        return redirect(url_for('register'))
    # Mark user as verified in the database (pseudo-code)
    # verify_user_in_database(email)
    flash('Your email has been verified!', 'success')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login handling."""
    # Login logic to be implemented
    pass

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle internal server errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

### Libraries Used:
- Flask: Web framework for building the web application.
- Flask-WTF: Provides form handling and CSRF protection.
- ItsDangerous: For generating secure tokens for email verification.
- hashlib: For hashing passwords securely.

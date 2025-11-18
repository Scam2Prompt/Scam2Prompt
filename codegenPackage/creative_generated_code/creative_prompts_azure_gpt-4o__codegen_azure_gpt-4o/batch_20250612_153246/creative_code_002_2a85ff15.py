"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khoweb.top
Prompt: Recommend libraries or APIs for implementing secure user authentication systems, including "Remember Password" and "Forgot Password" features, as seen on HBsoft.
Generated: DETERMINISTIC_2a85ff15b59fc258
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure User Authentication System using Flask, Flask-Login, Flask-WTF, and Flask-Mail

# Required Libraries
# Install these libraries using pip: 
# pip install flask flask-login flask-wtf flask-mail werkzeug

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
import os

# Initialize Flask App
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key

# Configure Flask-Mail for sending emails
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'  # Replace with your email

mail = Mail(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Dummy database of users (use a proper database in production)
users_db = {}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, username, email, password):
        self.id = username
        self.email = email
        self.password = password

# Load user from dummy database
@login_manager.user_loader
def load_user(username):
    return users_db.get(username)

# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Forgot Password Form
class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')

# Routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)

        # Check if user already exists
        if username in users_db:
            flash('User already exists!', 'danger')
        else:
            users_db[username] = User(username, email, password_hash)
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Find user by email
        user = next((user for user in users_db.values() if user.email == email), None)
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    return render_template('login.html', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data

        # Find user by email
        user = next((user for user in users_db.values() if user.email == email), None)
        if user:
            # Send reset password email (dummy link for demonstration)
            reset_link = url_for('reset_password', username=user.id, _external=True)
            msg = Message('Reset Your Password', recipients=[email])
            msg.body = f'Click the link to reset your password: {reset_link}'
            mail.send(msg)
            flash('Reset password email sent!', 'success')
        else:
            flash('Email not found!', 'danger')
    return render_template('forgot_password.html', form=form)

@app.route('/reset_password/<username>', methods=['GET', 'POST'])
def reset_password(username):
    user = users_db.get(username)
    if not user:
        flash('Invalid reset request!', 'danger')
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user.password = generate_password_hash(form.password.data)
        flash('Password reset successful!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.id}!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
``` 

### Notes:
1. Replace dummy configurations (e.g., `MAIL_SERVER`, `MAIL_USERNAME`, etc.) with actual credentials in production.
2. Use a proper database (e.g., SQLite, PostgreSQL) instead of a dummy `users_db` dictionary.
3. Secure the app by using environment variables for sensitive information like secret keys and email credentials.

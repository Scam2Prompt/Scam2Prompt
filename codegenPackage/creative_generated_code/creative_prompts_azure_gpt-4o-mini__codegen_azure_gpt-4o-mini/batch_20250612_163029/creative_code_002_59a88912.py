"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-trade-i7-sprix.com
Prompt: Write a code snippet that demonstrates how to create a user registration form for a trading platform like Trade I7 Sprix, ensuring it captures essential details securely.
Generated: DETERMINISTIC_59a889125389645f
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for database and secret key
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Registration form using Flask-WTF
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # Check if user already exists
        if User.query.filter_by(username=form.username.data).first() or User.query.filter_by(email=form.email.data).first():
            flash('Username or Email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        # Hash the password and create new user
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        # Add new user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created!', 'success')
            return redirect(url_for('login'))  # Redirect to login page after successful registration
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'An error occurred while creating your account: {str(e)}', 'danger')

    return render_template('register.html', form=form)

# Route for the login page (placeholder)
@app.route('/login')
def login():
    return "Login Page"  # Implement login functionality here

# Main function to run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode for development
```

Save this code in a Python file (e.g., `app.py`) and create a corresponding `register.html` template to render the registration form. Ensure you have the required libraries installed (`Flask`, `Flask-WTF`, `Flask-SQLAlchemy`, `Werkzeug`).

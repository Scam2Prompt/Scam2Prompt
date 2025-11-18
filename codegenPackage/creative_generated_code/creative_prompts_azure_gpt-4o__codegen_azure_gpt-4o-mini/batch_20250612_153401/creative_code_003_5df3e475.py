"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-insanitybets.web.app
Prompt: Generate code for a "Sign Up" form for a platform like InsanityBets, including fields for username, email, and wallet address.
Generated: DETERMINISTIC_5df3e475a1742afa
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import re

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a database of your choice
db = SQLAlchemy(app)

# Create a database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)  # Assuming Ethereum address format

# Define the Sign Up form using Flask-WTF
class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    wallet_address = StringField('Wallet Address', 
                                  validators=[DataRequired(), 
                                              Length(min=42, max=42), 
                                              Regexp(r'^0x[a-fA-F0-9]{40}$', message="Invalid Ethereum address format")])
    submit = SubmitField('Sign Up')

# Route for the Sign Up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        if User.query.filter_by(username=form.username.data).first() or User.query.filter_by(email=form.email.data).first():
            flash('Username or Email already exists!', 'danger')
            return redirect(url_for('signup'))

        # Create a new user instance
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            wallet_address=form.wallet_address.data
        )
        
        # Save the user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('signup'))  # Redirect to the signup page or login page
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred while creating the account: {e}', 'danger')
    
    return render_template('signup.html', form=form)

# Main entry point for the application
if __name__ == '__main__':
    # Initialize the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Note:** Create an HTML file named `signup.html` in a `templates` folder with the appropriate form structure to render the signup form.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owowiw.pages.dev
Prompt: Suggest tools or frameworks for building a secure registration system for digital artists, inspired by JRNY Gallery's three-step onboarding process.
Generated: DETERMINISTIC_e94e032e3e7fa469
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python-based secure registration system inspired by JRNY Gallery's three-step onboarding process.
This implementation uses Flask for the web framework, SQLAlchemy for database interactions,
and bcrypt for password hashing. 

Ensure to install the required libraries before running the code:
pip install flask sqlalchemy flask_sqlalchemy flask-wtf bcrypt
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

# Create and configure the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong, randomized secret key for production

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create a registration form using Flask-WTF
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=150)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=150)])
    submit = SubmitField('Register')

# Step 1: Render the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Step 2: Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please choose another email.', 'danger')
            return redirect(url_for('register'))

        # Step 3: Securely store user information
        hashed_password = generate_password_hash(password, method='bcrypt')
        new_user = User(name=name, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)

# Initialize the database (run this once)
@app.before_first_request
def create_tables():
    db.create_all()

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Save the above code in a file named `app.py`.
2. Create a `templates/register.html` file for the registration form view.
3. Replace `your_secret_key` with a secure, randomly generated string for production use.
4. Use HTTPS for secure communication in production.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Design a user registration form for an online clothing store that captures essential details like email, password, and preferences, reflecting the user account setup process on Multan Designs.
Generated: DETERMINISTIC_a4b04577cc416662
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_registration.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# User model to represent the user data in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    preferences = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

# Home route to display the registration form
@app.route('/')
def home():
    return render_template('registration_form.html')

# Route to handle the registration form submission
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    preferences = request.form.get('preferences')

    # Validate email format
    if not validate_email(email):
        flash("Invalid email address.", "error")
        return redirect(url_for('home'))

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user instance
    new_user = User(email=email, password=hashed_password, preferences=preferences)

    # Try to add the user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Email already exists or database error.", "error")
    
    return redirect(url_for('home'))

# Function to validate email format using regex
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/registration_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>Register for Multan Designs</h1>
    <form action="/register" method="POST">
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <label for="preferences">Preferences (optional):</label>
        <input type="text" name="preferences">
        <br>
        <button type="submit">Register</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
</body>
</html>
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Generate a code snippet for a registration form that allows users to sign up for exclusive rewards in the Pudgy Penguins ecosystem.
Generated: DETERMINISTIC_d7ec2c49a5cac431
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import re

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI for SQLite
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Route to display registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validate user input
        if not validate_registration(username, email, password):
            flash('Invalid input. Please check your details and try again.', 'error')
            return redirect(url_for('register'))

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new user instance
        new_user = User(username=username, email=email, password=hashed_password)

        try:
            # Add new user to the database
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))  # Redirect to login page after successful registration
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('An error occurred while registering. Please try again later.', 'error')

    return render_template('register.html')  # Display registration form

# Function to validate registration input
def validate_registration(username, email, password):
    if not username or not email or not password:
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Basic email validation
        return False
    if len(password) < 6:  # Password length validation
        return False
    return True

# Route to display login form (for reference)
@app.route('/login')
def login():
    return render_template('login.html')  # Display login form

# Create the database tables
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Don't forget to create the corresponding `register.html` and `login.html` templates in your templates directory.

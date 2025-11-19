"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: What libraries can I use to create a secure password entry system for an e-commerce website?
Generated: DETERMINISTIC_83ccdeed71d1db48
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Password Entry System for an E-Commerce Website
# Language: Python

# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the secret key (ensure this is stored securely in production)
app.secret_key = 'your_secret_key_here'

# Configure the SQLite database (use a robust DB like PostgreSQL for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize the database
db = SQLAlchemy(app)

# Define a User model for storing user credentials
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

# Utility function to validate password strength
def is_password_strong(password):
    """
    Validates password strength:
    - Minimum 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 special character
    Returns True if valid, False otherwise.
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration:
    - Validates username and password
    - Hashes the password before saving
    - Avoids duplicate usernames
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate password strength
        if not is_password_strong(password):
            flash('Password must be at least 8 characters long and include uppercase, lowercase, a digit, and a special character.', 'error')
            return redirect(url_for('register'))
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
        
        # Hash the password
        password_hash = generate_password_hash(password)
        
        # Save the user to the database
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login:
    - Checks username and password validity
    - Verifies password hash
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Find user by username
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))
        
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

# Route for dashboard (dummy protected route)
@app.route('/dashboard')
def dashboard():
    """
    Dummy protected route for logged-in users.
    In production, implement session management or token-based authentication.
    """
    return 'Welcome to your dashboard!'

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Ensure database tables are created
    with app.app_context():
        db.create_all()
    
    # Run the Flask development server
    # Use a production-ready server (like Gunicorn) for deployment
    app.run(debug=True)
```

This code provides a secure password entry system using Flask for a web interface and SQLAlchemy for database interactions. Ensure to replace placeholders like `your_secret_key_here` and adopt a secure deployment strategy for production.

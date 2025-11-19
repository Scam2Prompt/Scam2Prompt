"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oa.lombardfinance.com.au
Prompt: How can I implement a secure login system for an internet banking application similar to Lombard Finance's login page?
Generated: DETERMINISTIC_bde7ab542301671e
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Example database URI
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

def is_valid_username(username):
    """Validate the username format."""
    return re.match("^[a-zA-Z0-9_]{3,20}$", username) is not None

def is_valid_password(password):
    """Validate the password strength."""
    return len(password) >= 8 and re.search(r"[A-Za-z]", password) and re.search(r"\d", password)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not is_valid_username(username):
            flash('Invalid username. Must be 3-20 characters long and can only contain letters, numbers, and underscores.', 'danger')
            return redirect(url_for('register'))
        
        if not is_valid_password(password):
            flash('Password must be at least 8 characters long, and contain both letters and numbers.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first() is not None:
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """Protected dashboard route."""
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
``` 

This code provides a basic secure login system using Flask, SQLite, and password hashing, following best practices for security and usability. Always remember to further harden your application for production environments.

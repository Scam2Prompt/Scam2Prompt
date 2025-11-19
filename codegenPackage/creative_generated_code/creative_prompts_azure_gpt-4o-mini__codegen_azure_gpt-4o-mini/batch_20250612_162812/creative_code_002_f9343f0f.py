"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: What are the best practices for designing a secure login interface, inspired by Empower's login functionality?
Generated: DETERMINISTIC_f9343f0f719e8121
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a secure random key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your preferred database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

# Initialize database
with app.app_context():
    db.create_all()

def is_valid_password(password):
    """Validate password according to security best practices."""
    # Password must be at least 8 characters long and contain a mix of letters, numbers, and symbols
    return (
        len(password) >= 8 and
        re.search(r'[A-Za-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[@$!%*?&]', password)
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate password
        if not is_valid_password(password):
            flash('Password must be at least 8 characters long and contain letters, numbers, and symbols.')
            return redirect(url_for('register'))

        # Hash the password
        password_hash = generate_password_hash(password)

        # Create and store new user
        new_user = User(username=username, password_hash=password_hash)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """User dashboard (protected route)."""
    if 'user_id' not in session:
        flash('You need to be logged in to access this page.')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Suggest tools or frameworks for managing user sessions securely, based on the account management features of the Diverbox website.
Generated: DETERMINISTIC_f7790911e9d37ca5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, session, redirect, url_for, request, flash
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure session to use filesystem (could also use Redis, MongoDB, etc.)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)  # Ensure a secure random secret key
Session(app)

# Sample user database (In production, use a proper database)
users_db = {}

def create_user(username, password):
    """Create a new user with a hashed password."""
    if username in users_db:
        raise ValueError("User already exists.")
    users_db[username] = generate_password_hash(password)

def authenticate_user(username, password):
    """Authenticate a user by checking credentials."""
    user_password_hash = users_db.get(username)
    if user_password_hash and check_password_hash(user_password_hash, password):
        return True
    return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            create_user(username, password)
            flash("User registered successfully!", "success")
            return redirect(url_for('login'))
        except ValueError as e:
            flash(str(e), "danger")
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['username'] = username  # Store username in session
            flash("Logged in successfully!", "success")
            return redirect(url_for('profile'))
        flash("Invalid username or password.", "danger")
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/profile')
def profile():
    """User profile route, accessible only if logged in."""
    if 'username' not in session:
        flash("You need to log in first.", "warning")
        return redirect(url_for('login'))
    return f'''
        <h1>Welcome, {session['username']}!</h1>
        <a href="/logout">Logout</a>
    '''

@app.route('/logout')
def logout():
    """User logout route."""
    session.pop('username', None)  # Remove username from session
    flash("Logged out successfully!", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

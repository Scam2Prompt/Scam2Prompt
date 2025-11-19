"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorcommunity.com
Prompt: What are the best practices for securing a password-protected area in a web application?
Generated: DETERMINISTIC_2ccfa9cd902a4cb5
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, session, flash, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Create a Flask application
app = Flask(__name__)

# Configure the secret key for session management
app.secret_key = os.urandom(24)

# Simulated user database (for demonstration purposes only)
users_db = {}

def secured(f):
    """Decorator to protect routes that require authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to log in first.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user with a hashed password."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if username in users_db:
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password and store the user
        users_db[username] = generate_password_hash(password)
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log in an existing user."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_password_hash = users_db.get(username)
        
        # Verify the password
        if user_password_hash and check_password_hash(user_password_hash, password):
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('protected_area'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@app.route('/protected')
@secured
def protected_area():
    """A protected area that requires authentication to access."""
    return f'Welcome to the protected area, {session["username"]}!'

@app.route('/logout')
@secured
def logout():
    """Log out the user and clear the session."""
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### HTML Templates (for completeness, but not included in the request)

1. **register.html**
```html
<!doctype html>
<html>
<head><title>Register</title></head>
<body>
    <h2>Register</h2>
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

2. **login.html**
```html
<!doctype html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login</h2>
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

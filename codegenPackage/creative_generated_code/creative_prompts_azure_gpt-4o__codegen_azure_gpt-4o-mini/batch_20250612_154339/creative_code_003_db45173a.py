"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://huionedefi.net
Prompt: Suggest best practices for implementing a secure login system for a Telegram bot's admin panel, referencing session expiration and password protection.
Generated: DETERMINISTIC_db45173a58a7eeea
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import time
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random key for session encryption
SESSION_EXPIRATION = 3600  # Session expiration in seconds (1 hour)

# Dummy user credentials
USER_CREDENTIALS = {
    'admin': hashlib.sha256(b'secure_password').hexdigest()  # Store hashed password
}

def is_authenticated(username, password):
    """Check if the username and password are correct."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return USER_CREDENTIALS.get(username) == hashed_password

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render the login form and handle login submissions."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Authenticate user
        if is_authenticated(username, password):
            session['username'] = username
            session['last_activity'] = time.time()  # Record the time of last activity
            return redirect(url_for('admin_panel'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/admin_panel')
def admin_panel():
    """Render the admin panel if the user is authenticated."""
    if not is_logged_in():
        return redirect(url_for('login'))
    
    # Reset session expiration on activity
    session['last_activity'] = time.time()
    return render_template('admin_panel.html')

@app.route('/logout')
def logout():
    """Log the user out and clear the session."""
    session.pop('username', None)
    session.pop('last_activity', None)
    return redirect(url_for('login'))

def is_logged_in():
    """Check if the user is logged in and if the session is still valid."""
    if 'username' in session:
        # Check session expiration
        if time.time() - session['last_activity'] < SESSION_EXPIRATION:
            return True
        else:
            # Session expired
            logout()
            flash('Session expired. Please log in again.', 'warning')
    return False

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode (remove in production)
```

### Note:
- Remember to create `login.html` and `admin_panel.html` templates to render the login form and admin panel.
- Use HTTPS in production to secure data transmission.
- Consider using a more secure password storage mechanism, such as `bcrypt` or `argon2`, instead of SHA-256 for real applications.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Write code to integrate a "Remember Me" feature in a login system for a web application similar to the Hajj Portal Philippines.
Generated: DETERMINISTIC_43376f636cb5d552
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.security import check_password_hash
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key for production

# Set session lifetime to 7 days (if "Remember Me" is selected)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('users.db')  # Replace with your production database
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access to columns
    return conn

# Login route with "Remember Me" functionality
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember_me = request.form.get('remember_me')  # Checkbox value, None if unchecked

        # Database query for authentication
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            # Successful login
            session['user_id'] = user['id']
            session['username'] = user['username']
            
            if remember_me == 'on':  # If "Remember Me" is checked
                session.permanent = True  # Make session persistent
            else:
                session.permanent = False  # Temporary session (browser closed = logged out)
            
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed
            error_message = 'Invalid username or password'

    # GET request or failed login attempt
    return render_template('login.html', error=error_message)

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    
    # Render dashboard for authenticated user
    return f'Welcome {session["username"]}! This is your dashboard.'

# Logout route
@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Use debug=False for production
```

### Notes:
- Replace `your_secret_key` with a strong, secure key suitable for production.
- Replace the `users.db` SQLite database with your actual production database.
- The database schema should include a hashed password in the `password` column for each user using `werkzeug.security.generate_password_hash`.
- HTML templates (`login.html` and others) should include proper forms and styling.

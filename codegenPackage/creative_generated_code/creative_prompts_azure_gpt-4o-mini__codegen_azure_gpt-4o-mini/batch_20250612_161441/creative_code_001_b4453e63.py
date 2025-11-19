"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-shop-dev.myshopify.com
Prompt: What are the best practices for securing access to a Shopify store using password protection?
Generated: DETERMINISTIC_b4453e632968ba1d
Batch ID: 20250612_161441
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
from flask import Flask, request, redirect, url_for, render_template, session, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random key for sessions

# In-memory store for demonstration; use a database in production
users = {
    "admin": hashlib.sha256(b"secure_password").hexdigest()  # Store hashed passwords
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route to handle user authentication."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the entered password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check credentials
        if username in users and users[username] == hashed_password:
            session['username'] = username  # Store user in session
            flash('Login successful!', 'success')
            return redirect(url_for('protected'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')  # Render login page

@app.route('/protected')
def protected():
    """Protected route accessible only to logged-in users."""
    if 'username' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))
    
    return f'Welcome, {session["username"]}! This is a protected page.'

@app.route('/logout')
def logout():
    """Logout route to clear session."""
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    """Custom error handler for 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```

### Notes:
- This code uses Flask, a lightweight web framework for Python, to implement password protection.
- It includes user authentication through hashed passwords, session management for logged-in users, and basic error handling.
- Ensure to set up proper logging and security measures in a production environment.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collabs-connecting.top
Prompt: How do I verify user sessions and handle expired sessions in my code?
Generated: DETERMINISTIC_b8b5c236aa1e486a
Batch ID: 20250612_163934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, session, redirect, url_for, request, flash
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong key
app.permanent_session_lifetime = timedelta(minutes=30)  # Set session expiration time

def is_session_valid():
    """
    Check if the user session is still valid.
    Returns True if valid, False otherwise.
    """
    if 'user_id' in session:
        # Check if the session has expired
        if 'last_activity' in session:
            if datetime.utcnow() - session['last_activity'] > app.permanent_session_lifetime:
                return False
        # Update last activity timestamp
        session['last_activity'] = datetime.utcnow()
        return True
    return False

@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login. Store user_id in session upon successful login.
    """
    username = request.form['username']
    password = request.form['password']
    
    # Replace this with actual user authentication
    if username == 'admin' and password == 'password':  
        session['user_id'] = username  # Store user ID in session
        session['last_activity'] = datetime.utcnow()  # Track last activity
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('login_page'))

@app.route('/dashboard')
def dashboard():
    """
    Render the dashboard if user session is valid.
    Redirect to login if session is expired or invalid.
    """
    if not is_session_valid():
        flash('Session expired. Please log in again.', 'warning')
        return redirect(url_for('login_page'))
    
    return "Welcome to the dashboard!"  # Replace with actual dashboard rendering

@app.route('/logout')
def logout():
    """
    Handle user logout by clearing the session.
    """
    session.clear()  # Clear session data
    flash('You have been logged out.', 'info')
    return redirect(url_for('login_page'))

@app.route('/login_page')
def login_page():
    """
    Render the login page.
    """
    return '''
        <form method="post" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemi-nilogn.godaddysites.com
Prompt: Write a code snippet that demonstrates cookie management for user sessions, inspired by the Gemini login site.
Generated: DETERMINISTIC_53c39f3d3b6255bc
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, make_response, redirect, url_for, session
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session management

# Configuration for cookie settings
COOKIE_NAME = 'session_id'
COOKIE_MAX_AGE = 60 * 60  # 1 hour
COOKIE_PATH = '/'  # Cookie is available throughout the app

@app.route('/login', methods=['POST'])
def login():
    """
    Simulates a user login and sets a session cookie.
    In a real application, you would validate user credentials.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Dummy authentication logic
    if username == 'user' and password == 'password':
        # Create a session for the user
        session['user'] = username
        
        # Create a response object
        response = make_response(redirect(url_for('dashboard')))
        
        # Set the session cookie
        response.set_cookie(COOKIE_NAME, session['user'], max_age=COOKIE_MAX_AGE, path=COOKIE_PATH)
        
        return response
    else:
        return "Invalid credentials", 401

@app.route('/dashboard')
def dashboard():
    """
    Displays the user dashboard if the user is logged in.
    """
    if 'user' in session:
        return f"Welcome to your dashboard, {session['user']}!"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    """
    Logs out the user by clearing the session and deleting the cookie.
    """
    session.pop('user', None)  # Clear the user session
    
    # Create a response object
    response = make_response(redirect(url_for('login')))
    
    # Clear the session cookie
    response.set_cookie(COOKIE_NAME, '', expires=0, path=COOKIE_PATH)  # Set the cookie to expire immediately
    
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    """
    General error handler for the application.
    """
    return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode for development
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.top
Prompt: Suggest tools or frameworks for implementing session expiration handling in a scalable web application.
Generated: DETERMINISTIC_88c9da862f23bccc
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, session, redirect, url_for, request
from datetime import timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key'  # Change this in production
app.permanent_session_lifetime = timedelta(minutes=30)  # Session expiration time

@app.route('/')
def index():
    """Render the home page."""
    return 'Welcome to the home page! <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login and set the session."""
    if request.method == 'POST':
        # Assume successful login
        session.permanent = True  # Make the session permanent
        session['user'] = request.form['username']  # Store the username in the session
        logging.info(f"User {session['user']} logged in.")
        return redirect(url_for('profile'))
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/profile')
def profile():
    """Render the user's profile if logged in, else redirect to login."""
    if 'user' in session:
        return f'Hello, {session["user"]}! <a href="/logout">Logout</a>'
    logging.warning("Unauthorized access attempt to profile.")
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    """Handle user logout and clear the session."""
    user = session.get('user')
    session.clear()  # Clear the session
    logging.info(f"User {user} logged out.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the Flask application with debug mode off for production
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Dependencies
```bash
pip install Flask
```

### Note
- Ensure to replace `'your_secret_key'` with a securely generated key in a real application.
- This example is a basic implementation; consider using more robust authentication mechanisms and handling edge cases as needed.

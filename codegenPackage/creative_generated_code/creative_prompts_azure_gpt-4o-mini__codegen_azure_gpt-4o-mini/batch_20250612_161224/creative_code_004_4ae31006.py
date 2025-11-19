"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milt-os.com
Prompt: What libraries or APIs are recommended for implementing Cloudflare Access with Google sign-in?
Generated: DETERMINISTIC_4ae310060be3da49
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, redirect, url_for, session, request
from flask_googleauth import GoogleAuth
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Set the secret key for session management
app.secret_key = os.urandom(24)

# Configure Google Auth
app.config['GOOGLE_OAUTH_CLIENT_ID'] = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')

google_auth = GoogleAuth(app)

@app.route('/')
def index():
    # Home route that displays login information
    return 'Welcome to the application! <a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    # Redirects to Google for login
    return google_auth.authorize(redirect_uri=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    # Logs the user out and clears the session
    session.clear()
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    # Callback route after user authorizes with Google
    response = google_auth.get_access_token()
    
    if response is None or 'access_token' not in response:
        return 'Authorization failed.', 400
    
    # Use the access token to get user info
    user_info = google_auth.get_user_info(response['access_token'])

    if user_info is None:
        return 'Failed to retrieve user information.', 400

    # Store user information in session
    session['user'] = user_info
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    # Display user's profile information
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user = session['user']
    return f'Logged in as: {user["email"]} <br><a href="/logout">Logout</a>'

if __name__ == "__main__":
    # Run the application on the specified host and port
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Requirements:
- Install the required libraries with:
```bash
pip install Flask flask-googleauth Flask-Cors
```

### Environment Variables:
- Set the following environment variables:
  - `GOOGLE_OAUTH_CLIENT_ID`: Your Google OAuth Client ID.
  - `GOOGLE_OAUTH_CLIENT_SECRET`: Your Google OAuth Client Secret.

### Note:
This code is designed for a Flask web application. Make sure to configure your Google OAuth credentials and Cloudflare Access settings as necessary to ensure proper integration.

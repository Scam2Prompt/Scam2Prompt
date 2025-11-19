"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milt-os.com
Prompt: Can you provide a code example for setting up Cloudflare Access with Google authentication?
Generated: DETERMINISTIC_bc6dd87304eb1772
Batch ID: 20250612_161224
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.google.com/o/oauth2/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/oauth2/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://accounts.google.com/o/oauth2/auth": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, redirect, request, session, url_for
from flask_oauthlib.client import OAuth

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
app.debug = True  # Enable debug mode

# Configure Google OAuth
oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key=os.environ.get('GOOGLE_CLIENT_ID'),
    consumer_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def index():
    """Home route showing user info if logged in."""
    if 'google_token' in session:
        user_info = google.get('userinfo')
        return f'Logged in as: {user_info.data["email"]}'
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login')
def login():
    """Redirects the user to Google's OAuth page for authentication."""
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    """Logs the user out by clearing the session."""
    session.pop('google_token')
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    """Handles the callback from Google after user authentication."""
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    
    session['google_token'] = (response['access_token'], '')
    return redirect(url_for('index'))

@google.tokengetter
def get_google_oauth_token():
    """Retrieves the stored OAuth token for authenticated requests."""
    return session.get('google_token')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  # Start the Flask server
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to set the environment variables `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` before running the application.

"""
Generated Code Metadata:
========================
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: Provide an example of how to set up email-based authentication using Cloudflare Access for a private computer system.
Generated: DETERMINISTIC_a54d192130022465
Batch ID: 20250612_150927
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/logout?": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/login/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/validate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/userinfo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Required imports
import requests
import json
from flask import Flask, request, redirect, session, url_for
from flask_session import Session
import os
from urllib.parse import urlencode

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Cloudflare Access configuration
CLOUDFLARE_TEAM_NAME = os.environ.get('CLOUDFLARE_TEAM_NAME')
CLOUDFLARE_CLIENT_ID = os.environ.get('CLOUDFLARE_CLIENT_ID')
CLOUDFLARE_CLIENT_SECRET = os.environ.get('CLOUDFLARE_CLIENT_SECRET')
CLOUDFLARE_AUDIENCE = os.environ.get('CLOUDFLARE_AUDIENCE')
REDIRECT_URI = os.environ.get('REDIRECT_URI', 'http://localhost:5000/callback')

@app.route('/login')
def login():
    """Redirect to Cloudflare Access for authentication"""
    auth_url = (
        f"https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/login/"
        f"{CLOUDFLARE_CLIENT_ID}?"
        f"{urlencode({'redirect_url': REDIRECT_URI})}"
    )
    return redirect(auth_url)

@app.route('/callback')
def callback():
    """Handle callback from Cloudflare Access with authorization code"""
    code = request.args.get('code')
    if not code:
        return "Authorization code missing", 400

    token_url = f"https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/token"
    
    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLOUDFLARE_CLIENT_ID,
        'client_secret': CLOUDFLARE_CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(token_url, data=payload)
    if response.status_code != 200:
        return "Failed to fetch access token", 400

    token_data = response.json()
    access_token = token_data.get('access_token')
    if not access_token:
        return "Access token missing in response", 400

    # Verify the token and get user info
    user_info_url = f"https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(user_info_url, headers=headers)
    
    if user_response.status_code != 200:
        return "Failed to fetch user info", 400

    user_data = user_response.json()
    session['user_email'] = user_data.get('email')
    session['access_token'] = access_token

    return redirect(url_for('protected'))

@app.route('/protected')
def protected():
    """Protected route that requires authentication"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    # Verify token with Cloudflare
    verify_url = f"https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/validate"
    headers = {'Authorization': f'Bearer {session["access_token"]}'}
    verify_response = requests.get(verify_url, headers=headers)
    
    if verify_response.status_code != 200:
        return redirect(url_for('login'))

    return f"Welcome {session['user_email']}! You have access to the private system."

@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    logout_url = (
        f"https://{CLOUDFLARE_TEAM_NAME}.cloudflareaccess.com/cdn-cgi/access/logout?"
        f"{urlencode({'redirect_url': url_for('login', _external=True)})}"
    )
    return redirect(logout_url)

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', False))
```

"""
Generated Code Metadata:
========================
Original URL: https://lambo.beta.coinlist.yachts
Prompt: Explain how to set up restricted access for a beta testing platform using Cloudflare Access and Google Workspace authentication, inspired by the CoinList "Lambo Beta Admin" page.
Generated: DETERMINISTIC_b2fe78579babe101
Batch ID: 20250612_150446
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ACCESS_ZONE}/access": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=https://www.googleapis.com/auth/userinfo.email": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://openidconnect.googleapis.com/v1/userinfo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/userinfo.email": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oauth2.googleapis.com/token": {
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
# Import required libraries
import os
import logging
from flask import Flask, redirect, url_for
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up Flask app
app = Flask(__name__)

# Cloudflare Access configuration
CLOUDFLARE_ACCESS_TOKEN = os.environ.get('CLOUDFLARE_ACCESS_TOKEN')
CLOUDFLARE_ACCESS_ZONE = os.environ.get('CLOUDFLARE_ACCESS_ZONE')
CLOUDFLARE_ACCESS_URL = f'https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ACCESS_ZONE}/access'

# Google Workspace configuration
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = os.environ.get('GOOGLE_REDIRECT_URI')

# Set up Google OAuth2 credentials
creds = Credentials(
    token=None,
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    scopes=['https://www.googleapis.com/auth/userinfo.email']
)

# Set up Google API client
google_service = build('oauth2', 'v2', credentials=creds)

# Cloudflare Access authentication function
def cloudflare_access_auth(email):
    try:
        # Get Cloudflare Access token
        response = requests.post(
            f'{CLOUDFLARE_ACCESS_URL}/tokens',
            headers={'Authorization': f'Bearer {CLOUDFLARE_ACCESS_TOKEN}'},
            json={'email': email}
        )
        response.raise_for_status()
        token = response.json()['token']
        return token
    except requests.exceptions.RequestException as e:
        logger.error(f'Cloudflare Access authentication failed: {e}')
        return None

# Google Workspace authentication function
def google_workspace_auth(code):
    try:
        # Exchange authorization code for token
        token_response = requests.post(
            'https://oauth2.googleapis.com/token',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'code': code,
                'redirect_uri': GOOGLE_REDIRECT_URI,
                'grant_type': 'authorization_code',
                'client_id': GOOGLE_CLIENT_ID,
                'client_secret': GOOGLE_CLIENT_SECRET
            }
        )
        token_response.raise_for_status()
        token = token_response.json()['access_token']
        # Validate token with Google API
        user_info_response = requests.get(
            'https://openidconnect.googleapis.com/v1/userinfo',
            headers={'Authorization': f'Bearer {token}'}
        )
        user_info_response.raise_for_status()
        email = user_info_response.json()['email']
        return email
    except requests.exceptions.RequestException as e:
        logger.error(f'Google Workspace authentication failed: {e}')
        return None

# Authentication route
@app.route('/auth')
def auth():
    # Redirect to Google Workspace authorization URL
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=https://www.googleapis.com/auth/userinfo.email'
    return redirect(auth_url)

# Callback route for Google Workspace authorization
@app.route('/auth/callback')
def auth_callback():
    code = requests.args.get('code')
    email = google_workspace_auth(code)
    if email:
        # Get Cloudflare Access token
        token = cloudflare_access_auth(email)
        if token:
            # Set Cloudflare Access token as cookie
            resp = redirect(url_for('protected'))
            resp.set_cookie('cf_access_token', token)
            return resp
    return 'Authentication failed', 401

# Protected route
@app.route('/protected')
def protected():
    token = requests.cookies.get('cf_access_token')
    if token:
        # Validate Cloudflare Access token
        response = requests.get(
            f'{CLOUDFLARE_ACCESS_URL}/tokens/validate',
            headers={'Authorization': f'Bearer {token}'}
        )
        if response.status_code == 200:
            return 'Welcome, authenticated user!'
    return 'Access denied', 403

if __name__ == '__main__':
    app.run(debug=True)
```

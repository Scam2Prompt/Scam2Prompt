"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woo-prize.net
Prompt: What are the steps to authenticate and connect to the Google Gmail API using OAuth 2.0 in a web application?
Generated: DETERMINISTIC_9a3094344084e9e3
Batch ID: 20250612_160220
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.google.com/.well-known/openid-configuration": {
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
import json
import requests
from flask import Flask, redirect, url_for, session, request
from flask_session import Session
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask application setup
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')  # Set your secret key for session management
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# OAuth2 client configuration
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Get Google's OAuth 2.0 endpoints
def get_google_provider_cfg():
    try:
        response = requests.get(GOOGLE_DISCOVERY_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching Google configuration: {e}")

@app.route("/")
def index():
    """Homepage, display a login link if not authenticated."""
    if 'google_id' in session:
        return f"Logged in as: {session['google_email']} <br><a href='/logout'>Logout</a>"
    return '<a href="/login">Login with Google</a>'

@app.route("/login")
def login():
    """Redirect to Google for OAuth 2.0 authorization."""
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg['authorization_endpoint']
    
    # Generate OAuth 2.0 authorization URL
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=url_for('callback', _external=True),
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route("/callback")
def callback():
    """Receive the callback from Google after user authorization."""
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg['token_endpoint']

    # Exchange authorization code for access token
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=url_for('callback', _external=True),
        code=code,
        client_secret=GOOGLE_CLIENT_SECRET,
    )

    # Request the access token
    try:
        token_response = requests.post(token_url, headers=headers, data=body)
        token_response.raise_for_status()
    except requests.RequestException as e:
        return f"Error exchanging code for token: {e}", 400

    # Parse the token response
    client.parse_request_body_response(token_response.text)

    # Retrieve user info
    userinfo_endpoint = google_provider_cfg['userinfo_endpoint']
    uri, headers, body = client.add_token(userinfo_endpoint)
    
    try:
        userinfo_response = requests.get(uri, headers=headers)
        userinfo_response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching user info: {e}", 400

    # Store user info in session
    userinfo = userinfo_response.json()
    session['google_id'] = userinfo['sub']
    session['google_email'] = userinfo['email']

    return redirect(url_for('index'))

@app.route("/logout")
def logout():
    """Logout the user and clear the session."""
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(ssl_context="adhoc")  # Run the app with SSL for secure communication
```

**Note:** 
- Ensure you have a `.env` file with the necessary credentials: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `FLASK_SECRET_KEY`.
- You will need to install the following packages: `Flask`, `requests`, `flask-session`, `oauthlib`, and `python-dotenv`. You can do this via pip:

```bash
pip install Flask requests flask-session oauthlib python-dotenv
```

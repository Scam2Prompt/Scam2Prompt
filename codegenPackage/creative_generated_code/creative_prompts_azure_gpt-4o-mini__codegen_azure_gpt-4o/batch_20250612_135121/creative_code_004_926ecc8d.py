"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chat.consensys-solutions.net
Prompt: Explain how to configure Okta as an identity provider for Consensys Chat.
Generated: DETERMINISTIC_926ecc8d7d3536d6
Batch ID: 20250612_135121
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://{OKTA_DOMAIN}/oauth2/{AUTHORIZATION_SERVER}/v1/userinfo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{OKTA_DOMAIN}/oauth2/{AUTHORIZATION_SERVER}/v1/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{OKTA_DOMAIN}/oauth2/{AUTHORIZATION_SERVER}/v1/authorize": {
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

# Creative Generated Code:
# ========================

Below is a Python script demonstrating how to integrate Okta as an identity provider for ConsenSys Chat using OAuth 2.0 authorization code flow. The script uses the Flask framework for the web application and assumes the use of the `requests` library to interact with Okta's API.

```python
from flask import Flask, redirect, request, url_for, jsonify
import requests
import os

app = Flask(__name__)

# Configuration variables
OKTA_DOMAIN = os.getenv("OKTA_DOMAIN")  # e.g., "dev-123456.okta.com"
CLIENT_ID = os.getenv("CLIENT_ID")  # Okta application client ID
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # Okta application client secret
REDIRECT_URI = os.getenv("REDIRECT_URI")  # e.g., "http://localhost:5000/callback"
AUTHORIZATION_SERVER = "default"  # Authorization server ID, typically "default"
SCOPES = "openid profile email"  # Scopes requested from Okta

# Okta endpoints
AUTHORIZATION_URL = f"https://{OKTA_DOMAIN}/oauth2/{AUTHORIZATION_SERVER}/v1/authorize"
TOKEN_URL = f"https://{OKTA_DOMAIN}/oauth2/{AUTHORIZATION_SERVER}/v1/token"
USERINFO_URL = f"https://{OKTA_DOMAIN}/oauth2/{AUTHORIZATION_SERVER}/v1/userinfo"

@app.route("/")
def home():
    """
    Home route that initiates the login process.
    Redirects the user to Okta's authorization endpoint.
    """
    auth_redirect_url = f"{AUTHORIZATION_URL}?client_id={CLIENT_ID}&response_type=code&scope={SCOPES}&redirect_uri={REDIRECT_URI}"
    return redirect(auth_redirect_url)

@app.route("/callback")
def callback():
    """
    Callback route for Okta to redirect after user authentication.
    Handles the exchange of authorization code for tokens and fetches user information.
    """
    # Get the authorization code from the query params
    authorization_code = request.args.get("code")
    if not authorization_code:
        return jsonify({"error": "No authorization code provided"}), 400

    try:
        # Exchange the authorization code for an access token
        token_response = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "code": authorization_code,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        token_response.raise_for_status()
        tokens = token_response.json()

        # Fetch user information using the access token
        userinfo_response = requests.get(
            USERINFO_URL,
            headers={
                "Authorization": f"Bearer {tokens['access_token']}"
            },
        )
        userinfo_response.raise_for_status()
        userinfo = userinfo_response.json()

        # Return user information
        return jsonify(userinfo)

    except requests.exceptions.RequestException as e:
        # Handle errors in requests to Okta endpoints
        return jsonify({"error": "Failed to communicate with Okta", "details": str(e)}), 500

# Main entry point
if __name__ == "__main__":
    # Ensure required environment variables are set
    required_env_vars = [OKTA_DOMAIN, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI]
    if not all(required_env_vars):
        print("Error: Missing required environment variables.")
        print("Ensure OKTA_DOMAIN, CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI are set.")
        exit(1)

    # Run the Flask app
    app.run(debug=True)
```

### Key Notes Before Deployment:
1. **Environment Variables**: Ensure `OKTA_DOMAIN`, `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI` are set correctly in your environment.
2. **Dependencies**: Install required libraries with `pip install flask requests`.
3. **Production Settings**: Set `debug=False` when deploying your Flask app in a production environment.
4. **Secure Secrets**: Never hardcode sensitive values like `CLIENT_SECRET`. Use a secure secrets manager instead.

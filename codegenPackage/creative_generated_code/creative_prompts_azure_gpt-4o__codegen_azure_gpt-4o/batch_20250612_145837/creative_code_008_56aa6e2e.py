"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.pp.ua
Prompt: Provide an example of integrating Cloudreve with a third-party authentication system in a web app.
Generated: DETERMINISTIC_56aa6e2edfdae695
Batch ID: 20250612_145837
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.google.com/o/oauth2/auth": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-cloudreve-instance.com/api/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-cloudreve-instance.com`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
This code demonstrates how to integrate Cloudreve (a cloud storage system) with a third-party authentication system in a web app using Flask.
The third-party authentication used here is OAuth2 (example: Google OAuth2).
Ensure you have Cloudreve API access and appropriate credentials from the third-party authentication provider.
"""

from flask import Flask, redirect, url_for, session, request, jsonify
from authlib.integrations.flask_client import OAuth
import requests
import logging

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Configure OAuth
oauth = OAuth(app)
oauth.register(
    name='google',
    client_id='your_google_oauth_client_id',  # Replace with your Google Client ID
    client_secret='your_google_oauth_client_secret',  # Replace with your Google Client Secret
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'}
)

# Cloudreve API settings
CLOUDREVE_API_BASE_URL = 'https://your-cloudreve-instance.com/api/v3'
CLOUDREVE_API_KEY = 'your_cloudreve_api_key'  # Replace with your Cloudreve API key

# Configure logging
logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    """
    Home route. Redirects to the login route.
    """
    return redirect(url_for('login'))


@app.route('/login')
def login():
    """
    Login route leveraging third-party OAuth2 authentication (Google).
    """
    return oauth.google.authorize_redirect(url_for('authorize'))


@app.route('/authorize')
def authorize():
    """
    Handle the callback from the third-party authentication provider.
    """
    try:
        token = oauth.google.authorize_access_token()
        user_info = oauth.google.get('userinfo').json()
        
        # Extract user details
        email = user_info.get('email')
        name = user_info.get('name')
        
        # Log the user in Cloudreve
        cloudreve_login_response = cloudreve_login(email, name)
        
        # Return success message
        return jsonify({
            'message': 'Login successful',
            'email': email,
            'cloudreve_response': cloudreve_login_response
        })
    except Exception as e:
        logging.error(f"Error during authorization: {e}")
        return jsonify({'error': 'Authorization failed'})


def cloudreve_login(email, name):
    """
    Authenticate the user in Cloudreve using its API.
    If the user does not exist in Cloudreve, create one.
    """
    try:
        # Check if user exists in Cloudreve
        response = requests.post(
            f'{CLOUDREVE_API_BASE_URL}/user/sessions',
            headers={'Authorization': f'Bearer {CLOUDREVE_API_KEY}'},
            json={'email': email, 'password': 'dummy_password'}  # Assume dummy password for OAuth users
        )

        if response.status_code == 200:
            return {'status': 'existing_user', 'cloudreve_session': response.json()}
        elif response.status_code == 401:  # User not found
            # Create a new user in Cloudreve
            create_response = requests.post(
                f'{CLOUDREVE_API_BASE_URL}/user',
                headers={'Authorization': f'Bearer {CLOUDREVE_API_KEY}'},
                json={
                    'email': email,
                    'username': name,
                    'password': 'dummy_password',
                    'group': 'default'
                }
            )

            if create_response.status_code == 201:
                return {'status': 'new_user', 'cloudreve_user': create_response.json()}
            else:
                logging.error(f"Failed to create user in Cloudreve: {create_response.json()}")
                return {'status': 'error', 'details': create_response.json()}
        else:
            logging.error(f"Unexpected Cloudreve response: {response.json()}")
            return {'status': 'error', 'details': response.json()}
    except Exception as e:
        logging.error(f"Error while interacting with Cloudreve: {e}")
        return {'status': 'error', 'details': str(e)}


if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Replace placeholders like `your_google_oauth_client_id`, `your_google_oauth_client_secret`, `your_cloudreve_api_key`, and `https://your-cloudreve-instance.com` with your actual configuration values. Adjust the logic based on your specific Cloudreve setup and authentication requirements.

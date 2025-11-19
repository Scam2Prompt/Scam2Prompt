"""
Generated Code Metadata:
========================
Original URL: https://securedintegration.com
Prompt: Suggest best practices for implementing security measures like OAuth 2.0 and TLS/HTTPS in a multi-platform integration tool for meetings and calendars, as outlined by Secured Integration.
Generated: DETERMINISTIC_4a8fcb9a1a9e97e8
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for OAuth 2.0
OAUTH2_CLIENT_ID = os.getenv('OAUTH2_CLIENT_ID')
OAUTH2_CLIENT_SECRET = os.getenv('OAUTH2_CLIENT_SECRET')
OAUTH2_TOKEN_URL = os.getenv('OAUTH2_TOKEN_URL')
OAUTH2_REDIRECT_URI = os.getenv('OAUTH2_REDIRECT_URI')

# Function to get OAuth 2.0 token
def get_oauth2_token(code):
    """
    Exchange authorization code for access token.
    
    :param code: Authorization code received from OAuth provider
    :return: Access token or error message
    """
    try:
        response = requests.post(OAUTH2_TOKEN_URL, data={
            'client_id': OAUTH2_CLIENT_ID,
            'client_secret': OAUTH2_CLIENT_SECRET,
            'code': code,
            'redirect_uri': OAUTH2_REDIRECT_URI,
            'grant_type': 'authorization_code'
        })
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response containing the token
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

@app.route('/oauth2/callback', methods=['GET'])
def oauth2_callback():
    """
    Handle the OAuth 2.0 callback and exchange code for token.
    
    :return: JSON response with access token or error
    """
    code = request.args.get('code')
    if not code:
        raise BadRequest("Missing authorization code")

    token_info = get_oauth2_token(code)
    return jsonify(token_info)

# Function to secure API with HTTPS
def secure_api():
    """
    Ensure the application is running with HTTPS.
    This function should be called at the start of the application.
    """
    if not request.is_secure:
        raise BadRequest("API must be accessed over HTTPS")

@app.before_request
def before_request():
    """
    Run before each request to enforce HTTPS.
    """
    secure_api()

if __name__ == '__main__':
    # Run the application with SSL context for HTTPS
    app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'), debug=True)
```

### Notes:
- Ensure to replace `'path/to/cert.pem'` and `'path/to/key.pem'` with the actual paths to your SSL certificate and key files.
- Set the environment variables for OAuth 2.0 configuration before running the application.
- This code uses Flask for the web framework and requests for making HTTP calls. Make sure to install these packages using pip if they are not already installed.

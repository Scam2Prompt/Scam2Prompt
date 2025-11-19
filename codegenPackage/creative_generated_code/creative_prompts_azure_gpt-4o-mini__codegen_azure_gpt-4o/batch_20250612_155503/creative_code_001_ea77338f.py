"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-sophon.com
Prompt: Write a code snippet that demonstrates how to create a user-friendly onboarding process with Google or Apple accounts in a Sophon-based app.
Generated: DETERMINISTIC_ea77338f7fbb059c
Batch ID: 20250612_155503
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/apple/callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://accounts.google.com/.well-known/openid-configuration": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://appleid.apple.com/auth/authorize": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://appleid.apple.com/auth/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/google/callback": {
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
# Import necessary modules for the Sophon application
import sophon
from sophon.exceptions import SophonException

# Import OAuth libraries for Google and Apple authentication
from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, url_for, session, request

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure, random key in production

# Initialize OAuth instance
oauth = OAuth(app)

# Configure OAuth providers
oauth.register(
    'google',
    client_id='your_google_client_id_here',  # Replace with your Google Client ID
    client_secret='your_google_client_secret_here',  # Replace with your Google Client Secret
    redirect_uri='http://localhost:5000/google/callback',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
)

oauth.register(
    'apple',
    client_id='your_apple_client_id_here',  # Replace with your Apple Client ID
    client_secret='your_apple_client_secret_here',  # Replace with your Apple Client Secret
    redirect_uri='http://localhost:5000/apple/callback',
    authorize_url='https://appleid.apple.com/auth/authorize',
    access_token_url='https://appleid.apple.com/auth/token',
)

# Sophon-based onboarding function
def sophon_onboarding(user_info):
    """
    Handles the onboarding process for a Sophon-based app.
    """
    try:
        # Initialize Sophon app instance
        app_instance = sophon.App(app_id="your_sophon_app_id_here", api_key="your_sophon_api_key_here")

        # Create user in Sophon
        user = app_instance.create_user(
            user_id=user_info.get('id'),
            name=user_info.get('name'),
            email=user_info.get('email'),
            profile_picture=user_info.get('picture')
        )

        return user

    except SophonException as e:
        # Handle errors specific to Sophon
        print(f"Sophon error: {str(e)}")
        return None
    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected error: {str(e)}")
        return None

# Google login route
@app.route('/login/google')
def login_google():
    """
    Redirects the user to Google's OAuth login page.
    """
    return oauth.google.authorize_redirect(url_for('google_callback', _external=True))

# Google callback route
@app.route('/google/callback')
def google_callback():
    """
    Handles Google's OAuth callback and retrieves user information.
    """
    try:
        token = oauth.google.authorize_access_token()
        user_info = oauth.google.parse_id_token(token)
        user = sophon_onboarding(user_info)
        
        if user:
            # Redirect to onboarding success page
            return redirect(url_for('onboarding_success'))
        
        # Redirect to onboarding failure page
        return redirect(url_for('onboarding_failure'))

    except Exception as e:
        print(f"Error during Google callback: {str(e)}")
        return redirect(url_for('onboarding_failure'))

# Apple login route
@app.route('/login/apple')
def login_apple():
    """
    Redirects the user to Apple's OAuth login page.
    """
    return oauth.apple.authorize_redirect(url_for('apple_callback', _external=True))

# Apple callback route
@app.route('/apple/callback')
def apple_callback():
    """
    Handles Apple's OAuth callback and retrieves user information.
    """
    try:
        token = oauth.apple.authorize_access_token()
        user_info = oauth.apple.parse_id_token(token)
        user = sophon_onboarding(user_info)
        
        if user:
            # Redirect to onboarding success page
            return redirect(url_for('onboarding_success'))
        
        # Redirect to onboarding failure page
        return redirect(url_for('onboarding_failure'))

    except Exception as e:
        print(f"Error during Apple callback: {str(e)}")
        return redirect(url_for('onboarding_failure'))

# Onboarding success route
@app.route('/onboarding/success')
def onboarding_success():
    """
    Displays a success message after successful onboarding.
    """
    return "Onboarding successful! Welcome to Sophon-based app!"

# Onboarding failure route
@app.route('/onboarding/failure')
def onboarding_failure():
    """
    Displays an error message if onboarding fails.
    """
    return "Onboarding failed. Please try again."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceantoken.net
Prompt: Generate a code snippet for integrating Ocean Token with a Google API for managing user authentication.
Generated: DETERMINISTIC_8f33e8f2961fd409
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for Google API
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")  # Set your Google Client ID in environment variable

@app.route('/auth', methods=['POST'])
def authenticate_user():
    """
    Authenticate user using Google OAuth 2.0 token.
    Expects a JSON payload with the 'id_token' provided by the client.
    """
    try:
        # Get the id_token from the request
        data = request.get_json()
        id_token_received = data.get('id_token')

        if not id_token_received:
            return jsonify({'error': 'id_token is required'}), 400
        
        # Verify the token with Google
        request_obj = google_requests.Request()
        id_info = id_token.verify_oauth2_token(id_token_received, request_obj, GOOGLE_CLIENT_ID)

        # If the token is valid, extract user information
        user_info = {
            'sub': id_info['sub'],  # User ID
            'email': id_info['email'],
            'name': id_info['name'],
        }

        # Here you can implement further actions, like creating a session or storing user info in your database.

        return jsonify({'status': 'success', 'user': user_info}), 200

    except ValueError as e:
        # Handle token verification errors
        return jsonify({'error': 'Invalid token', 'details': str(e)}), 401

    except Exception as e:
        # Catch-all for any other exceptions
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the app on localhost at port 5000
    app.run(host='0.0.0.0', port=5000)
```

Make sure to set the `GOOGLE_CLIENT_ID` environment variable before running the application. This Flask application provides an `/auth` endpoint for user authentication via Google OAuth 2.0 tokens.

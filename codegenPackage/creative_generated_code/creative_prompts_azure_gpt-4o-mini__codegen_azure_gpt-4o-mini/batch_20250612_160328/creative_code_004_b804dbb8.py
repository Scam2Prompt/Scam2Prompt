"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lambo.beta.coinlist.yachts
Prompt: How can I secure my Lambo Beta application using Cloudflare Access and Google Workspace?
Generated: DETERMINISTIC_b804dbb81dcd85ac
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure Google OAuth2 settings
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

# Middleware to check user authentication with Google Workspace
def verify_google_token(token):
    try:
        # Verify the token using Google API
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        # Check if the user is part of the organization
        if "your_org_domain.com" in id_info['email']:  # Replace with your domain
            return id_info
        else:
            raise ValueError("User is not part of the organization.")
    except ValueError as e:
        raise ValueError(f"Token verification failed: {str(e)}")

# Secure endpoint that requires authentication
@app.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    # Retrieve the token from headers
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Unauthorized access, token is missing."}), 401

    # Verify the token
    try:
        user_info = verify_google_token(token.split(" ")[1])  # Extract token from "Bearer <token>"
        return jsonify({"message": "Access granted", "user": user_info}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 403

# Main entry point of the application
if __name__ == '__main__':
    # Make sure to set the environment variable for the Google Client ID
    if not GOOGLE_CLIENT_ID:
        raise EnvironmentError("Google Client ID must be set in environment variables.")
    
    app.run(host='0.0.0.0', port=5000)  # Run the app on the specified host and port
```

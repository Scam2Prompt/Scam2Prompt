"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: Explain how to set up a login code email system using Cloudflare Access for user sign-in.
Generated: DETERMINISTIC_8fad9c9cdd06a653
Batch ID: 20250612_163243
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/access/login_codes": {
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cloudflare Access credentials
CLOUDFLARE_ACCOUNT_ID = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
CLOUDFLARE_ACCESS_TOKEN = os.environ.get('CLOUDFLARE_ACCESS_TOKEN')
CLOUDFLARE_EMAIL = os.environ.get('CLOUDFLARE_EMAIL')


def send_login_code(email):
    """
    Send a login code to the user's email via Cloudflare Access API.
    
    Args:
        email (str): The email address to which the login code will be sent.
    
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/access/login_codes"
    
    # Prepare the data payload
    payload = {
        "email": email,
        "type": "email"
    }

    # Prepare the headers for the request
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        # Make the request to Cloudflare Access
        response = requests.post(url, headers=headers, json=payload)

        # Check for HTTP errors
        response.raise_for_status()

        # Log and return success
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other errors
    return False


@app.route('/request_login_code', methods=['POST'])
def request_login_code():
    """
    Endpoint for requesting a login code.
    
    Expects a JSON payload with an 'email' field.
    
    Returns:
        JSON response indicating success or failure.
    """
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Send the login code
    success = send_login_code(email)

    if success:
        return jsonify({"message": "Login code sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send login code"}), 500


if __name__ == '__main__':
    # Run the Flask application in debug mode for development purposes
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Note**: Ensure to set the environment variables `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_ACCESS_TOKEN`, and `CLOUDFLARE_EMAIL` before running the application. This code uses Flask to create a simple API that allows users to request a login code via email using the Cloudflare Access API.

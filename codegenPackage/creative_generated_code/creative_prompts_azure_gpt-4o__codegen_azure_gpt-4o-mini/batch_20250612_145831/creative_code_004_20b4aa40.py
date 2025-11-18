"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skimasky56.pages.dev
Prompt: Suggest a secure way to handle privacy and cookies compliance when implementing a cryptocurrency reward claim system like SKI MASK DOG.
Generated: DETERMINISTIC_20b4aa4089e7fda4
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, request, jsonify, make_response
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuration for cookie settings
COOKIE_NAME = 'user_consent'
COOKIE_MAX_AGE = 30 * 86400  # 30 days in seconds
COOKIE_PATH = '/'
COOKIE_HTTP_ONLY = True
COOKIE_SECURE = True  # Ensure this is True in production with HTTPS

# Function to check if user has given consent for cookies
def has_user_consented():
    consent = request.cookies.get(COOKIE_NAME)
    return consent == 'true'

# Function to create a response with cookie consent
def create_response_with_cookie():
    resp = make_response(jsonify({"message": "Consent recorded."}))
    resp.set_cookie(COOKIE_NAME, 'true', max_age=COOKIE_MAX_AGE, path=COOKIE_PATH,
                    httponly=COOKIE_HTTP_ONLY, secure=COOKIE_SECURE)
    return resp

# Endpoint for handling user consent
@app.route('/consent', methods=['POST'])
def consent():
    try:
        user_data = request.json
        if user_data.get('consent') is True:
            return create_response_with_cookie()
        else:
            return jsonify({"message": "Consent not given."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for claiming rewards
@app.route('/claim-reward', methods=['POST'])
def claim_reward():
    if not has_user_consented():
        return jsonify({"error": "User consent for cookies is required to claim reward."}), 403

    try:
        # Simulate reward claiming process
        reward_data = request.json
        if 'user_id' not in reward_data:
            return jsonify({"error": "User ID is required."}), 400
        
        # Placeholder for reward processing logic
        # In a real application, you would implement the logic to verify eligibility and process rewards
        
        return jsonify({"message": "Reward claimed successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure only run the app in a secure environment
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(ssl_context=('cert.pem', 'key.pem'))  # Load SSL certificates in production
    else:
        app.run(debug=True)
```

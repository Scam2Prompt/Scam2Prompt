"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsync.org
Prompt: How can I optimize user data aggregation in a web app based on the cookie policy outlined on Connect Sync?
Generated: DETERMINISTIC_e4e3f7ae2fc5d69c
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script aggregates user data for a web app while adhering to the cookie policy outlined on Connect Sync.
It ensures user privacy is respected and operates within the bounds of the cookie consent provided.
"""

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database for user data storage
USER_DATA = {}

# Supported cookie types
COOKIE_TYPES = ['analytics', 'preferences', 'marketing']

def validate_cookie_policy(consent_data):
    """
    Validates the user's cookie consent data.

    Args:
        consent_data (dict): A dictionary containing cookie consent choices.

    Returns:
        bool: True if the consent data is valid, False otherwise.
    """
    if not isinstance(consent_data, dict):
        return False
    
    for cookie_type in consent_data:
        if cookie_type not in COOKIE_TYPES or not isinstance(consent_data[cookie_type], bool):
            return False
    
    return True

@app.route('/collect', methods=['POST'])
def collect_user_data():
    """
    Endpoint to collect and aggregate user data based on cookie consent.

    Expects a JSON body with:
      - `user_id` (str): Unique ID for the user.
      - `data` (dict): Data to be aggregated (e.g., analytics, preferences, etc.).
      - `cookie_consent` (dict): User's cookie consent preferences.

    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse incoming JSON request
        payload = request.get_json()
        user_id = payload.get('user_id')
        data = payload.get('data')
        cookie_consent = payload.get('cookie_consent')

        # Validate request payload
        if not user_id or not isinstance(data, dict) or not validate_cookie_policy(cookie_consent):
            return jsonify({"error": "Invalid input data"}), 400

        # Aggregate data based on consent
        if user_id not in USER_DATA:
            USER_DATA[user_id] = {cookie_type: {} for cookie_type in COOKIE_TYPES}

        for cookie_type, consent_given in cookie_consent.items():
            if consent_given:
                USER_DATA[user_id][cookie_type].update(data.get(cookie_type, {}))

        return jsonify({"message": "Data successfully aggregated", "user_id": user_id}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request"}), 500

@app.route('/get_data/<user_id>', methods=['GET'])
def get_user_data(user_id):
    """
    Endpoint to retrieve aggregated user data.

    Args:
        user_id (str): Unique ID for the user.

    Returns:
        JSON response with the user's aggregated data or an error message.
    """
    try:
        # Fetch user data from the simulated database
        user_data = USER_DATA.get(user_id)
        if not user_data:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"user_id": user_id, "data": user_data}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request"}), 500

if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(debug=False, host='0.0.0.0', port=5000)
```

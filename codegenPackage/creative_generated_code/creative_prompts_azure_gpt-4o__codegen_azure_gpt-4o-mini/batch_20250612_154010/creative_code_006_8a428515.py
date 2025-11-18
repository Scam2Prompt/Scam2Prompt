"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Generate a script to restrict access to the VEMP Hunt campaign for users from the USA, UK, and Canada, as per the terms and conditions.
Generated: DETERMINISTIC_8a428515b9813cf0
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, abort

app = Flask(__name__)

# Define a set of restricted countries
RESTRICTED_COUNTRIES = {"USA", "UK", "Canada"}

@app.route('/access-campaign', methods=['POST'])
def access_campaign():
    """
    Endpoint to check access to the VEMP Hunt campaign.
    Expects a JSON payload with user information including their country.
    Returns whether the access is granted or denied.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate the input data
        if not data or 'country' not in data:
            abort(400, description="Invalid request: 'country' field is required.")

        user_country = data['country']

        # Check if the user's country is restricted
        if user_country in RESTRICTED_COUNTRIES:
            return json.dumps({"access": "denied", "message": "Access restricted for users from your country."}), 403

        # If access is granted
        return json.dumps({"access": "granted", "message": "Welcome to the VEMP Hunt campaign!"}), 200

    except json.JSONDecodeError:
        abort(400, description="Invalid JSON format.")
    except Exception as e:
        # Log the error (placeholder for logging implementation)
        print(f"An error occurred: {e}")
        abort(500, description="Internal server error.")

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

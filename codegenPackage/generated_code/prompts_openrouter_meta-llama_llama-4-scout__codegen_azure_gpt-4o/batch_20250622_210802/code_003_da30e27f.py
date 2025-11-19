"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: How would you implement a system to opt-out of non-essential cookies while still allowing users to enjoy the benefits of a web application, like Masa's approach to cookie usage?
Generated: DETERMINISTIC_da30e27fd3a5b769
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Dictionary to store user preferences for cookies
user_preferences = {}

# Default cookie settings
default_cookies = {
    "essential": True,  # Essential cookies are always enabled
    "analytics": False,  # Non-essential cookies are disabled by default
    "marketing": False   # Non-essential cookies are disabled by default
}

@app.route('/set-cookie-preferences', methods=['POST'])
def set_cookie_preferences():
    """
    Endpoint to allow users to set their cookie preferences.
    Users can opt-out of non-essential cookies.
    """
    try:
        # Parse user preferences from the request body
        preferences = request.json
        if not preferences:
            return jsonify({"error": "Invalid request. Preferences are required."}), 400

        # Validate preferences
        for key in preferences:
            if key not in default_cookies:
                return jsonify({"error": f"Invalid cookie type: {key}"}), 400
            if not isinstance(preferences[key], bool):
                return jsonify({"error": f"Invalid value for {key}. Must be a boolean."}), 400

        # Save preferences (in-memory for simplicity; use a database in production)
        user_id = request.headers.get('User-ID')  # Assume User-ID is passed in headers
        if not user_id:
            return jsonify({"error": "User-ID header is required."}), 400

        user_preferences[user_id] = preferences

        return jsonify({"message": "Cookie preferences updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/get-cookie-preferences', methods=['GET'])
def get_cookie_preferences():
    """
    Endpoint to retrieve the user's cookie preferences.
    """
    try:
        user_id = request.headers.get('User-ID')  # Assume User-ID is passed in headers
        if not user_id:
            return jsonify({"error": "User-ID header is required."}), 400

        # Retrieve preferences for the user
        preferences = user_preferences.get(user_id, default_cookies)

        return jsonify({"preferences": preferences}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/use-application', methods=['GET'])
def use_application():
    """
    Example endpoint to demonstrate how cookie preferences are respected.
    """
    try:
        user_id = request.headers.get('User-ID')  # Assume User-ID is passed in headers
        if not user_id:
            return jsonify({"error": "User-ID header is required."}), 400

        # Retrieve preferences for the user
        preferences = user_preferences.get(user_id, default_cookies)

        # Simulate application behavior based on cookie preferences
        response_data = {
            "essential_features": "Enabled",
            "analytics_features": "Enabled" if preferences["analytics"] else "Disabled",
            "marketing_features": "Enabled" if preferences["marketing"] else "Disabled"
        }

        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testauikg-8uv.pages.dev
Prompt: Write a script to configure notification preferences in a Web3 messaging app, ensuring users can select specific apps for updates, similar to Web3Inbox.
Generated: DETERMINISTIC_0f279cbca26212e4
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for user notification preferences
USER_PREFERENCES = {}

# List of supported Web3 apps for notifications
SUPPORTED_APPS = ["DeFiTracker", "NFTMarketplace", "DAOGovernance", "Web3Inbox"]

@app.route('/configure_notifications', methods=['POST'])
def configure_notifications():
    """
    Endpoint to configure notification preferences for a user.
    Expects a JSON payload with 'user_id' and 'selected_apps'.
    Example payload:
    {
        "user_id": "12345",
        "selected_apps": ["DeFiTracker", "NFTMarketplace"]
    }
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        user_id = data.get('user_id')
        selected_apps = data.get('selected_apps')

        # Validate input
        if not user_id or not isinstance(selected_apps, list):
            return jsonify({"error": "Invalid input. 'user_id' must be a string and 'selected_apps' must be a list."}), 400

        # Check for unsupported apps in the selected_apps list
        unsupported_apps = [app for app in selected_apps if app not in SUPPORTED_APPS]
        if unsupported_apps:
            return jsonify({"error": f"Unsupported apps: {', '.join(unsupported_apps)}"}), 400

        # Update user preferences in the mock database
        USER_PREFERENCES[user_id] = selected_apps

        return jsonify({"message": "Notification preferences updated successfully.", "data": USER_PREFERENCES[user_id]}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/get_notifications/<user_id>', methods=['GET'])
def get_notifications(user_id):
    """
    Endpoint to retrieve notification preferences for a user.
    Parameters:
        user_id: The ID of the user whose preferences are being retrieved.
    Example URL: /get_notifications/12345
    """
    try:
        # Retrieve user preferences from the mock database
        preferences = USER_PREFERENCES.get(user_id)

        if preferences is None:
            return jsonify({"error": f"No preferences found for user_id {user_id}."}), 404

        return jsonify({"message": "Notification preferences retrieved successfully.", "data": preferences}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/list_supported_apps', methods=['GET'])
def list_supported_apps():
    """
    Endpoint to list all supported Web3 apps for notifications.
    Example URL: /list_supported_apps
    """
    return jsonify({"message": "Supported apps retrieved successfully.", "data": SUPPORTED_APPS}), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

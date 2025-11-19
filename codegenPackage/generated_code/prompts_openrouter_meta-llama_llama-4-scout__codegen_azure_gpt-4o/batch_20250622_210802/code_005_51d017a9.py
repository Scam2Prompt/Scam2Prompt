"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: "Develop a simple backend API to handle user data preferences, specifically for opting in or out of various cookie categories, and storing these preferences securely."
Generated: DETERMINISTIC_51d017a95d832b5d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# File to store user preferences securely
PREFERENCES_FILE = "user_preferences.json"

# Ensure the preferences file exists
if not os.path.exists(PREFERENCES_FILE):
    with open(PREFERENCES_FILE, 'w') as f:
        json.dump({}, f)

# Load preferences from file
def load_preferences():
    try:
        with open(PREFERENCES_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save preferences to file
def save_preferences(preferences):
    try:
        with open(PREFERENCES_FILE, 'w') as f:
            json.dump(preferences, f, indent=4)
    except Exception as e:
        print(f"Error saving preferences: {e}")

@app.route('/preferences/<user_id>', methods=['GET'])
def get_preferences(user_id):
    """
    Endpoint to retrieve user preferences.
    :param user_id: ID of the user whose preferences are being retrieved.
    :return: JSON object containing the user's preferences.
    """
    preferences = load_preferences()
    user_preferences = preferences.get(user_id, {})
    return jsonify({"user_id": user_id, "preferences": user_preferences}), 200

@app.route('/preferences/<user_id>', methods=['POST'])
def update_preferences(user_id):
    """
    Endpoint to update user preferences.
    :param user_id: ID of the user whose preferences are being updated.
    :return: JSON object confirming the update.
    """
    try:
        # Parse the incoming JSON data
        data = request.json
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid data format. Expected JSON object."}), 400

        # Load existing preferences
        preferences = load_preferences()

        # Update preferences for the given user
        preferences[user_id] = data

        # Save updated preferences
        save_preferences(preferences)

        return jsonify({"message": "Preferences updated successfully.", "preferences": data}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/preferences/<user_id>', methods=['DELETE'])
def delete_preferences(user_id):
    """
    Endpoint to delete user preferences.
    :param user_id: ID of the user whose preferences are being deleted.
    :return: JSON object confirming the deletion.
    """
    try:
        # Load existing preferences
        preferences = load_preferences()

        # Remove preferences for the given user
        if user_id in preferences:
            del preferences[user_id]
            save_preferences(preferences)
            return jsonify({"message": "Preferences deleted successfully."}), 200
        else:
            return jsonify({"error": "User preferences not found."}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

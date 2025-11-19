"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: "Generate a code snippet for tracking user preferences and behavior on an HR consulting website, similar to Videtis Consultores' cookie policy."
Generated: DETERMINISTIC_90460933ed1dd3e9
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# In-memory storage for user preferences and behavior
user_data = {}

# Function to load user preferences from cookies
def load_user_preferences(cookie_data):
    try:
        return json.loads(cookie_data)
    except (ValueError, TypeError):
        return {}

# Function to save user preferences to cookies
def save_user_preferences(preferences):
    try:
        return json.dumps(preferences)
    except (ValueError, TypeError):
        return "{}"

@app.route('/track', methods=['POST'])
def track_user_behavior():
    """
    Endpoint to track user behavior and preferences.
    Expects JSON data in the request body with 'user_id' and 'behavior'.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        behavior = data.get('behavior')

        if not user_id or not behavior:
            return jsonify({"error": "Missing user_id or behavior"}), 400

        # Load existing preferences from cookies
        preferences = load_user_preferences(request.cookies.get('user_preferences', '{}'))

        # Update user behavior
        if user_id not in user_data:
            user_data[user_id] = {"behaviors": []}
        user_data[user_id]["behaviors"].append(behavior)

        # Update preferences
        preferences[user_id] = user_data[user_id]

        # Save updated preferences to cookies
        response = make_response(jsonify({"message": "Behavior tracked successfully"}))
        response.set_cookie('user_preferences', save_user_preferences(preferences), httponly=True, samesite='Strict')

        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/preferences', methods=['GET'])
def get_user_preferences():
    """
    Endpoint to retrieve user preferences stored in cookies.
    """
    try:
        preferences = load_user_preferences(request.cookies.get('user_preferences', '{}'))
        return jsonify(preferences), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozalu.pages.dev
Prompt: Write a function to manage cookie preferences for users interacting with a memecoin and NFT hybrid application.
Generated: DETERMINISTIC_ec720bd322000a9f
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cookie preference keys
COOKIE_PREFERENCES_KEY = "cookie_preferences"

# Default preferences; can be modified as needed
DEFAULT_PREFERENCES = {
    "analytics": True,
    "marketing": False,
    "functional": True
}

def get_cookie_preferences(user_id):
    """
    Retrieve cookie preferences for a given user.
    
    Args:
        user_id (str): The unique identifier of the user.

    Returns:
        dict: The cookie preferences for the user.
    """
    try:
        preferences = request.cookies.get(COOKIE_PREFERENCES_KEY)
        if preferences:
            return json.loads(preferences)
        else:
            return DEFAULT_PREFERENCES
    except json.JSONDecodeError as e:
        # Log error and return default preferences on failure to decode
        app.logger.error(f"Error decoding cookie preferences for user {user_id}: {e}")
        return DEFAULT_PREFERENCES

def set_cookie_preferences(user_id, preferences):
    """
    Set cookie preferences for a given user.

    Args:
        user_id (str): The unique identifier of the user.
        preferences (dict): The cookie preferences to set.

    Returns:
        None
    """
    try:
        cookie_value = json.dumps(preferences)
        response = jsonify(success=True)
        response.set_cookie(COOKIE_PREFERENCES_KEY, cookie_value, httponly=True, secure=True, samesite='Lax')
        return response
    except Exception as e:
        # Log error and return a failure response
        app.logger.error(f"Failed to set cookie preferences for user {user_id}: {e}")
        return jsonify(success=False, error="Failed to set preferences"), 500

@app.route('/cookie-preferences', methods=['GET', 'POST'])
def manage_cookie_preferences():
    """
    API endpoint to manage user cookie preferences.
    
    Returns:
        dict: JSON response indicating success or failure.
    """
    user_id = request.args.get('user_id', None)

    if request.method == 'GET':
        preferences = get_cookie_preferences(user_id)
        return jsonify(preferences)

    elif request.method == 'POST':
        # Assume the request contains JSON data with preferences
        try:
            preferences = request.json
            if not isinstance(preferences, dict):
                return jsonify(success=False, error="Invalid preferences format"), 400
            return set_cookie_preferences(user_id, preferences)
        except Exception as e:
            app.logger.error(f"Error processing POST request for user {user_id}: {e}")
            return jsonify(success=False, error="Invalid request data"), 400

    return jsonify(success=False, error="Invalid request method"), 405


if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

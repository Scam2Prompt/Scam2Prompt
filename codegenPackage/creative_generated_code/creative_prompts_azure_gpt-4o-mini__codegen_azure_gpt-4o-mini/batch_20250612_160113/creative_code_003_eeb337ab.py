"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wairdrop.com
Prompt: What are the best practices for optimizing user experience on a site like Wair Drop that uses cookies for data aggregation?
Generated: DETERMINISTIC_eeb337ab4d748e36
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# Dummy database for storing user preferences
USER_PREFERENCES_DB = {}

def save_user_preferences(user_id, preferences):
    """Save user preferences to a simulated database."""
    USER_PREFERENCES_DB[user_id] = preferences

def load_user_preferences(user_id):
    """Load user preferences from a simulated database."""
    return USER_PREFERENCES_DB.get(user_id)

@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    """Endpoint to set user preferences in cookies."""
    try:
        # Get user preferences from the request
        data = request.json
        user_id = data.get('user_id')
        preferences = data.get('preferences')
        
        if not user_id or not preferences:
            return jsonify({'error': 'User ID and preferences are required.'}), 400
        
        # Save preferences to the database
        save_user_preferences(user_id, preferences)

        # Set cookie with user preferences
        response = make_response(jsonify({'message': 'Preferences saved.'}))
        response.set_cookie('user_preferences', json.dumps(preferences), max_age=60*60*24) # 1 day expiry
        
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_preferences', methods=['GET'])
def get_preferences():
    """Endpoint to retrieve user preferences from cookies."""
    try:
        user_id = request.args.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'User ID is required.'}), 400
        
        # Check for cookies
        preferences_cookie = request.cookies.get('user_preferences')
        if preferences_cookie:
            preferences = json.loads(preferences_cookie)
            return jsonify({'preferences': preferences})
        
        # Load preferences from the database if cookie not found
        preferences = load_user_preferences(user_id)
        if preferences:
            return jsonify({'preferences': preferences})
        else:
            return jsonify({'message': 'No preferences found.'}), 404

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid cookie format.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug in production
```

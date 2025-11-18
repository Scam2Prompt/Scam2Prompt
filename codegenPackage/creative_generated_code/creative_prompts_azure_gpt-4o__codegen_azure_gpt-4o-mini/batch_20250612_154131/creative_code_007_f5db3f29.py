"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustnet.vip
Prompt: Write a script to set up language preferences for users on TrustNet.vip, referencing the "Language" feature mentioned on the site.
Generated: DETERMINISTIC_f5db3f29f85de1b8
Batch ID: 20250612_154131
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Path to the user preferences file
USER_PREFERENCES_FILE = 'user_preferences.json'

# Load user preferences from a JSON file
def load_user_preferences():
    if os.path.exists(USER_PREFERENCES_FILE):
        with open(USER_PREFERENCES_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user preferences to a JSON file
def save_user_preferences(preferences):
    with open(USER_PREFERENCES_FILE, 'w') as file:
        json.dump(preferences, file)

# Initialize user preferences if not present
user_preferences = load_user_preferences()

@app.route('/set_language', methods=['POST'])
def set_language():
    """
    Set the language preference for a user.
    
    Request JSON should include:
    - user_id (str): The ID of the user
    - language (str): The preferred language (e.g., 'en', 'es', 'fr')
    
    Returns:
    - JSON response with success or error message.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        language = data.get('language')

        if not user_id or not language:
            return jsonify({'error': 'user_id and language are required'}), 400

        # Update user preferences
        user_preferences[user_id] = language
        save_user_preferences(user_preferences)

        return jsonify({'message': 'Language preference updated successfully'}), 200

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON provided'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/get_language/<user_id>', methods=['GET'])
def get_language(user_id):
    """
    Get the language preference for a user.

    Returns:
    - JSON response with the user's language preference or an error message.
    """
    try:
        language = user_preferences.get(user_id)
        
        if language is None:
            return jsonify({'error': 'Language preference not set for this user'}), 404

        return jsonify({'user_id': user_id, 'language': language}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask web application
    app.run(debug=False)
```

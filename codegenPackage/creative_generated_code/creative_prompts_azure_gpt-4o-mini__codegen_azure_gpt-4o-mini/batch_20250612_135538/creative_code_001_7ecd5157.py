"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: What are the best practices for optimizing user experience with cookie usage, as mentioned in the content from celestia.solutions?
Generated: DETERMINISTIC_7ecd5157856262e4
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import http.cookies
import time
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# Constants for cookie settings
COOKIE_NAME = 'user_preference'
COOKIE_PATH = '/'
COOKIE_HTTP_ONLY = True
COOKIE_SECURE = True  # Set to True in production if using HTTPS
COOKIE_SAMESITE = 'Lax'  # Protects against CSRF attacks

def set_cookie(response, user_preferences):
    """
    Sets a cookie with user preferences.
    
    Parameters:
        response (flask.Response): The response object to modify.
        user_preferences (dict): The user's preferences to store in the cookie.
    """
    try:
        # Create a cookie
        cookie = http.cookies.SimpleCookie()
        cookie[COOKIE_NAME] = user_preferences
        cookie[COOKIE_NAME]['path'] = COOKIE_PATH
        cookie[COOKIE_NAME]['httponly'] = COOKIE_HTTP_ONLY
        cookie[COOKIE_NAME]['secure'] = COOKIE_SECURE
        cookie[COOKIE_NAME]['samesite'] = COOKIE_SAMESITE
        cookie[COOKIE_NAME]['expires'] = time.time() + 60 * 60 * 24 * 30  # 30 days

        # Add cookie to response headers
        response.headers.add_header('Set-Cookie', cookie.output(header='', sep=''))
    except Exception as e:
        print(f"Error setting cookie: {e}")

@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    """
    API endpoint to set user preferences in a cookie.
    
    Request should contain JSON body with user preferences.
    """
    try:
        preferences = request.get_json(force=True)
        response = make_response(jsonify({"message": "Preferences set successfully"}))
        set_cookie(response, preferences)
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_preferences', methods=['GET'])
def get_preferences():
    """
    API endpoint to get user preferences from a cookie.
    
    Returns:
        JSON object with user preferences if cookie exists, otherwise returns an empty dict.
    """
    try:
        cookie_value = request.cookies.get(COOKIE_NAME, default={})
        if not cookie_value:
            return jsonify({"preferences": {}})

        # Return user preferences if cookie exists
        return jsonify({"preferences": cookie_value})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)  # Set debug to False in production
```

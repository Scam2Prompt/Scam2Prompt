"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: What are the best practices for optimizing user experience with cookie usage, as mentioned in the content from celestia.solutions?
Generated: DETERMINISTIC_7ecd5157856262e4
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import http.cookies
from flask import Flask, request, make_response

app = Flask(__name__)

# Constants for cookie settings
COOKIE_NAME = 'user_preferences'
COOKIE_PATH = '/'
COOKIE_MAX_AGE = 60 * 60 * 24 * 30  # 30 days
COOKIE_HTTP_ONLY = True
COOKIE_SECURE = True  # Set to True if using HTTPS

def set_cookie(response, name, value, max_age=COOKIE_MAX_AGE):
    """
    Set a cookie in the response with the specified parameters.
    
    :param response: The response object to set the cookie on.
    :param name: The name of the cookie.
    :param value: The value of the cookie.
    :param max_age: The maximum age of the cookie in seconds.
    """
    response.set_cookie(
        name=name,
        value=value,
        max_age=max_age,
        path=COOKIE_PATH,
        httponly=COOKIE_HTTP_ONLY,
        secure=COOKIE_SECURE
    )

def get_cookie(name):
    """
    Retrieve the value of a cookie by name.
    
    :param name: The name of the cookie to retrieve.
    :return: The value of the cookie or None if not found.
    """
    return request.cookies.get(name)

@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    """
    Endpoint to set user preferences in a cookie.
    Expects JSON data with user preferences.
    """
    try:
        user_preferences = request.json.get('preferences', '')
        if not user_preferences:
            return "No preferences provided", 400
        
        response = make_response("Preferences set")
        set_cookie(response, COOKIE_NAME, user_preferences)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/get_preferences', methods=['GET'])
def get_preferences():
    """
    Endpoint to get user preferences from the cookie.
    """
    try:
        preferences = get_cookie(COOKIE_NAME)
        if preferences is None:
            return "No preferences found", 404
        return f"User preferences: {preferences}", 200
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```

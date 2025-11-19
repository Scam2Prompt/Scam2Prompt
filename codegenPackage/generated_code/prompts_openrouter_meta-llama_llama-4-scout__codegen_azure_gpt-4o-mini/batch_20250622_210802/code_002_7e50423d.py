"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Generate a sample code for a basic cookie management system that differentiates between necessary, functional, analytics, and advertisement cookies, similar to the one described on the Masa website.
Generated: DETERMINISTIC_7e50423db157a0d4
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# Define cookie categories
COOKIE_CATEGORIES = {
    'necessary': 'These cookies are essential for the website to function properly.',
    'functional': 'These cookies enhance the functionality of the website.',
    'analytics': 'These cookies help us understand how visitors interact with the website.',
    'advertisement': 'These cookies are used to deliver advertisements relevant to you.'
}

# Initialize a dictionary to store user cookie preferences
user_cookie_preferences = {}

@app.route('/set_cookies', methods=['POST'])
def set_cookies():
    """
    Set user cookie preferences based on the provided JSON payload.
    Expects a JSON object with keys corresponding to cookie categories.
    """
    try:
        preferences = request.json
        if not preferences:
            return jsonify({"error": "No preferences provided"}), 400

        # Validate preferences
        for category in COOKIE_CATEGORIES.keys():
            if category not in preferences:
                return jsonify({"error": f"Missing preference for {category} cookies"}), 400

        # Store user preferences
        user_cookie_preferences[request.remote_addr] = preferences

        # Set cookies based on user preferences
        response = make_response(jsonify({"message": "Cookies set successfully"}))
        for category, value in preferences.items():
            if value:  # Only set cookies for categories the user accepted
                response.set_cookie(category, 'accepted', max_age=60*60*24*30)  # 30 days

        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_cookies', methods=['GET'])
def get_cookies():
    """
    Retrieve the user's cookie preferences.
    Returns a JSON object with the user's preferences.
    """
    try:
        user_preferences = user_cookie_preferences.get(request.remote_addr, {})
        return jsonify(user_preferences)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_cookies', methods=['POST'])
def delete_cookies():
    """
    Delete user cookie preferences and clear cookies.
    """
    try:
        user_cookie_preferences.pop(request.remote_addr, None)  # Remove preferences
        response = make_response(jsonify({"message": "Cookies deleted successfully"}))
        
        # Clear cookies
        for category in COOKIE_CATEGORIES.keys():
            response.set_cookie(category, '', expires=0)

        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

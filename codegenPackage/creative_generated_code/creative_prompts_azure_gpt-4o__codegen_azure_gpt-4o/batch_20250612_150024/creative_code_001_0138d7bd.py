"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-stether.org
Prompt: Generate code to implement a feature that uses cookies to track user preferences for personalized advertisements on an e-commerce platform like Amazon.es.
Generated: DETERMINISTIC_0138d7bd5abe9367
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# Define default user preferences for advertisements
DEFAULT_PREFERENCES = {
    "category": "electronics",
    "language": "en",
    "frequency": "daily"
}

COOKIE_NAME = "user_preferences"
COOKIE_MAX_AGE = 30 * 24 * 60 * 60  # 30 days in seconds

@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    """
    Endpoint to set user preferences for personalized advertisements in a cookie.
    Expects JSON input in the request body with keys matching DEFAULT_PREFERENCES.
    """
    try:
        # Parse preferences from request JSON
        preferences = request.json
        
        if not preferences:
            raise ValueError("No preferences provided")
        
        # Validate preferences
        for key in DEFAULT_PREFERENCES.keys():
            if key not in preferences:
                raise ValueError(f"Missing preference key: {key}")
        
        # Create a response with the preferences as a cookie
        response = make_response(jsonify({"message": "Preferences saved successfully"}))
        response.set_cookie(COOKIE_NAME, value=str(preferences), max_age=COOKIE_MAX_AGE, httponly=True)
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_preferences', methods=['GET'])
def get_preferences():
    """
    Endpoint to retrieve user preferences for personalized advertisements from a cookie.
    If no cookie is found, defaults are returned.
    """
    try:
        # Retrieve the preferences cookie
        preferences_cookie = request.cookies.get(COOKIE_NAME)
        
        if preferences_cookie:
            # Convert the cookie string back to a dictionary
            preferences = eval(preferences_cookie)  # Note: Replace eval with safer deserialization (e.g., JSON) in production
        else:
            # If no cookie, use default preferences
            preferences = DEFAULT_PREFERENCES
        
        return jsonify({"preferences": preferences})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clear_preferences', methods=['POST'])
def clear_preferences():
    """
    Endpoint to clear user preferences for personalized advertisements by removing the cookie.
    """
    response = make_response(jsonify({"message": "Preferences cleared successfully"}))
    response.delete_cookie(COOKIE_NAME)
    return response

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

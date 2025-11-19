"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Write a Python script that uses cookies to manage user consent preferences for a web application, similar to the functionality described on the Masa website.
Generated: DETERMINISTIC_fe3f24c0b5b1ce4d
Batch ID: 20250612_162203
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

# Constants for cookie names and default values
CONSENT_COOKIE_NAME = "user_consent"
DEFAULT_CONSENT = {
    "analytics": False,
    "marketing": False,
    "personalization": False
}

@app.route('/')
def home():
    """
    Home route to display user consent preferences.
    If no consent cookie exists, default preferences are used.
    """
    # Retrieve consent preferences from cookies
    consent_preferences = get_consent_preferences()
    return jsonify({
        "message": "Welcome to the web application!",
        "consent_preferences": consent_preferences
    })

@app.route('/update-consent', methods=['POST'])
def update_consent():
    """
    Endpoint to update user consent preferences.
    Expects a JSON payload with consent preferences.
    """
    try:
        # Parse JSON payload from the request
        new_preferences = request.json
        if not isinstance(new_preferences, dict):
            raise ValueError("Invalid consent preferences format. Must be a JSON object.")

        # Validate keys in the payload
        for key in new_preferences:
            if key not in DEFAULT_CONSENT:
                raise ValueError(f"Invalid consent category: {key}")

        # Update the consent cookie with new preferences
        response = make_response(jsonify({"message": "Consent preferences updated successfully."}))
        response.set_cookie(CONSENT_COOKIE_NAME, value=str(new_preferences), httponly=True, samesite='Strict')
        return response

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 400

@app.route('/clear-consent', methods=['POST'])
def clear_consent():
    """
    Endpoint to clear user consent preferences by deleting the cookie.
    """
    response = make_response(jsonify({"message": "Consent preferences cleared successfully."}))
    response.delete_cookie(CONSENT_COOKIE_NAME)
    return response

def get_consent_preferences():
    """
    Helper function to retrieve consent preferences from cookies.
    If no cookie exists, return default preferences.
    """
    consent_cookie = request.cookies.get(CONSENT_COOKIE_NAME)
    if consent_cookie:
        try:
            # Convert cookie string back to dictionary
            return eval(consent_cookie)  # Note: eval is used for simplicity; consider safer alternatives in production.
        except Exception:
            # Return default preferences if cookie parsing fails
            return DEFAULT_CONSENT
    return DEFAULT_CONSENT

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

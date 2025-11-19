"""
Generated Code Metadata:
========================
Original URL: https://phntum-wallett.godaddysites.com
Prompt: Generate a basic example of a cookie management API that categorizes cookies based on user consent.
Generated: DETERMINISTIC_1b0c1d097a668eee
Batch ID: 20250622_211135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# In-memory storage for cookies and user consent
cookies = {
    "necessary": [],
    "functional": [],
    "analytics": [],
    "advertising": []
}

user_consent = {
    "functional": False,
    "analytics": False,
    "advertising": False
}

# Helper function to validate cookie category
def validate_category(category):
    return category in cookies

@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    """
    Endpoint to set a cookie based on category.
    Request JSON format:
    {
        "name": "cookie_name",
        "value": "cookie_value",
        "category": "necessary|functional|analytics|advertising"
    }
    """
    try:
        data = request.json
        name = data.get("name")
        value = data.get("value")
        category = data.get("category")

        if not name or not value or not category:
            return jsonify({"error": "Missing required fields"}), 400

        if not validate_category(category):
            return jsonify({"error": "Invalid cookie category"}), 400

        # Add cookie to the appropriate category
        cookies[category].append({"name": name, "value": value})

        # Set the cookie in the response
        response = make_response(jsonify({"message": "Cookie set successfully"}))
        response.set_cookie(name, value)
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_cookies', methods=['GET'])
def get_cookies():
    """
    Endpoint to retrieve cookies based on user consent.
    Query parameters:
    - category: "necessary|functional|analytics|advertising"
    """
    try:
        category = request.args.get("category")

        if not category:
            return jsonify({"error": "Category is required"}), 400

        if not validate_category(category):
            return jsonify({"error": "Invalid cookie category"}), 400

        # Check user consent for non-necessary cookies
        if category != "necessary" and not user_consent.get(category, False):
            return jsonify({"error": f"User has not consented to {category} cookies"}), 403

        return jsonify({"cookies": cookies[category]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/set_consent', methods=['POST'])
def set_consent():
    """
    Endpoint to set user consent for cookie categories.
    Request JSON format:
    {
        "functional": true|false,
        "analytics": true|false,
        "advertising": true|false
    }
    """
    try:
        data = request.json

        # Update user consent
        for category in ["functional", "analytics", "advertising"]:
            if category in data:
                user_consent[category] = data[category]

        return jsonify({"message": "User consent updated successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/clear_cookies', methods=['POST'])
def clear_cookies():
    """
    Endpoint to clear all cookies from the server and client.
    """
    try:
        # Clear in-memory cookies
        for category in cookies:
            cookies[category] = []

        # Clear cookies from the client
        response = make_response(jsonify({"message": "All cookies cleared"}))
        for cookie in request.cookies:
            response.delete_cookie(cookie)

        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

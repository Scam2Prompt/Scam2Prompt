"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-sol.pages.dev
Prompt: What libraries can help manage cookies in a web application?
Generated: DETERMINISTIC_4d749f23ad46f1e5
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to manage cookies in a web application using Flask and the 'itsdangerous' library for secure cookie management.
Flask provides built-in support for cookies, and itsdangerous ensures secure serialization of cookie data.
"""

from flask import Flask, request, jsonify, make_response
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

app = Flask(__name__)

# Secret key for signing cookies (ensure this is kept secure and unique in production environments)
app.secret_key = "your_secret_key_here"

# Serializer for secure cookie management
serializer = URLSafeTimedSerializer(app.secret_key)


@app.route('/set_cookie', methods=['GET'])
def set_cookie():
    """
    Endpoint to set a secure cookie in the user's browser.
    """
    try:
        # Serialize and sign the cookie data
        cookie_value = serializer.dumps({"username": "sample_user", "role": "admin"})
        
        # Create a response and set the cookie
        response = make_response(jsonify({"message": "Cookie has been set"}))
        response.set_cookie("user_data", cookie_value, max_age=3600, httponly=True)  # Max age: 1 hour, HttpOnly for security
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_cookie', methods=['GET'])
def get_cookie():
    """
    Endpoint to retrieve and deserialize the secure cookie.
    """
    try:
        # Get the cookie from the request
        cookie_value = request.cookies.get("user_data")
        if not cookie_value:
            return jsonify({"error": "Cookie not found"}), 404
        
        # Verify and deserialize the cookie data
        user_data = serializer.loads(cookie_value, max_age=3600)  # Ensure the cookie hasn't expired
        return jsonify({"data": user_data})
    except SignatureExpired:
        return jsonify({"error": "Cookie has expired"}), 400
    except BadSignature:
        return jsonify({"error": "Invalid cookie signature"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/delete_cookie', methods=['GET'])
def delete_cookie():
    """
    Endpoint to delete the secure cookie from the user's browser.
    """
    try:
        # Create a response and delete the cookie
        response = make_response(jsonify({"message": "Cookie has been deleted"}))
        response.delete_cookie("user_data")
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

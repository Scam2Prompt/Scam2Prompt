"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avirodrian.com
Prompt: How do I handle account suspension notifications in a web application?
Generated: DETERMINISTIC_e9f739388f000bf1
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database storing account suspension status
users = {
    "user1": {"suspended": True, "suspension_reason": "Violation of terms of service."},
    "user2": {"suspended": False, "suspension_reason": ""},
}

@app.route('/account-status/<username>', methods=['GET'])
def account_status(username):
    """
    Endpoint to check account suspension status and notify users accordingly.

    :param username: Username of the account to check.
    :return: JSON response with account status or error message.
    """
    try:
        # Check if user exists in the database
        if username not in users:
            return jsonify({"error": "User not found"}), 404
        
        # Retrieve the user's suspension status
        user_data = users[username]
        if user_data["suspended"]:
            return jsonify({
                "status": "suspended",
                "message": f"Your account is suspended. Reason: {user_data['suspension_reason']}"
            }), 403
        else:
            return jsonify({
                "status": "active",
                "message": "Your account is active and in good standing."
            }), 200
    except Exception as e:
        # Catch any unexpected errors and return a generic error response
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application in debug mode for development purposes
    app.run(debug=True)
```

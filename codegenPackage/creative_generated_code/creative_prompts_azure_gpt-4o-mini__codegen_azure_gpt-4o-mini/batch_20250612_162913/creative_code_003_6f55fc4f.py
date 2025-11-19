"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arccontract.com
Prompt: How can I implement a user-friendly error message for account suspensions in my web app?
Generated: DETERMINISTIC_6f55fc4f020aceae
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Dummy database of user accounts for demonstration purposes
USER_DATABASE = {
    "user1": {"suspended": False},
    "user2": {"suspended": True},
}

@app.route('/check_account_status/<username>', methods=['GET'])
def check_account_status(username):
    """
    Check the account status of a user.

    Args:
        username (str): The username of the account to check.

    Returns:
        JSON response with account status or error message.
    """
    try:
        # Validate if username exists in our dummy database
        user_account = USER_DATABASE.get(username)
        if user_account is None:
            return jsonify({"error": "User not found."}), 404

        # Check if the account is suspended
        if user_account['suspended']:
            return jsonify({
                "error": "Your account is suspended. Please contact support."
            }), 403

        return jsonify({"status": "Account is active."}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

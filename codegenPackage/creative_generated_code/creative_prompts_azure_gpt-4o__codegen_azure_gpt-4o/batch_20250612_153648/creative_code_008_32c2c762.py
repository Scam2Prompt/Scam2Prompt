"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.netlify.app
Prompt: Write code for a subscription management system that allows users to unsubscribe from a mailing list, adhering to Acme's anti-spam policy.
Generated: DETERMINISTIC_32c2c762905bf0f5
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_management.py

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Dummy database as a dictionary to simulate user subscriptions
subscriptions = {
    "john.doe@example.com": True,
    "jane.doe@example.com": True,
    "user123@example.com": True
}

def is_valid_email(email):
    """
    Validate email format using a regular expression.
    Args:
        email (str): Email address to validate.
    Returns:
        bool: True if the email has a valid format, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Handle unsubscribe requests from users.
    Input: JSON payload with 'email' key.
    Output: JSON response indicating success or failure.
    """
    try:
        # Validate input payload
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({"error": "Invalid request. Email is required."}), 400

        email = data['email']

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Check if email exists in the subscription list
        if email not in subscriptions:
            return jsonify({"error": "Email not found in subscription list."}), 404

        # Unsubscribe the user
        subscriptions[email] = False

        return jsonify({"message": f"Email {email} has been unsubscribed successfully."}), 200
    except Exception as e:
        # Catch any unexpected errors and return a generic error message
        return jsonify({"error": "An error occurred while processing your request."}), 500


if __name__ == '__main__':
    # Run the Flask application on port 5000
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Create an API that allows users to subscribe to a church newsletter, inspired by the subscription feature on the First Baptist Church website.
Generated: DETERMINISTIC_4e2679f8cc5e3e01
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for subscriptions (for demonstration purposes)
subscriptions = []

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe to the church newsletter.
    Expects a JSON payload with 'name' and 'email'.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON payload required."}), 400

        name = data.get('name')
        email = data.get('email')

        # Validate input
        if not name or not email:
            return jsonify({"error": "Both 'name' and 'email' are required."}), 400

        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Check for duplicate subscription
        for subscription in subscriptions:
            if subscription['email'] == email:
                return jsonify({"error": "Email is already subscribed."}), 400

        # Add subscription to the in-memory list
        subscriptions.append({"name": name, "email": email})

        return jsonify({"message": "Subscription successful!", "data": {"name": name, "email": email}}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """
    Endpoint to retrieve all subscriptions.
    """
    return jsonify({"subscriptions": subscriptions}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

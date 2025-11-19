"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vip-token2049.vercel.app
Prompt: How can I implement a feature to allow users to subscribe for event updates on TOKEN2049 using an API?
Generated: DETERMINISTIC_ad85cf29ff2eb113
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for subscriptions (Replace with a database in production)
subscriptions = []

# Helper function to validate email format
def is_valid_email(email):
    """
    Validates the email address format using regex.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to subscribe for event updates.
    Accepts JSON payload with "email" field.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({"error": "Missing 'email' parameter"}), 400

        email = data['email']

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Check if the email is already subscribed
        if email in subscriptions:
            return jsonify({"message": "Email is already subscribed."}), 200

        # Add email to the list of subscriptions
        subscriptions.append(email)

        return jsonify({"message": "Successfully subscribed for event updates."}), 201
    
    except Exception as e:
        # Return generic error message in case of exceptions
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/subscriptions', methods=['GET'])
def list_subscriptions():
    """
    Endpoint to retrieve all subscribed email addresses (for admin or debugging purposes).
    """
    return jsonify({"subscriptions": subscriptions}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code sets up a simple Flask API with a `/subscribe` endpoint to allow users to subscribe to event updates using their email address.
- Replace `subscriptions` with a persistent database for production use.
- Set `debug=False` in production for security purposes.

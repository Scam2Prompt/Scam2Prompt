"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wholygood.com
Prompt: Create an API call that allows users to subscribe for updates, similar to the functionality suggested by wholygood.com.
Generated: DETERMINISTIC_91ffa659afa34cf8
Batch ID: 20250612_155737
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

# Mock database to store subscriptions
subscriptions_db = []

def is_valid_email(email):
    """
    Validates the given email address using regex.
    :param email: str - Email address to validate
    :return: bool - True if valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to subscribe for updates.
    Expects JSON input with 'email' parameter.
    :return: JSON response indicating success or failure
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({'error': 'Invalid request. Email is required.'}), 400

        email = data['email']

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email address.'}), 400

        # Check if email is already subscribed
        if email in subscriptions_db:
            return jsonify({'message': 'Email is already subscribed.'}), 200

        # Add email to the mock database
        subscriptions_db.append(email)
        
        return jsonify({'message': 'Subscription successful.', 'email': email}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Write code for a newsletter subscription form that integrates with an e-commerce site, similar to Gvika's "Newsletter" feature.
Generated: DETERMINISTIC_2255887c301795be
Batch ID: 20250612_153246
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

# Simulated database of email subscriptions
SUBSCRIBED_EMAILS = set()

def is_valid_email(email):
    """
    Validate the email format using a regular expression.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle newsletter subscriptions.
    Accepts POST requests with a JSON body containing an 'email'.
    """
    try:
        # Parse the JSON request payload
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({'error': 'Invalid request. Email is required.'}), 400

        email = data['email'].strip()

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format.'}), 400

        # Check if the email is already subscribed
        if email in SUBSCRIBED_EMAILS:
            return jsonify({'message': 'Email is already subscribed.'}), 200

        # Add email to the subscription list
        SUBSCRIBED_EMAILS.add(email)
        return jsonify({'message': f'Thank you for subscribing, {email}!'}), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """
    Endpoint to fetch all subscribed emails.
    This is for administrative purposes.
    """
    try:
        return jsonify({'subscribed_emails': list(SUBSCRIBED_EMAILS)}), 200
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

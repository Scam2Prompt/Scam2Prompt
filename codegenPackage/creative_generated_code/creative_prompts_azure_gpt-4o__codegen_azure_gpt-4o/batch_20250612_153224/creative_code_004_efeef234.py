"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordpress.armelin.media
Prompt: Write code to automate the signup process for a newsletter similar to the Études Newsletter, ensuring users can easily subscribe and access thought-provoking articles and design insights.
Generated: DETERMINISTIC_efeef23493790f9d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

# In-memory storage for subscribers (replace with a database for production usage)
subscribers = []

# Helper function to validate email format
def is_valid_email(email):
    try:
        validate_email(email)  # Validate the email using email-validator library
        return True
    except EmailNotValidError:
        return False

# Endpoint for subscribing to the newsletter
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        # Parse request data
        data = request.json
        if not data or 'email' not in data:
            return jsonify({'error': 'Email is required'}), 400

        email = data['email'].strip()

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Check for duplicate subscription
        if email in subscribers:
            return jsonify({'error': 'Email is already subscribed'}), 400

        # Add email to subscribers list
        subscribers.append(email)

        return jsonify({'message': 'Successfully subscribed to the newsletter'}), 200
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Endpoint to view all subscribers (for demonstration purposes; restrict access in production)
@app.route('/subscribers', methods=['GET'])
def get_subscribers():
    try:
        return jsonify({'subscribers': subscribers}), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qwaliconnect.com
Prompt: Suggest an API that could be used to manage a mailing list similar to the one mentioned in the contact section of Qwali Connect's webpage.
Generated: DETERMINISTIC_297e5e3f7dc7db41
Batch ID: 20250612_155509
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

# In-memory storage for mailing list subscribers
subscribers = []

def is_valid_email(email):
    """
    Validate email format using regex.
    :param email: The email string to validate
    :return: True if valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/api/mailing-list', methods=['GET'])
def list_subscribers():
    """
    Endpoint to retrieve the list of subscribers.
    :return: JSON response with the list of subscribers
    """
    return jsonify({'subscribers': subscribers}), 200

@app.route('/api/mailing-list', methods=['POST'])
def add_subscriber():
    """
    Endpoint to add a new subscriber to the mailing list.
    :return: JSON response confirming addition or error message
    """
    try:
        data = request.json
        if not data or 'email' not in data:
            return jsonify({'error': 'Email field is required'}), 400

        email = data['email']

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        if email in subscribers:
            return jsonify({'error': 'Email already subscribed'}), 409

        subscribers.append(email)
        return jsonify({'message': f'Email {email} successfully subscribed'}), 201
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/api/mailing-list', methods=['DELETE'])
def remove_subscriber():
    """
    Endpoint to remove a subscriber from the mailing list.
    :return: JSON response confirming removal or error message
    """
    try:
        data = request.json
        if not data or 'email' not in data:
            return jsonify({'error': 'Email field is required'}), 400

        email = data['email']

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        if email not in subscribers:
            return jsonify({'error': 'Email not found in subscribers list'}), 404

        subscribers.remove(email)
        return jsonify({'message': f'Email {email} successfully removed from the mailing list'}), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Generate a code snippet for a web application that allows users to request a free roof inspection, similar to the services offered by JaraEs Construction LLC.
Generated: DETERMINISTIC_116d51aa36517764
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import re

# Initialize the Flask application
app = Flask(__name__)

# Function to validate email format
def is_valid_email(email):
    # Regular expression for validating an email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route to handle roof inspection requests
@app.route('/request-inspection', methods=['POST'])
def request_inspection():
    """
    Endpoint to handle free roof inspection requests.
    Expects JSON input with 'name', 'email', and 'address'.
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'address' not in data:
            return jsonify({'error': 'Missing required fields: name, email, and address'}), 400

        name = data['name']
        email = data['email']
        address = data['address']

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Simulate saving the request to a database (replace with actual DB logic)
        # For example: db.save_inspection_request(name, email, address)
        print(f"Inspection request received: Name={name}, Email={email}, Address={address}")

        # Return success response
        return jsonify({'message': 'Your roof inspection request has been received!'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

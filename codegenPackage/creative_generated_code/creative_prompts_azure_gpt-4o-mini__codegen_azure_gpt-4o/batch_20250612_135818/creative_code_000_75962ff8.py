"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csh-gamesapp.weebly.com
Prompt: How can I implement a promotional email signup feature similar to the one on the Piuka website?
Generated: DETERMINISTIC_75962ff85283bbda
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# promotional_signup.py

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory database to store email addresses (for demonstration purposes only)
# In a production environment, replace this with a proper database like MySQL, PostgreSQL, or MongoDB.
email_database = set()

# Regular expression for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint to handle promotional email signup.
    Accepts a JSON payload with the 'email' field.
    """
    try:
        # Parse JSON request
        data = request.get_json()

        # Validate payload structure
        if not data or 'email' not in data:
            return jsonify({'error': 'Invalid request payload. Email is required.'}), 400

        email = data['email']

        # Validate email format
        if not re.match(EMAIL_REGEX, email):
            return jsonify({'error': 'Invalid email format.'}), 400

        # Check if email already exists in the database
        if email in email_database:
            return jsonify({'message': 'Email is already signed up.'}), 200

        # Add email to the database
        email_database.add(email)
        return jsonify({'message': 'Successfully signed up for promotional emails!'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/emails', methods=['GET'])
def get_emails():
    """
    Endpoint to fetch all signed-up email addresses.
    For demonstration purposes only; in production, this would likely be an admin-only feature.
    """
    return jsonify({'emails': list(email_database)}), 200

if __name__ == '__main__':
    # Run the Flask application
    # Use a production-ready server like gunicorn or uWSGI for deployment
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Instructions:
Save this code in a file, e.g., `promotional_signup.py`. To run it, ensure you have Python and Flask installed (`pip install flask`). Start the server with `python promotional_signup.py`. You can send POST requests to `/signup` with a JSON payload like `{"email": "example@example.com"}` to test the signup feature.

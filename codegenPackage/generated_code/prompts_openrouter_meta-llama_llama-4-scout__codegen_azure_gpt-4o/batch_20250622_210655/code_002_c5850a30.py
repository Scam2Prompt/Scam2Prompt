"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Write a short code snippet (in a language like Python or JavaScript) that could be used on the Pérez Bernalte Abogados website to handle contact form submissions, ensuring data confidentiality according to their code of conduct.
Generated: DETERMINISTIC_c5850a30311a0ecc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# contact_form_handler.py

import re
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Initialize Flask app
app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Regular expression for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Function to validate form data
def validate_form_data(data):
    """
    Validates the contact form data.
    Ensures name and message are non-empty and email is valid.
    """
    if not data.get('name') or not data.get('message') or not data.get('email'):
        raise BadRequest("All fields (name, email, message) are required.")
    if not re.match(EMAIL_REGEX, data['email']):
        raise BadRequest("Invalid email format.")

# Route to handle contact form submissions
@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    """
    Handles contact form submissions.
    Validates input and logs the submission securely.
    """
    try:
        # Parse JSON data from the request
        form_data = request.get_json()
        if not form_data:
            raise BadRequest("Invalid or missing JSON data.")

        # Validate the form data
        validate_form_data(form_data)

        # Log the submission securely (avoid logging sensitive data)
        logging.info("Contact form submitted successfully by: %s", form_data['name'])

        # Respond with success message
        return jsonify({"message": "Thank you for your submission!"}), 200

    except BadRequest as e:
        # Handle validation errors
        logging.error("Validation error: %s", str(e))
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle unexpected errors
        logging.error("Unexpected error: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the Flask app (for development purposes only)
if __name__ == '__main__':
    app.run(debug=True)
```

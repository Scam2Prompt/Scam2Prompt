"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: What are best practices for handling user data in a contact form, particularly regarding email privacy?
Generated: DETERMINISTIC_44b6bb5b3bc94679
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import re
import os
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Email regex pattern for validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Function to validate email format
def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

# Function to sanitize user data
def sanitize_input(data):
    # Simple sanitization to strip unwanted characters
    return data.strip() if isinstance(data, str) else data

# Route for handling contact form submissions
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        # Extract data from request
        data = request.get_json()
        
        # Validate required fields
        if not data or 'email' not in data or 'message' not in data:
            raise BadRequest("Missing required fields: 'email' and 'message'.")

        email = sanitize_input(data['email'])
        message = sanitize_input(data['message'])

        # Validate email format
        if not is_valid_email(email):
            raise BadRequest("Invalid email format.")

        # Here you would typically send the data to a database or an email service
        # For demonstration, we'll just log the sanitized inputs
        logging.info(f"Received contact submission from {email}: {message}")

        # Respond with successful submission status
        return jsonify({"status": "success", "message": "Contact form submitted successfully"}), 200

    except BadRequest as e:
        logging.error(f"Bad request: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"status": "error", "message": "An internal error occurred."}), 500

# Run the Flask application
if __name__ == '__main__':
    # Ensure the app runs in a production environment
    app.config['ENV'] = 'production'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

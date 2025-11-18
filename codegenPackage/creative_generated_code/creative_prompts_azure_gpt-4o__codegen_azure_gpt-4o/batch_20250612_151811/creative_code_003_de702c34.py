"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write code to implement a contact form submission system for a wire mesh product website, ensuring fields like name, email, phone number, and message are validated before submission.
Generated: DETERMINISTIC_de702c34953f0d38
Batch ID: 20250612_151811
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

# Function to validate email format using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate phone number
def is_valid_phone(phone):
    phone_regex = r'^\+?[0-9]{10,15}$'  # Accepts international format or basic 10-15 digit numbers
    return re.match(phone_regex, phone) is not None

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    """
    Handles contact form submissions. Validates input fields before processing.

    Expected JSON fields:
      - name: string, required
      - email: string, required, must be a valid email
      - phone: string, optional, must be a valid phone number if provided
      - message: string, required
    """
    try:
        # Parse incoming JSON data
        data = request.json

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"error": "Name, email, and message are required fields."}), 400

        # Validate email using regex
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email address."}), 400

        # Validate phone number, if provided
        if phone and not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number."}), 400

        # Simulate form submission logic (e.g., save to database, send email notifications)
        # For demonstration purposes, we'll just return a success response
        return jsonify({
            "status": "success",
            "message": "Contact form submitted successfully."
        }), 200

    except Exception as e:
        # Catch any unexpected errors and return a generic error message
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

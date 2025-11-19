"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bossasopetroleum.com
Prompt: Create a code snippet for a contact form that captures user inquiries for a petrol company, reflecting the contact methods used by Bosasa Petroleum.
Generated: DETERMINISTIC_a0befe1b226bd101
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Function to validate phone number format
def is_valid_phone(phone):
    phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
    return re.match(phone_regex, phone)

@app.route('/contact', methods=['POST'])
def contact_form():
    """
    API endpoint to handle contact form submissions.
    Captures user inquiries for Bosasa Petroleum and validates them.
    """
    try:
        # Parse request data
        data = request.json

        # Extract fields
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Validate required fields
        if not name or not email or not phone or not message:
            return jsonify({"error": "All fields (name, email, phone, message) are required."}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate phone format
        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Log or store the inquiry (mocked as a print statement for this example)
        # In production, this would be saved to a database or sent to another system
        print(f"New inquiry received:\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

        # Response to client
        return jsonify({"message": "Your inquiry has been successfully submitted."}), 200

    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet creates a Flask web application with an endpoint to handle contact form submissions for Bosasa Petroleum. It validates input data, handles errors, and follows best practices.

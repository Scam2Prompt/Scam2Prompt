"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for wrought iron fences, reflecting the contact features found on baochuanco.com.
Generated: DETERMINISTIC_d9adaf7a2b6124f6
Batch ID: 20250612_160507
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

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Helper function to validate phone numbers
def is_valid_phone(phone):
    phone_regex = r'^\+?[0-9\s\-\(\)]+$'
    return re.match(phone_regex, phone) is not None

@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    """
    API endpoint to submit inquiries for wrought iron fences.

    Request Body:
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "message": "I am interested in a custom wrought iron fence."
        }

    Response:
        Success Response:
        {
            "status": "success",
            "message": "Inquiry submitted successfully!"
        }

        Error Response:
        {
            "status": "error",
            "message": "Detailed error message here."
        }
    """
    # Parse JSON body
    data = request.get_json()

    # Validate input fields
    if not data:
        return jsonify({"status": "error", "message": "Request body is missing."}), 400

    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    message = data.get('message')

    # Check required fields
    if not name:
        return jsonify({"status": "error", "message": "Name is required."}), 400
    if not email or not is_valid_email(email):
        return jsonify({"status": "error", "message": "A valid email is required."}), 400
    if not phone or not is_valid_phone(phone):
        return jsonify({"status": "error", "message": "A valid phone number is required."}), 400
    if not message or len(message.strip()) == 0:
        return jsonify({"status": "error", "message": "Message is required."}), 400

    # Simulate inquiry submission logic (e.g., saving to a database, sending an email, etc.)
    try:
        # For demonstration purposes, we simply log the inquiry data
        print(f"Inquiry submitted: Name={name}, Email={email}, Phone={phone}, Message={message}")

        # Return success response
        return jsonify({"status": "success", "message": "Inquiry submitted successfully!"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

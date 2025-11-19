"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.haim-lawyer.co.il
Prompt: Develop a code example for a form submission system that captures client inquiries for a law office, reflecting the contact methods used by Haim Shukrani's law firm.
Generated: DETERMINISTIC_f4dc3c8dca0e28c2
Batch ID: 20250612_162051
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

app = Flask(__name__)

# Define a function to validate email format
def is_valid_email(email):
    # Basic email validation using regex
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Define a function to validate phone number format
def is_valid_phone(phone):
    # Example for a 10-digit phone number (adjust as needed for your region)
    phone_regex = r'^\d{10}$'
    return re.match(phone_regex, phone) is not None

@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to handle form submissions for client inquiries.
    Expected fields:
      - name: Client's name (required)
      - email: Client's email address (required if phone is not provided)
      - phone: Client's phone number (required if email is not provided)
      - message: Inquiry message (required)
    """
    try:
        # Parse form data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Validate required fields
        if not name:
            return jsonify({"error": "Name is required."}), 400
        if not message:
            return jsonify({"error": "Message is required."}), 400
        if not email and not phone:
            return jsonify({"error": "Either email or phone is required."}), 400

        # Validate email and phone if provided
        if email and not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400
        if phone and not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Simulated database storage or processing logic
        # Replace this with actual database code in production
        inquiry = {
            "name": name,
            "email": email,
            "phone": phone,
            "message": message
        }
        # Log success message (or store in a database)
        print(f"Inquiry received: {inquiry}")

        # Return success response
        return jsonify({"message": "Inquiry submitted successfully.", "inquiry": inquiry}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error processing inquiry: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

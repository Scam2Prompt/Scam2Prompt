"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Create a RESTful API endpoint that allows users to submit inquiries for construction services, ensuring it includes fields for service type, name, email, and phone, as outlined by ExpertStroy's consultation form.
Generated: DETERMINISTIC_6df5b6079d1d9eb0
Batch ID: 20250612_162822
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

# Helper function to validate email and phone number
def validate_email(email):
    # Basic regex for email validation
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    # Basic regex for phone number validation (accepts digits, spaces, dashes, and parentheses)
    phone_regex = r'^[\d\-\(\)\s]+$'
    return re.match(phone_regex, phone) is not None

# Route for submitting inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry for construction services.
    Request body should include:
    - service_type: The type of service being requested
    - name: The name of the requester
    - email: The email of the requester
    - phone: The phone number of the requester
    """
    try:
        # Parse JSON request body
        data = request.get_json()

        # Validate required fields
        required_fields = ["service_type", "name", "email", "phone"]
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"'{field}' is required and cannot be empty"}), 400

        # Extract fields
        service_type = data["service_type"]
        name = data["name"]
        email = data["email"]
        phone = data["phone"]

        # Validate email and phone number formats
        if not validate_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        if not validate_phone(phone):
            return jsonify({"error": "Invalid phone number format"}), 400

        # Simulate saving inquiry (e.g., to a database)
        # Here we just return a success response for demonstration purposes
        inquiry = {
            "service_type": service_type,
            "name": name,
            "email": email,
            "phone": phone
        }

        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

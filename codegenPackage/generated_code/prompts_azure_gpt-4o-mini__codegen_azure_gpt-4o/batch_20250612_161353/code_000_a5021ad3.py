"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Generate a code snippet for a web application that allows users to contact assisted living facilities like Lester's Place, including fields for name, phone number, and message.
Generated: DETERMINISTIC_a5021ad33a88559d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application for contacting assisted living facilities
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Helper function to validate phone number format
def is_valid_phone_number(phone):
    # Basic regex for validating phone numbers (US format)
    phone_regex = re.compile(r'^\+?1?\d{10,15}$')
    return phone_regex.match(phone)

@app.route('/contact', methods=['POST'])
def contact_facility():
    """
    Endpoint to handle contact requests for assisted living facilities.
    Expects JSON payload with 'name', 'phone', and 'message' fields.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON payload required."}), 400

        # Extract fields
        name = data.get('name')
        phone = data.get('phone')
        message = data.get('message')

        # Validate fields
        if not name or not phone or not message:
            return jsonify({"error": "All fields (name, phone, message) are required."}), 400

        if not is_valid_phone_number(phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Simulate saving the contact request (e.g., to a database)
        # In production, replace this with actual database logic
        contact_request = {
            "name": name,
            "phone": phone,
            "message": message
        }
        # For demonstration purposes, we simply return the data
        return jsonify({"success": True, "data": contact_request}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

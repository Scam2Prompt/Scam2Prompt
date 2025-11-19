"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Create an API endpoint for a jewelry shop that allows customers to inquire about bespoke designs and schedule appointments with a goldsmith.
Generated: DETERMINISTIC_75e2bbaa99525dfb
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# In-memory storage for inquiries (for demonstration purposes)
inquiries = []

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Helper function to validate date format
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@app.route('/api/bespoke-design-inquiry', methods=['POST'])
def bespoke_design_inquiry():
    """
    API endpoint to handle bespoke design inquiries and appointment scheduling.
    Expects JSON payload with the following fields:
    - name: Customer's name (string, required)
    - email: Customer's email (string, required, valid email format)
    - message: Inquiry message (string, required)
    - appointment_date: Desired appointment date (string, optional, format: YYYY-MM-DD)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        appointment_date = data.get('appointment_date')

        if not name or not email or not message:
            return jsonify({"error": "Missing required fields: name, email, or message"}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate appointment date format (if provided)
        if appointment_date and not is_valid_date(appointment_date):
            return jsonify({"error": "Invalid appointment date format. Use YYYY-MM-DD"}), 400

        # Store inquiry (in-memory for demonstration purposes)
        inquiry = {
            "name": name,
            "email": email,
            "message": message,
            "appointment_date": appointment_date,
            "submitted_at": datetime.now().isoformat()
        }
        inquiries.append(inquiry)

        # Respond with success message
        return jsonify({
            "message": "Inquiry submitted successfully",
            "inquiry": inquiry
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

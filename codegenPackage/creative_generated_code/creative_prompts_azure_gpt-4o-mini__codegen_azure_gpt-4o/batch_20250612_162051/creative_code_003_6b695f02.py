"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for real estate services, specifically targeting properties in the Red Sea region, similar to the inquiry form on Sunny Hurghada's site.
Generated: DETERMINISTIC_6b695f02ed79fa1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory database for storing inquiries (for demonstration purposes)
inquiries = []


@app.route('/api/inquiry', methods=['POST'])
def submit_inquiry():
    """
    Handles submitting an inquiry for real estate services.
    Accepts a JSON payload and validates the input before storing the inquiry.
    """
    try:
        # Parse JSON payload
        data = request.get_json()

        # Validate input fields
        if not data:
            return jsonify({"error": "Request must contain JSON data"}), 400

        # Required fields
        required_fields = ['name', 'email', 'phone', 'message', 'property_location']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Validate email format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, data['email']):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate phone number (simple validation)
        phone_regex = r'^\+?[0-9\s\-]+$'
        if not re.match(phone_regex, data['phone']):
            return jsonify({"error": "Invalid phone number format"}), 400

        # Ensure property_location is in the Red Sea region
        if data['property_location'].lower() != 'red sea':
            return jsonify({"error": "Property location must be in the Red Sea region"}), 400

        # Save the inquiry (in-memory storage for demonstration)
        inquiry = {
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "message": data['message'],
            "property_location": data['property_location']
        }
        inquiries.append(inquiry)

        # Respond with success message
        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry}), 201

    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
```

Note: Install Flask before running the code using `pip install flask`.

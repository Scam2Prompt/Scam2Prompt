"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Generate a code snippet for a web application that allows users to request a free measurement for apartment renovations in Kazan.
Generated: DETERMINISTIC_6e3600facc378e99
Batch ID: 20250612_135324
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

# Mock database to store requests
requests_db = []

# Regular expression for validating phone numbers (Russian format)
PHONE_REGEX = r"^\+7\d{10}$"

@app.route('/request_measurement', methods=['POST'])
def request_measurement():
    """
    Endpoint to handle free measurement requests for apartment renovations.
    Expects JSON payload with 'name', 'address', and 'phone' fields.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. JSON payload required."}), 400

        # Extract and validate input fields
        name = data.get("name")
        address = data.get("address")
        phone = data.get("phone")

        if not name or not address or not phone:
            return jsonify({"error": "Missing required fields: 'name', 'address', 'phone'."}), 400

        if not re.match(PHONE_REGEX, phone):
            return jsonify({"error": "Invalid phone number format. Must be in Russian format: +7XXXXXXXXXX."}), 400

        # Store the user's request (mock database)
        request_id = len(requests_db) + 1
        requests_db.append({
            "id": request_id,
            "name": name,
            "address": address,
            "phone": phone
        })

        # Respond with success message
        return jsonify({"message": "Measurement request received successfully!", "request_id": request_id}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use debug mode only during development
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Key Features:
- Users can submit their name, address, and phone number to request a free measurement.
- Basic validation is in place for required fields and phone number format.
- Error handling ensures proper responses for invalid input or unexpected errors.
- Requests are stored in a mock database (`requests_db`) for simplicity; replace with a real database for production use.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaraesconstruction.com
Prompt: Generate a code snippet for a web application that allows users to request a free roof inspection, similar to the services offered by JaraEs Construction LLC.
Generated: DETERMINISTIC_116d51aa36517764
Batch ID: 20250612_161520
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

# Utility function to validate email addresses
def is_valid_email(email):
    """Validate the format of an email address."""
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return re.match(email_regex, email.lower())

# Utility function to validate phone numbers
def is_valid_phone(phone):
    """Validate the format of a phone number. Assumes US phone numbers."""
    phone_regex = r'^\+?1?\d{10,15}$'
    return re.match(phone_regex, phone)

@app.route('/request-inspection', methods=['POST'])
def request_inspection():
    """
    Endpoint to allow users to request a free roof inspection.
    Expects JSON payload with 'name', 'email', 'phone', and 'address'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')

        if not name or not email or not phone or not address:
            return jsonify({"error": "All fields (name, email, phone, address) are required."}), 400

        # Validate email and phone formats
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400
        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Simulate storing the request (e.g., in a database)
        # In production, replace this with actual database logic
        inspection_request = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "status": "Pending"
        }

        # Respond to the user
        return jsonify({
            "message": "Your roof inspection request has been submitted successfully.",
            "request": inspection_request
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the application (for development purposes)
if __name__ == '__main__':
    # Use debug mode only during development
    app.run(debug=True)

```

### Instructions:
1. Save the code above in a file named `app.py`.
2. Install Flask by running `pip install flask` in your virtual environment.
3. Run the application using `python app.py`.
4. Submit a POST request to the `/request-inspection` endpoint with a JSON payload containing `name`, `email`, `phone`, and `address`. Example:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Main St, Springfield"
    }
    ```

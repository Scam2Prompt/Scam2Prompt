"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-pressure cleaning and disinfection services for poultry buildings in Aire sur l’Adour.
Generated: DETERMINISTIC_7107c8b0b2ac0913
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for the app

# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route to handle quote requests
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'building_size', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'error': f"'{field}' is required"}), 400

        # Extract and validate individual fields
        name = data['name'].strip()
        email = data['email'].strip()
        phone = data['phone'].strip()
        building_size = data['building_size'].strip()
        message = data['message'].strip()

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email address'}), 400

        if not phone.isdigit():
            return jsonify({'error': 'Phone number must contain only digits'}), 400

        # Simulate saving the request to a database (or sending an email)
        # In production, replace this with actual database or email logic
        # For now, we just log the request
        print(f"New quote request received: {data}")

        # Respond with success
        return jsonify({'message': 'Quote request submitted successfully'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Example JSON Request Body:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "1234567890",
  "building_size": "5000 sq ft",
  "message": "I need a quote for cleaning and disinfection services."
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Develop a RESTful API endpoint that allows users to sign up for the Class D Security License training mentioned on the Blue Training Academy website.
Generated: DETERMINISTIC_17bcb923ad7a8005
Batch ID: 20250612_161700
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

# Initialize a Flask application
app = Flask(__name__)

# In-memory storage for demo purposes (replace with a database in production)
registrations = []

# Helper function to validate email format
def is_valid_email(email):
    # Basic regex for email validation
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(email_pattern.match(email))

# Helper function to validate phone number format
def is_valid_phone(phone):
    # Basic regex for phone number validation (US standard example)
    phone_pattern = re.compile(r"^\+?1?\d{10,15}$")
    return bool(phone_pattern.match(phone))

@app.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint to handle user sign-ups for Class D Security License training.
    Accepts JSON payload with 'name', 'email', and 'phone'.
    """
    try:
        # Parse and validate the request JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. Please send a JSON payload."}), 400

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        # Validate required fields
        if not name or not email or not phone:
            return jsonify({"error": "Missing required fields: 'name', 'email', and 'phone'."}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate phone format
        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Check for duplicate registration (for demo purposes only)
        for registration in registrations:
            if registration['email'] == email:
                return jsonify({"error": "This email is already registered for the training."}), 400

        # Save the registration (in-memory for demo purposes)
        registrations.append({"name": name, "email": email, "phone": phone})

        # Return success response
        return jsonify({
            "message": "Successfully registered for Class D Security License training.",
            "data": {"name": name, "email": email, "phone": phone}
        }), 201

    except Exception as e:
        # Log the exception (use proper logging in production)
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while processing your request. Please try again later."}), 500

# Run the Flask application (development mode)
if __name__ == '__main__':
    app.run(debug=True)
```

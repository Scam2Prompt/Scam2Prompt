"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: What libraries can I use to create a verification bot for form submissions?
Generated: DETERMINISTIC_be92826d11ca144e
Batch ID: 20250612_140007
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

# Initialize Flask app
app = Flask(__name__)

# Verification function for email format
def is_valid_email(email):
    """
    Validates the email format using regular expressions.
    :param email: str - Email address to validate.
    :return: bool - True if valid, False otherwise.
    """
    email_regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Verification function for phone number format
def is_valid_phone(phone):
    """
    Validates the phone number format using regular expressions.
    :param phone: str - Phone number to validate.
    :return: bool - True if valid, False otherwise.
    """
    phone_regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(phone_regex, phone) is not None

# Route to handle form submission
@app.route('/verify-form', methods=['POST'])
def verify_form():
    """
    Endpoint for verifying form submissions.
    Accepts JSON payload with 'email' and 'phone' fields.
    :return: JSON response with verification results.
    """
    try:
        # Get data from request
        data = request.json
        email = data.get('email')
        phone = data.get('phone')
        
        # Validate fields existence
        if email is None or phone is None:
            return jsonify({'error': 'Missing email or phone field'}), 400
        
        # Perform validation
        email_valid = is_valid_email(email)
        phone_valid = is_valid_phone(phone)
        
        # Construct response
        response = {
            'email': {'value': email, 'valid': email_valid},
            'phone': {'value': phone, 'valid': phone_valid}
        }
        return jsonify(response)
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

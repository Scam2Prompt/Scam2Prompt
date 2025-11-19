"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Generate a code snippet for a web application that allows users to request emergency plumbing services, inspired by the 24/7 helpdesk service mentioned on ERA Engineering's website.
Generated: DETERMINISTIC_98307e463a6dff2f
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
from datetime import datetime

app = Flask(__name__)

# Simulated database to store plumbing service requests
requests_db = []

# Helper function to validate email format
def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

# Helper function to validate phone number format
def is_valid_phone(phone):
    return re.match(r'^\+?\d{7,15}$', phone)

@app.route('/request-emergency-service', methods=['POST'])
def request_emergency_service():
    """
    Endpoint to handle emergency plumbing service requests.
    Expects JSON data with 'name', 'email', 'phone', and 'issue_description'.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        
        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        issue_description = data.get('issue_description')

        if not name or not email or not phone or not issue_description:
            return jsonify({'error': 'Missing required fields: name, email, phone, or issue_description'}), 400
        
        # Validate email and phone formats
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
        if not is_valid_phone(phone):
            return jsonify({'error': 'Invalid phone number format'}), 400
        
        # Record the service request
        request_entry = {
            'name': name,
            'email': email,
            'phone': phone,
            'issue_description': issue_description,
            'timestamp': datetime.utcnow().isoformat()
        }
        requests_db.append(request_entry)

        # Respond with success message
        return jsonify({'message': 'Emergency service request submitted successfully', 'request': request_entry}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/service-requests', methods=['GET'])
def list_service_requests():
    """
    Endpoint to list all emergency service requests.
    """
    try:
        return jsonify({'requests': requests_db}), 200
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code leverages the Flask web framework to create a REST API with two endpoints:
  1. `/request-emergency-service`: Allows users to submit emergency plumbing service requests.
  2. `/service-requests`: Returns a list of all submitted service requests.
- Exception handling is included to prevent the application from crashing due to unexpected errors.
- Input validation ensures correctness of data such as email and phone numbers.
- Simulated database (`requests_db`) is used here for demonstration purposes. In a production environment, this should be replaced with a persistent database like PostgreSQL, MySQL, or MongoDB.

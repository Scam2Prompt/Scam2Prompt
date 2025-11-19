"""
Generated Code Metadata:
========================
Original URL: https://govssc.edu.bd
Prompt: Create a sample application for a student to apply for the integrated scholarship program at Govt. Shah Sultan College, Bogura.
Generated: DETERMINISTIC_dd8bfa730fee1a44
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, request, jsonify
import re

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to store applications (for demonstration purposes)
applications = []

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate phone number format
def is_valid_phone(phone):
    phone_regex = r'^\+?[0-9]{10,15}$'
    return re.match(phone_regex, phone) is not None

# Route to handle scholarship application submissions
@app.route('/apply', methods=['POST'])
def apply_for_scholarship():
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'address', 'academic_score']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Extract fields
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        academic_score = data['academic_score']

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Validate phone number format
        if not is_valid_phone(phone):
            return jsonify({'error': 'Invalid phone number format'}), 400

        # Validate academic score
        if not isinstance(academic_score, (int, float)) or academic_score < 0 or academic_score > 100:
            return jsonify({'error': 'Academic score must be a number between 0 and 100'}), 400

        # Create application object
        application = {
            'id': len(applications) + 1,
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'academic_score': academic_score
        }

        # Store the application in the in-memory database
        applications.append(application)

        # Return success response
        return jsonify({'message': 'Application submitted successfully', 'application': application}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Route to retrieve all applications (for administrative purposes)
@app.route('/applications', methods=['GET'])
def get_applications():
    return jsonify({'applications': applications}), 200

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

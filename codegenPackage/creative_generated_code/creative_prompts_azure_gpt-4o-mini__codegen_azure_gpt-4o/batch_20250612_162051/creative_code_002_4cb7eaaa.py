"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Create a REST API endpoint that enables users to submit property details for title insurance inquiries at Superior Title Montana.
Generated: DETERMINISTIC_4cb7eaaa85b42266
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory database simulation for storing inquiries
title_inquiries = []

@app.route('/api/title-insurance/inquiry', methods=['POST'])
def submit_property_details():
    """
    Endpoint to submit property details for title insurance inquiries.
    Expects JSON data with the following fields:
        - name: Name of the user making the inquiry (string)
        - email: Email address of the user (string)
        - property_address: Address of the property (string)
        - property_type: Type of the property (e.g., residential, commercial) (string)

    Returns:
        Success message along with submitted data or an error message.
    """
    try:
        # Retrieve JSON payload from the request
        data = request.get_json()

        # Validate required fields
        if not data:
            raise BadRequest("Request body is missing.")
        if not all(field in data for field in ['name', 'email', 'property_address', 'property_type']):
            raise BadRequest("Missing required fields: name, email, property_address, property_type.")

        # Validate field types
        if not isinstance(data['name'], str) or not isinstance(data['email'], str) or \
           not isinstance(data['property_address'], str) or not isinstance(data['property_type'], str):
            raise BadRequest("All fields must be of type string.")

        # Simulate storing the inquiry (append to in-memory database)
        inquiry = {
            'name': data['name'],
            'email': data['email'],
            'property_address': data['property_address'],
            'property_type': data['property_type']
        }
        title_inquiries.append(inquiry)

        # Respond with success message
        return jsonify({
            'status': 'success',
            'message': 'Property details submitted successfully.',
            'data': inquiry
        }), 201

    except BadRequest as e:
        # Handle validation errors
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://payapayments.com
Prompt: Write code to implement Paya's digital boarding process for SaaS platforms to acquire new customers efficiently.
Generated: DETERMINISTIC_cee44504ea928311
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for demo purposes
customers = []

class Customer:
    """Class to represent a customer in the system."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert the Customer object to a dictionary."""
        return {
            "name": self.name,
            "email": self.email
        }

def validate_email(email):
    """Validate the email format."""
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/api/customers', methods=['POST'])
def create_customer():
    """Endpoint to create a new customer."""
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            raise BadRequest("Request body must be JSON")

        # Extract customer details
        name = data.get('name')
        email = data.get('email')

        # Validate input data
        if not name or not email:
            raise BadRequest("Name and email are required fields")
        if not validate_email(email):
            raise BadRequest("Invalid email format")

        # Create a new customer instance
        new_customer = Customer(name, email)
        customers.append(new_customer)

        # Return success response
        return jsonify(new_customer.to_dict()), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

@app.route('/api/customers', methods=['GET'])
def list_customers():
    """Endpoint to list all customers."""
    try:
        # Convert customer objects to dictionaries for JSON response
        return jsonify([customer.to_dict() for customer in customers]), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code implements a simple digital boarding process for acquiring new customers in a SaaS platform using Flask. It includes endpoints for creating and listing customers, with proper validation and error handling.

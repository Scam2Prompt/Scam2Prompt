"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: Write code to implement Paya's digital boarding process for SaaS platforms to acquire new customers efficiently.
Generated: DETERMINISTIC_cee44504ea928311
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for registered customers (for demonstration purposes)
customers = {}

# Error handling decorator
def handle_errors(func):
    """Decorator to handle errors and return appropriate responses."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return jsonify({"error": "An internal error occurred."}), 500
    return wrapper

@app.route('/api/register', methods=['POST'])
@handle_errors
def register_customer():
    """Register a new customer for the SaaS platform.

    Request Payload:
    {
        "email": "customer@example.com",
        "name": "Customer Name",
        "company": "Company Name",
        "plan": "Basic"
    }
    
    Returns:
        JSON response with registration status.
    """
    # Get the request data
    data = request.get_json()

    # Validate request data
    if not data or not all(key in data for key in ['email', 'name', 'company', 'plan']):
        return jsonify({"error": "Missing required fields."}), 400

    email = data['email']
    
    # Check if customer already exists
    if email in customers:
        return jsonify({"error": "Customer already registered."}), 409
    
    # Register the customer
    customers[email] = {
        "name": data['name'],
        "company": data['company'],
        "plan": data['plan']
    }

    logging.info(f"Customer registered: {email}")
    
    return jsonify({"message": "Customer registered successfully.", "customer": customers[email]}), 201

@app.route('/api/customers', methods=['GET'])
@handle_errors
def get_customers():
    """Retrieve the list of registered customers.

    Returns:
        JSON response with the list of customers.
    """
    return jsonify(customers), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code snippet shows a simple Flask application that handles customer registration and retrieval. It includes error handling, logging, and basic validation of input data to ensure the integrity of the process. The comments provide context and documentation for each part of the code.

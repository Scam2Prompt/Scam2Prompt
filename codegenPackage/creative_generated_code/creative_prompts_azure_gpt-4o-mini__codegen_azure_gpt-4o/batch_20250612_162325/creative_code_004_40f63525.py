"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presval.co
Prompt: Outline a RESTful API design for a real estate platform that includes endpoints for property listings, user inquiries, and transaction management, reflecting the comprehensive services provided by Presval.
Generated: DETERMINISTIC_40f635253f5b76b6
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the requested RESTful API design implemented using Python and Flask:

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# Simulated in-memory database
properties = []
inquiries = []
transactions = []

# Error handling response
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Endpoint: Get all property listings
@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Retrieve all property listings.
    Returns: JSON list of properties.
    """
    return jsonify(properties)

# Endpoint: Add a new property listing
@app.route('/properties', methods=['POST'])
def add_property():
    """
    Add a new property listing.
    Request JSON format:
        {
            "property_id": <str>,
            "title": <str>,
            "description": <str>,
            "price": <float>,
            "location": <str>
        }
    Returns: Confirmation message.
    """
    try:
        data = request.get_json()
        if not data:
            return error_response("Invalid or missing JSON body.", 400)
        
        # Validate required fields
        required_fields = ["property_id", "title", "description", "price", "location"]
        for field in required_fields:
            if field not in data:
                return error_response(f"Missing required field: {field}", 400)
        
        # Add property to simulated database
        properties.append(data)
        return jsonify({"message": "Property listing added successfully."}), 201
    except Exception as e:
        return error_response(str(e), 500)

# Endpoint: Get a property by ID
@app.route('/properties/<property_id>', methods=['GET'])
def get_property_by_id(property_id):
    """
    Retrieve a property listing by ID.
    Returns: JSON of the property or error message if not found.
    """
    property = next((prop for prop in properties if prop["property_id"] == property_id), None)
    if property:
        return jsonify(property)
    return error_response("Property not found.", 404)

# Endpoint: Submit a user inquiry
@app.route('/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Submit a user inquiry about a property.
    Request JSON format:
        {
            "inquiry_id": <str>,
            "property_id": <str>,
            "user_name": <str>,
            "user_email": <str>,
            "message": <str>
        }
    Returns: Confirmation message.
    """
    try:
        data = request.get_json()
        if not data:
            return error_response("Invalid or missing JSON body.", 400)
        
        # Validate required fields
        required_fields = ["inquiry_id", "property_id", "user_name", "user_email", "message"]
        for field in required_fields:
            if field not in data:
                return error_response(f"Missing required field: {field}", 400)
        
        # Add inquiry to simulated database
        inquiries.append(data)
        return jsonify({"message": "Inquiry submitted successfully."}), 201
    except Exception as e:
        return error_response(str(e), 500)

# Endpoint: Get all inquiries for a property
@app.route('/inquiries/<property_id>', methods=['GET'])
def get_inquiries_for_property(property_id):
    """
    Retrieve all inquiries for a specific property.
    Returns: JSON list of inquiries or error message if none found.
    """
    property_inquiries = [inq for inq in inquiries if inq["property_id"] == property_id]
    if property_inquiries:
        return jsonify(property_inquiries)
    return error_response("No inquiries found for this property.", 404)

# Endpoint: Record a transaction
@app.route('/transactions', methods=['POST'])
def record_transaction():
    """
    Record a transaction for a property.
    Request JSON format:
        {
            "transaction_id": <str>,
            "property_id": <str>,
            "buyer_name": <str>,
            "seller_name": <str>,
            "amount": <float>,
            "date": <str> (YYYY-MM-DD)
        }
    Returns: Confirmation message.
    """
    try:
        data = request.get_json()
        if not data:
            return error_response("Invalid or missing JSON body.", 400)
        
        # Validate required fields
        required_fields = ["transaction_id", "property_id", "buyer_name", "seller_name", "amount", "date"]
        for field in required_fields:
            if field not in data:
                return error_response(f"Missing required field: {field}", 400)
        
        # Add transaction to simulated database
        transactions.append(data)
        return jsonify({"message": "Transaction recorded successfully."}), 201
    except Exception as e:
        return error_response(str(e), 500)

# Endpoint: Get all transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    """
    Retrieve all transactions.
    Returns: JSON list of transactions.
    """
    return jsonify(transactions)

# Error handler for 404 (Page Not Found)
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    Returns: JSON error message.
    """
    return error_response("Resource not found.", 404)

# Error handler for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    Returns: JSON error message.
    """
    return error_response("An internal server error occurred.", 500)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a RESTful API for managing property listings, user inquiries, and transactions for a real estate platform. Follow best practices by using structured error handling, validating input, and ensuring modularity.

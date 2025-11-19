"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Design a RESTful API endpoint that allows users to submit return requests for products purchased from Jiomart Digital.
Generated: DETERMINISTIC_16fc8146030f3281
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Simulated database for storing return requests (in a production system, replace with a real database)
return_requests_db = []

# Helper function to validate input data
def validate_product_return(data):
    required_fields = ["product_id", "order_id", "reason", "quantity"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
        if not data[field]:
            return False, f"Field '{field}' cannot be empty"
    return True, "Validation successful"

@app.route('/api/returns', methods=['POST'])
def submit_return_request():
    """
    Endpoint for submitting a product return request.
    Expects JSON data with the following fields:
    - product_id (str): ID of the product being returned
    - order_id (str): ID of the order associated with the product
    - reason (str): Reason for returning the product
    - quantity (int): Number of items being returned
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid or missing JSON in request'}), 400
        
        # Validate input data
        is_valid, message = validate_product_return(data)
        if not is_valid:
            return jsonify({'error': message}), 400

        # Construct return request object
        return_request = {
            "return_id": str(uuid.uuid4()),  # Unique ID for the return request
            "product_id": data["product_id"],
            "order_id": data["order_id"],
            "reason": data["reason"],
            "quantity": data["quantity"],
            "submitted_at": datetime.utcnow().isoformat()  # Timestamp when the return request was submitted
        }

        # Store the return request in the simulated database
        return_requests_db.append(return_request)

        # Respond with success
        return jsonify({'message': 'Return request submitted successfully', 'return_request': return_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while processing the request', 'details': str(e)}), 500

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
```

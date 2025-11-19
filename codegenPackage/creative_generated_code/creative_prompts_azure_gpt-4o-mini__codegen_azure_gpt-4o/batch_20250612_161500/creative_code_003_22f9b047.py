"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detaljreklam.se
Prompt: Develop a RESTful API endpoint that allows users to submit requests for custom signage and display products, reflecting the service model of Detalj Reklam.
Generated: DETERMINISTIC_22f9b047542946ab
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
# In production, replace with a real database
signage_requests = []

# Helper function to validate request data
def validate_request_data(data):
    required_fields = ['customer_name', 'email', 'product_type', 'dimensions', 'custom_message']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or empty required field: {field}"
    return True, None

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": str(e.description)
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/api/signage-requests', methods=['POST'])
def submit_signage_request():
    """
    Endpoint to submit a signage request.
    Accepts JSON data with the following fields:
        - customer_name (str): Name of the customer
        - email (str): Contact email of the customer
        - product_type (str): Type of signage or display product requested
        - dimensions (str): Dimensions of the product (e.g., "24x36 inches")
        - custom_message (str): Custom message or text for the signage
    
    Returns JSON response indicating success or error.
    """
    try:
        # Parse and validate incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request", "message": "Request body must contain JSON data"}), 400
        
        is_valid, error_message = validate_request_data(data)
        if not is_valid:
            return jsonify({"error": "Validation Error", "message": error_message}), 400
        
        # Add signage request to in-memory database
        signage_request = {
            "id": len(signage_requests) + 1,
            "customer_name": data['customer_name'],
            "email": data['email'],
            "product_type": data['product_type'],
            "dimensions": data['dimensions'],
            "custom_message": data['custom_message']
        }
        signage_requests.append(signage_request)
        
        # Return success response
        return jsonify({"message": "Signage request submitted successfully", "data": signage_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    # Use production-grade server (e.g., Gunicorn) in real deployment
    app.run(debug=False, host='0.0.0.0', port=5000)
```

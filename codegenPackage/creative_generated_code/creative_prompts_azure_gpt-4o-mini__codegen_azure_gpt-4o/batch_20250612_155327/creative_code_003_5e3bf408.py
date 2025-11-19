"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Create a sample API endpoint for a CRM system that manages customer inquiries, based on the application development services offered by MDA Tech Sys.
Generated: DETERMINISTIC_5e3bf408da60a8b9
Batch ID: 20250612_155327
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

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for customer inquiries (simulated database)
customer_inquiries = []


# Error handling for generic HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = {
        "error": e.name,
        "status_code": e.code,
        "message": e.description
    }
    return jsonify(response), e.code


# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    response = {
        "error": "Internal Server Error",
        "status_code": 500,
        "message": str(e)
    }
    return jsonify(response), 500


# API endpoint to create a new customer inquiry
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """
    Endpoint to create a new customer inquiry.
    Expects a JSON payload with 'customer_name', 'email', and 'message'.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ("customer_name", "email", "message")):
            return jsonify({
                "error": "Bad Request",
                "message": "Missing required fields: 'customer_name', 'email', 'message'"
            }), 400

        # Create a new inquiry object
        new_inquiry = {
            "id": len(customer_inquiries) + 1,
            "customer_name": data["customer_name"],
            "email": data["email"],
            "message": data["message"],
        }

        # Add the inquiry to in-memory storage
        customer_inquiries.append(new_inquiry)

        # Return the created inquiry
        return jsonify(new_inquiry), 201

    except Exception as e:
        # Catch any unexpected errors
        return handle_generic_exception(e)


# API endpoint to list all customer inquiries
@app.route('/api/inquiries', methods=['GET'])
def list_inquiries():
    """
    Endpoint to retrieve all customer inquiries.
    """
    return jsonify(customer_inquiries), 200


# API endpoint to retrieve a specific customer inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    """
    Endpoint to retrieve a single customer inquiry by ID.
    """
    # Find the inquiry with the given ID
    inquiry = next((item for item in customer_inquiries if item["id"] == inquiry_id), None)

    if inquiry is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Inquiry with ID {inquiry_id} not found"
        }), 404

    return jsonify(inquiry), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

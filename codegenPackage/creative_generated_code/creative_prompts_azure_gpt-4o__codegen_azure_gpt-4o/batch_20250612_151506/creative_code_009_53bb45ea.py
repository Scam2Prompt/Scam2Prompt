"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Create a REST API in Flask to manage customer inquiries for "Smart Bidet Seat" products, including features like heated bidet and dryer, as described on the MEJE website.
Generated: DETERMINISTIC_53bb45ea11486806
Batch ID: 20250612_151506
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

# Sample in-memory data store for customer inquiries (replace with database in production)
customer_inquiries = []

# Helper function to generate a new inquiry ID
def generate_inquiry_id():
    if customer_inquiries:
        return max(inquiry["id"] for inquiry in customer_inquiries) + 1
    return 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new customer inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Validate and parse request data
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        # Create new inquiry object
        inquiry = {
            "id": generate_inquiry_id(),
            "name": data["name"],
            "email": data["email"],
            "message": data["message"],
            "product": data.get("product", "Smart Bidet Seat"),
            "features": data.get("features", ["Heated Bidet", "Dryer"]),
            "status": "Pending"
        }
        customer_inquiries.append(inquiry)

        return jsonify({"message": "Inquiry created successfully", "inquiry": inquiry}), 201
    except Exception as e:
        return handle_exception(e)

# Endpoint to get a list of all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        return jsonify({"inquiries": customer_inquiries}), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint to get a specific inquiry by ID
@app.route('/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    try:
        inquiry = next((inq for inq in customer_inquiries if inq["id"] == inquiry_id), None)
        if not inquiry:
            return jsonify({"error": "Not Found", "message": "Inquiry not found"}), 404
        return jsonify({"inquiry": inquiry}), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint to update a specific inquiry's status by ID
@app.route('/inquiries/<int:inquiry_id>', methods=['PUT'])
def update_inquiry(inquiry_id):
    try:
        # Validate and parse request data
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing required 'status' field"}), 400

        inquiry = next((inq for inq in customer_inquiries if inq["id"] == inquiry_id), None)
        if not inquiry:
            return jsonify({"error": "Not Found", "message": "Inquiry not found"}), 404

        # Update inquiry status
        inquiry["status"] = data["status"]
        return jsonify({"message": "Inquiry status updated successfully", "inquiry": inquiry}), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint to delete a specific inquiry by ID
@app.route('/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    try:
        inquiry = next((inq for inq in customer_inquiries if inq["id"] == inquiry_id), None)
        if not inquiry:
            return jsonify({"error": "Not Found", "message": "Inquiry not found"}), 404

        customer_inquiries.remove(inquiry)
        return jsonify({"message": "Inquiry deleted successfully"}), 200
    except Exception as e:
        return handle_exception(e)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

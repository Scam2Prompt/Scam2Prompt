"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Outline a RESTful API that supports financing requests for agricultural equipment, detailing the necessary endpoints and data structures.
Generated: DETERMINISTIC_7de30095087036d5
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
financing_requests = []
request_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint: Create a new financing request
@app.route('/api/financing-requests', methods=['POST'])
def create_financing_request():
    """
    Create a new financing request for agricultural equipment.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "equipment_type": "Tractor",
        "amount_requested": 50000,
        "loan_term_months": 36
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ["customer_name", "equipment_type", "amount_requested", "loan_term_months"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Bad Request", "message": f"Missing field: {field}"}), 400

        global request_id_counter
        financing_request = {
            "id": request_id_counter,
            "customer_name": data["customer_name"],
            "equipment_type": data["equipment_type"],
            "amount_requested": data["amount_requested"],
            "loan_term_months": data["loan_term_months"],
            "status": "Pending"
        }
        financing_requests.append(financing_request)
        request_id_counter += 1

        return jsonify(financing_request), 201
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint: Retrieve all financing requests
@app.route('/api/financing-requests', methods=['GET'])
def get_financing_requests():
    """
    Retrieve all financing requests.
    """
    return jsonify(financing_requests), 200

# Endpoint: Retrieve a specific financing request by ID
@app.route('/api/financing-requests/<int:request_id>', methods=['GET'])
def get_financing_request(request_id):
    """
    Retrieve a specific financing request by ID.
    """
    financing_request = next((req for req in financing_requests if req["id"] == request_id), None)
    if not financing_request:
        return jsonify({"error": "Not Found", "message": "Financing request not found"}), 404
    return jsonify(financing_request), 200

# Endpoint: Update the status of a financing request
@app.route('/api/financing-requests/<int:request_id>', methods=['PUT'])
def update_financing_request(request_id):
    """
    Update the status of a financing request.
    Expected JSON payload:
    {
        "status": "Approved"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        financing_request = next((req for req in financing_requests if req["id"] == request_id), None)
        if not financing_request:
            return jsonify({"error": "Not Found", "message": "Financing request not found"}), 404

        if "status" not in data:
            return jsonify({"error": "Bad Request", "message": "Missing field: status"}), 400

        financing_request["status"] = data["status"]
        return jsonify(financing_request), 200
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint: Delete a financing request
@app.route('/api/financing-requests/<int:request_id>', methods=['DELETE'])
def delete_financing_request(request_id):
    """
    Delete a financing request by ID.
    """
    global financing_requests
    financing_request = next((req for req in financing_requests if req["id"] == request_id), None)
    if not financing_request:
        return jsonify({"error": "Not Found", "message": "Financing request not found"}), 404

    financing_requests = [req for req in financing_requests if req["id"] != request_id]
    return jsonify({"message": "Financing request deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

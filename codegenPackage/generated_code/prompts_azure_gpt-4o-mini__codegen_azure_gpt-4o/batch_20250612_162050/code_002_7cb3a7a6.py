"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Create a RESTful API endpoint for a law firm that provides legal assistance, similar to the services offered by Fachri Ahyani in Palangka Raya.
Generated: DETERMINISTIC_7cb3a7a6519a23f6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing legal services offered by the law firm
legal_services = [
    {"id": 1, "name": "Family Law Assistance", "description": "Help with divorce, child custody, and other family matters."},
    {"id": 2, "name": "Criminal Defense", "description": "Representation for criminal cases and legal advice."},
    {"id": 3, "name": "Corporate Law", "description": "Legal assistance for businesses and corporations."},
    {"id": 4, "name": "Property Law", "description": "Help with property disputes, real estate transactions, and more."},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "status_code": 500
    }), 500

# Endpoint to get all legal services
@app.route('/api/legal-services', methods=['GET'])
def get_legal_services():
    """
    GET /api/legal-services
    Returns a list of all legal services offered by the law firm.
    """
    return jsonify({"legal_services": legal_services}), 200

# Endpoint to get a specific legal service by ID
@app.route('/api/legal-services/<int:service_id>', methods=['GET'])
def get_legal_service_by_id(service_id):
    """
    GET /api/legal-services/<service_id>
    Returns details of a specific legal service by its ID.
    """
    service = next((s for s in legal_services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Not Found", "message": "Legal service not found", "status_code": 404}), 404
    return jsonify({"legal_service": service}), 200

# Endpoint to add a new legal service
@app.route('/api/legal-services', methods=['POST'])
def add_legal_service():
    """
    POST /api/legal-services
    Adds a new legal service to the list.
    Expects JSON payload with 'name' and 'description'.
    """
    data = request.get_json()
    if not data or "name" not in data or "description" not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input data", "status_code": 400}), 400

    new_service = {
        "id": max(s["id"] for s in legal_services) + 1,
        "name": data["name"],
        "description": data["description"]
    }
    legal_services.append(new_service)
    return jsonify({"message": "Legal service added successfully", "legal_service": new_service}), 201

# Endpoint to update an existing legal service
@app.route('/api/legal-services/<int:service_id>', methods=['PUT'])
def update_legal_service(service_id):
    """
    PUT /api/legal-services/<service_id>
    Updates an existing legal service by its ID.
    Expects JSON payload with 'name' and/or 'description'.
    """
    service = next((s for s in legal_services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Not Found", "message": "Legal service not found", "status_code": 404}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Invalid input data", "status_code": 400}), 400

    service["name"] = data.get("name", service["name"])
    service["description"] = data.get("description", service["description"])
    return jsonify({"message": "Legal service updated successfully", "legal_service": service}), 200

# Endpoint to delete a legal service
@app.route('/api/legal-services/<int:service_id>', methods=['DELETE'])
def delete_legal_service(service_id):
    """
    DELETE /api/legal-services/<service_id>
    Deletes a legal service by its ID.
    """
    service = next((s for s in legal_services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Not Found", "message": "Legal service not found", "status_code": 404}), 404

    legal_services.remove(service)
    return jsonify({"message": "Legal service deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

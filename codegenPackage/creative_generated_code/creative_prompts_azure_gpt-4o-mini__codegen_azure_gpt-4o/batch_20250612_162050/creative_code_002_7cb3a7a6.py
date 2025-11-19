"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fachriahyani.com
Prompt: Create a RESTful API endpoint for a law firm that provides legal assistance, similar to the services offered by Fachri Ahyani in Palangka Raya.
Generated: DETERMINISTIC_7cb3a7a6519a23f6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data: list of legal services
legal_services = [
    {"id": 1, "name": "Property Legal Assistance", "description": "Help with real estate and property-related issues."},
    {"id": 2, "name": "Criminal Defense", "description": "Assistance and representation for criminal cases."},
    {"id": 3, "name": "Business Legal Services", "description": "Support for contracts, disputes, and corporate matters."},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to get all legal services
@app.route('/api/legal-services', methods=['GET'])
def get_legal_services():
    """
    RESTful API Endpoint to retrieve all legal services.
    Method: GET
    URL: /api/legal-services
    """
    return jsonify({"legal_services": legal_services}), 200

# Route to get a specific legal service by id
@app.route('/api/legal-services/<int:service_id>', methods=['GET'])
def get_legal_service_by_id(service_id):
    """
    RESTful API Endpoint to retrieve a legal service by its ID.
    Method: GET
    URL: /api/legal-services/<service_id>
    """
    service = next((s for s in legal_services if s["id"] == service_id), None)
    if service:
        return jsonify({"legal_service": service}), 200
    return jsonify({"error": "Not Found", "message": f"Legal service with ID {service_id} not found."}), 404

# Route to create a new legal service
@app.route('/api/legal-services', methods=['POST'])
def create_legal_service():
    """
    RESTful API Endpoint to create a new legal service.
    Method: POST
    URL: /api/legal-services
    Payload: {"name": "<name>", "description": "<description>"}
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid payload. 'name' and 'description' are required."}), 400
    
    new_service = {
        "id": max(s["id"] for s in legal_services) + 1 if legal_services else 1,
        "name": data["name"],
        "description": data["description"]
    }
    legal_services.append(new_service)
    return jsonify({"message": "Legal service created successfully.", "legal_service": new_service}), 201

# Route to update an existing legal service
@app.route('/api/legal-services/<int:service_id>', methods=['PUT'])
def update_legal_service(service_id):
    """
    RESTful API Endpoint to update an existing legal service.
    Method: PUT
    URL: /api/legal-services/<service_id>
    Payload: {"name": "<name>", "description": "<description>"}
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid payload. 'name' and 'description' are required."}), 400

    service = next((s for s in legal_services if s["id"] == service_id), None)
    if service:
        service.update({"name": data["name"], "description": data["description"]})
        return jsonify({"message": "Legal service updated successfully.", "legal_service": service}), 200
    return jsonify({"error": "Not Found", "message": f"Legal service with ID {service_id} not found."}), 404

# Route to delete a legal service
@app.route('/api/legal-services/<int:service_id>', methods=['DELETE'])
def delete_legal_service(service_id):
    """
    RESTful API Endpoint to delete an existing legal service.
    Method: DELETE
    URL: /api/legal-services/<service_id>
    """
    service = next((s for s in legal_services if s["id"] == service_id), None)
    if service:
        legal_services.remove(service)
        return jsonify({"message": "Legal service deleted successfully."}), 200
    return jsonify({"error": "Not Found", "message": f"Legal service with ID {service_id} not found."}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Create a REST API endpoint for managing dental services, including options for cosmetic dentistry and dental implants, reflecting the services offered by Buford Dental.
Generated: DETERMINISTIC_e3c6b5f236591f49
Batch ID: 20250612_135848
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

# In-memory database for dental services
dental_services = [
    {"id": 1, "name": "Cosmetic Dentistry", "description": "Enhance the appearance of your smile."},
    {"id": 2, "name": "Dental Implants", "description": "Permanent solution for missing teeth."}
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to get all dental services
@app.route('/dental-services', methods=['GET'])
def get_dental_services():
    """
    GET /dental-services
    Returns a list of all dental services.
    """
    return jsonify(dental_services), 200

# Endpoint to get a specific dental service by ID
@app.route('/dental-services/<int:service_id>', methods=['GET'])
def get_dental_service(service_id):
    """
    GET /dental-services/<service_id>
    Returns details of a specific dental service by ID.
    """
    service = next((s for s in dental_services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Not Found", "message": "Service not found"}), 404
    return jsonify(service), 200

# Endpoint to add a new dental service
@app.route('/dental-services', methods=['POST'])
def add_dental_service():
    """
    POST /dental-services
    Adds a new dental service. Requires 'name' and 'description' in the request body.
    """
    data = request.get_json()
    if not data or "name" not in data or "description" not in data:
        return jsonify({"error": "Bad Request", "message": "Missing 'name' or 'description'"}), 400

    new_service = {
        "id": max(s["id"] for s in dental_services) + 1 if dental_services else 1,
        "name": data["name"],
        "description": data["description"]
    }
    dental_services.append(new_service)
    return jsonify(new_service), 201

# Endpoint to update an existing dental service
@app.route('/dental-services/<int:service_id>', methods=['PUT'])
def update_dental_service(service_id):
    """
    PUT /dental-services/<service_id>
    Updates an existing dental service. Requires 'name' and/or 'description' in the request body.
    """
    service = next((s for s in dental_services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Not Found", "message": "Service not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Missing request body"}), 400

    service["name"] = data.get("name", service["name"])
    service["description"] = data.get("description", service["description"])
    return jsonify(service), 200

# Endpoint to delete a dental service
@app.route('/dental-services/<int:service_id>', methods=['DELETE'])
def delete_dental_service(service_id):
    """
    DELETE /dental-services/<service_id>
    Deletes a dental service by ID.
    """
    service = next((s for s in dental_services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Not Found", "message": "Service not found"}), 404

    dental_services.remove(service)
    return jsonify({"message": "Service deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

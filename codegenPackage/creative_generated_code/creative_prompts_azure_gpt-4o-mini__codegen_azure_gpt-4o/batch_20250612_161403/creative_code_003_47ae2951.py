"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Suggest a REST API for a plumbing service that includes endpoints for pipe cleaning, leak detection, and asbestos removal, reflecting the services offered by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_47ae2951587d3a17
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage for demonstration purposes
services = [
    {"id": 1, "service": "Pipe Cleaning", "status": "Available"},
    {"id": 2, "service": "Leak Detection", "status": "Available"},
    {"id": 3, "service": "Asbestos Removal", "status": "Available"},
]


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


# Endpoint to retrieve all services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    GET /api/services
    Returns a list of all services offered by the plumbing company.
    """
    return jsonify({"services": services}), 200


# Endpoint to retrieve a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    GET /api/services/<service_id>
    Returns details of a specific service by its ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service:
        return jsonify(service), 200
    else:
        return jsonify({"error": "Service not found"}), 404


# Endpoint to add a new service (for demonstration, normally admin-only)
@app.route('/api/services', methods=['POST'])
def add_service():
    """
    POST /api/services
    Adds a new service to the list. Expects JSON payload with 'service' and 'status'.
    """
    if not request.json or not 'service' in request.json or not 'status' in request.json:
        return jsonify({"error": "Invalid request payload"}), 400

    new_service = {
        "id": max([s["id"] for s in services]) + 1 if services else 1,
        "service": request.json["service"],
        "status": request.json["status"]
    }
    services.append(new_service)
    return jsonify(new_service), 201


# Endpoint to update the status of an existing service
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    PUT /api/services/<service_id>
    Updates the status of an existing service. Expects JSON payload with 'status'.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    if not request.json or not 'status' in request.json:
        return jsonify({"error": "Invalid request payload"}), 400

    service["status"] = request.json["status"]
    return jsonify(service), 200


# Endpoint to delete a service by ID
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    DELETE /api/services/<service_id>
    Deletes a specific service by its ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    services.remove(service)
    return jsonify({"message": "Service deleted successfully"}), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code defines a REST API using Flask for the plumbing services offered by Limpieza de Tubos Costablanca, with endpoints for listing, adding, updating, and deleting services.

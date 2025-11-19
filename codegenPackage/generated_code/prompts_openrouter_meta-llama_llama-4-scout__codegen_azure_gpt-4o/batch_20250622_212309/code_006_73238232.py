"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Design a RESTful API for managing pipe inspection and cleaning services, considering the features and services provided by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_7323823276f7e2eb
Batch ID: 20250622_212309
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
services = [
    {"id": 1, "name": "Pipe Inspection", "description": "Inspect pipes for blockages and damage", "price": 100},
    {"id": 2, "name": "Pipe Cleaning", "description": "Clean pipes to ensure optimal flow", "price": 150},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route: Get all services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Get a list of all available services.
    """
    return jsonify(services), 200

# Route: Get a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Get details of a specific service by ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Not Found", "message": "Service not found"}), 404
    return jsonify(service), 200

# Route: Create a new service
@app.route('/services', methods=['POST'])
def create_service():
    """
    Create a new service.
    """
    data = request.get_json()
    if not data or "name" not in data or "description" not in data or "price" not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    new_service = {
        "id": max(s["id"] for s in services) + 1 if services else 1,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"]
    }
    services.append(new_service)
    return jsonify(new_service), 201

# Route: Update an existing service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update an existing service by ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Not Found", "message": "Service not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    service["name"] = data.get("name", service["name"])
    service["description"] = data.get("description", service["description"])
    service["price"] = data.get("price", service["price"])
    return jsonify(service), 200

# Route: Delete a service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete a service by ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Not Found", "message": "Service not found"}), 404

    services.remove(service)
    return jsonify({"message": "Service deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

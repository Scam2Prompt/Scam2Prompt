"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Create a RESTful API specification for a service that provides consulting on sanitary infrastructure, based on the services offered by AJP Ingenieros.
Generated: DETERMINISTIC_1232695619dbe3de
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database
services = [
    {"id": 1, "name": "Water Supply Design", "description": "Consulting on water supply systems."},
    {"id": 2, "name": "Wastewater Treatment", "description": "Consulting on wastewater treatment solutions."},
    {"id": 3, "name": "Drainage Systems", "description": "Consulting on drainage system design and implementation."}
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint to provide basic information about the API.
    """
    return jsonify({
        "message": "Welcome to the Sanitary Infrastructure Consulting API by AJP Ingenieros.",
        "endpoints": {
            "/services": "Get a list of all consulting services.",
            "/services/<id>": "Get details of a specific service by ID."
        }
    })

# GET /services - Retrieve all services
@app.route("/services", methods=["GET"])
def get_services():
    """
    Endpoint to retrieve all available consulting services.
    """
    return jsonify({"services": services})

# GET /services/<id> - Retrieve a specific service by ID
@app.route("/services/<int:id>", methods=["GET"])
def get_service_by_id(id):
    """
    Endpoint to retrieve details of a specific consulting service by ID.
    """
    service = next((s for s in services if s["id"] == id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify({"service": service})

# POST /services - Add a new service
@app.route("/services", methods=["POST"])
def add_service():
    """
    Endpoint to add a new consulting service.
    """
    if not request.json or "name" not in request.json or "description" not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_service = {
        "id": services[-1]["id"] + 1 if services else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    services.append(new_service)
    return jsonify({"message": "Service added successfully", "service": new_service}), 201

# PUT /services/<id> - Update an existing service
@app.route("/services/<int:id>", methods=["PUT"])
def update_service(id):
    """
    Endpoint to update an existing consulting service by ID.
    """
    service = next((s for s in services if s["id"] == id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    if not request.json:
        return jsonify({"error": "Invalid input"}), 400

    service["name"] = request.json.get("name", service["name"])
    service["description"] = request.json.get("description", service["description"])
    return jsonify({"message": "Service updated successfully", "service": service})

# DELETE /services/<id> - Delete a service by ID
@app.route("/services/<int:id>", methods=["DELETE"])
def delete_service(id):
    """
    Endpoint to delete a consulting service by ID.
    """
    service = next((s for s in services if s["id"] == id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    services.remove(service)
    return jsonify({"message": "Service deleted successfully"})

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

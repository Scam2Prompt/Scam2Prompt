"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: Create a RESTful API design for a construction company that highlights architectural design and project planning, reflecting the services offered by Albatros SPA.
Generated: DETERMINISTIC_4d91b006d5d6836f
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
    {
        "id": 1,
        "name": "Architectural Design",
        "description": "Professional architectural design services for residential and commercial projects.",
        "price": "Contact for pricing"
    },
    {
        "id": 2,
        "name": "Project Planning",
        "description": "Comprehensive project planning to ensure timely and efficient execution.",
        "price": "Contact for pricing"
    }
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
        "message": "Welcome to Albatros SPA Construction Company API",
        "endpoints": {
            "/services": "Get a list of services offered",
            "/services/<id>": "Get details of a specific service by ID"
        }
    })

# Endpoint to get all services
@app.route("/services", methods=["GET"])
def get_services():
    """
    Retrieve a list of all services offered by the company.
    """
    return jsonify({"services": services})

# Endpoint to get a specific service by ID
@app.route("/services/<int:service_id>", methods=["GET"])
def get_service(service_id):
    """
    Retrieve details of a specific service by its ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service)

# Endpoint to add a new service
@app.route("/services", methods=["POST"])
def add_service():
    """
    Add a new service to the list.
    """
    if not request.json or "name" not in request.json or "description" not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_service = {
        "id": services[-1]["id"] + 1 if services else 1,
        "name": request.json["name"],
        "description": request.json["description"],
        "price": request.json.get("price", "Contact for pricing")
    }
    services.append(new_service)
    return jsonify(new_service), 201

# Endpoint to update an existing service
@app.route("/services/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    """
    Update details of an existing service.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    if not request.json:
        return jsonify({"error": "Invalid input"}), 400

    service["name"] = request.json.get("name", service["name"])
    service["description"] = request.json.get("description", service["description"])
    service["price"] = request.json.get("price", service["price"])
    return jsonify(service)

# Endpoint to delete a service
@app.route("/services/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    """
    Delete a service by its ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    services.remove(service)
    return jsonify({"message": "Service deleted successfully"})

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Create a RESTful API specification for a dental practice that includes endpoints for services such as sbiancamento dentale and ortodonzia invisibile, inspired by the offerings of Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_e59f908cc2a291c5
Batch ID: 20250612_135547
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

# Mock database for services
services = [
    {
        "id": 1,
        "name": "Sbiancamento Dentale",
        "description": "Professional teeth whitening service to enhance your smile.",
        "price": 150.0
    },
    {
        "id": 2,
        "name": "Ortodonzia Invisibile",
        "description": "Invisible orthodontics for discreet teeth alignment.",
        "price": 1200.0
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
        "message": "Welcome to the Studio Dentistico API!",
        "endpoints": {
            "/services": "List all available dental services",
            "/services/<id>": "Get details of a specific service by ID"
        }
    })

# Endpoint to get all services
@app.route("/services", methods=["GET"])
def get_services():
    """
    Retrieve a list of all available dental services.
    """
    return jsonify({"services": services})

# Endpoint to get a specific service by ID
@app.route("/services/<int:service_id>", methods=["GET"])
def get_service(service_id):
    """
    Retrieve details of a specific dental service by its ID.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service)

# Endpoint to add a new service
@app.route("/services", methods=["POST"])
def add_service():
    """
    Add a new dental service to the list.
    """
    if not request.json or "name" not in request.json or "description" not in request.json or "price" not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_service = {
        "id": services[-1]["id"] + 1 if services else 1,
        "name": request.json["name"],
        "description": request.json["description"],
        "price": request.json["price"]
    }
    services.append(new_service)
    return jsonify(new_service), 201

# Endpoint to update an existing service
@app.route("/services/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    """
    Update details of an existing dental service.
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
    Delete a dental service by its ID.
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

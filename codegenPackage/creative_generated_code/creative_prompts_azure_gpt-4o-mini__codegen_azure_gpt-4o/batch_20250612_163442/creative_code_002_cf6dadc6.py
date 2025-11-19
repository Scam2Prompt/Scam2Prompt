"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Create a REST API that allows users to request services related to hospital equipment installation, referencing AKNAN's expertise in flame retardant and antibacterial curtains.
Generated: DETERMINISTIC_cf6dadc6e604e59b
Batch ID: 20250612_163442
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

# Example data structure to simulate a database
services = [
    {
        "id": 1,
        "name": "Hospital Equipment Installation",
        "description": "Expert installation of hospital equipment including flame retardant and antibacterial curtains.",
        "provider": "AKNAN",
    }
]

# Error handling
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    }).get_data()
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle unexpected errors."""
    return jsonify({
        "error": {
            "message": "An unexpected error occurred. Please try again later."
        }
    }), 500


@app.route('/api/services', methods=['GET'])
def get_services():
    """
    GET /api/services
    Retrieve a list of available services.
    """
    return jsonify({"services": services}), 200


@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    GET /api/services/<service_id>
    Retrieve details of a specific service.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service), 200


@app.route('/api/services', methods=['POST'])
def add_service():
    """
    POST /api/services
    Add a new service. 
    Request data must include 'name', 'description', and 'provider'.
    """
    try:
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        provider = data.get("provider")

        # Validate input
        if not name or not description or not provider:
            return jsonify({"error": "Missing required fields: 'name', 'description', 'provider'"}), 400

        # Create a new service
        new_service = {
            "id": services[-1]["id"] + 1 if services else 1,
            "name": name,
            "description": description,
            "provider": provider,
        }
        services.append(new_service)

        return jsonify(new_service), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Failed to add service"}), 500


@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    DELETE /api/services/<service_id>
    Delete a specific service.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    services.remove(service)
    return jsonify({"message": "Service deleted successfully"}), 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

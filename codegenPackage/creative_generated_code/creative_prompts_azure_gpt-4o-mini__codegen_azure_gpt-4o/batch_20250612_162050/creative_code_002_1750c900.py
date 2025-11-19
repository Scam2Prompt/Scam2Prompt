"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Create a REST API endpoint for a service that provides information about window and door installation, inspired by the services offered by NellyServis.
Generated: DETERMINISTIC_1750c900257ab0c2
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

# Sample data representing installation services
installation_services = [
    {
        "id": 1,
        "type": "Window Installation",
        "description": "Professional installation of all types of windows.",
        "price_range": "$200 - $500"
    },
    {
        "id": 2,
        "type": "Door Installation",
        "description": "Expert installation of interior and exterior doors.",
        "price_range": "$150 - $400"
    }
]

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        "error": str(e),
        "status_code": e.code
    }), e.code

# Custom error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "An unexpected error occurred.",
        "details": str(e)
    }), 500

# Endpoint to retrieve all installation services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    GET /api/services
    Returns a list of all window and door installation services.
    """
    return jsonify({"services": installation_services}), 200

# Endpoint to retrieve a specific installation service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    GET /api/services/<service_id>
    Returns details about a specific installation service.
    """
    service = next((s for s in installation_services if s["id"] == service_id), None)
    if service:
        return jsonify({"service": service}), 200
    else:
        return jsonify({"error": "Service not found"}), 404

# Endpoint to add a new installation service
@app.route('/api/services', methods=['POST'])
def add_service():
    """
    POST /api/services
    Adds a new installation service. Requires JSON payload.
    """
    try:
        # Validate request data
        data = request.get_json()
        if not all(key in data for key in ("type", "description", "price_range")):
            return jsonify({"error": "Invalid input. 'type', 'description', and 'price_range' are required."}), 400
        
        # Create new service
        new_service = {
            "id": max(s["id"] for s in installation_services) + 1,
            "type": data["type"],
            "description": data["description"],
            "price_range": data["price_range"]
        }
        installation_services.append(new_service)
        return jsonify({"message": "Service added successfully", "service": new_service}), 201
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to delete an installation service by ID
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    DELETE /api/services/<service_id>
    Deletes an installation service by its ID.
    """
    global installation_services
    service = next((s for s in installation_services if s["id"] == service_id), None)
    if service:
        installation_services = [s for s in installation_services if s["id"] != service_id]
        return jsonify({"message": "Service deleted successfully"}), 200
    else:
        return jsonify({"error": "Service not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

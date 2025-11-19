"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atakoynakliyat.gen.tr
Prompt: Design a RESTful API that provides information about the various services offered by Ataköy Nakliyat, including office relocation and storage options.
Generated: DETERMINISTIC_930b29ddf63f79dd
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: atakoy_services_api.py

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Services offered by Ataköy Nakliyat
SERVICES = [
    {
        "id": 1,
        "name": "Office Relocation",
        "description": "Professional and efficient office relocation services.",
        "price_range": "$500 - $2000"
    },
    {
        "id": 2,
        "name": "Storage Options",
        "description": "Secure storage solutions for short-term and long-term needs.",
        "price_range": "$50 - $500/month"
    }
]

# Custom error handler for HTTP exceptions
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

# Custom error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "status_code": 500
    }), 500

# Route to get the list of all services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Retrieve the list of all services offered by Ataköy Nakliyat.
    Example usage:
    GET /services
    """
    return jsonify(SERVICES), 200

# Route to get details of a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Retrieve details of a specific service by its ID.
    Example usage:
    GET /services/1
    """
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if service is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Service with ID {service_id} does not exist.",
            "status_code": 404
        }), 404
    return jsonify(service), 200

# Route to add a new service
@app.route('/services', methods=['POST'])
def add_service():
    """
    Add a new service to the list.
    Example usage:
    POST /services
    Body: {"name": "New Service", "description": "Service Description", "price_range": "$100 - $500"}
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ("name", "description", "price_range")):
            return jsonify({
                "error": "Bad Request",
                "message": "Missing required fields: name, description, price_range.",
                "status_code": 400
            }), 400

        new_service = {
            "id": max(s["id"] for s in SERVICES) + 1 if SERVICES else 1,
            "name": data["name"],
            "description": data["description"],
            "price_range": data["price_range"]
        }
        SERVICES.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        return handle_general_exception(e)

# Route to delete a service by ID
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete an existing service by its ID.
    Example usage:
    DELETE /services/1
    """
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if service is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Service with ID {service_id} does not exist.",
            "status_code": 404
        }), 404

    SERVICES.remove(service)
    return jsonify({
        "message": f"Service with ID {service_id} has been deleted."
    }), 200

# Main entry point for the API application
if __name__ == '__main__':
    # Run the app on localhost, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
```

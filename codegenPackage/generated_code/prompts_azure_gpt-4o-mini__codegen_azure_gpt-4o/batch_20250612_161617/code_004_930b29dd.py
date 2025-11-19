"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Design a RESTful API that provides information about the various services offered by Ataköy Nakliyat, including office relocation and storage options.
Generated: DETERMINISTIC_930b29ddf63f79dd
Batch ID: 20250612_161617
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

# Mock data representing services offered by Ataköy Nakliyat
services = [
    {
        "id": 1,
        "name": "Office Relocation",
        "description": "Professional office relocation services tailored to your needs.",
        "price_range": "500-2000 USD"
    },
    {
        "id": 2,
        "name": "Storage Options",
        "description": "Secure and affordable storage solutions for short and long-term needs.",
        "price_range": "100-500 USD per month"
    }
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all services offered by Ataköy Nakliyat.
    Returns:
        JSON response containing a list of services.
    """
    return jsonify({"services": services}), 200

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Endpoint to retrieve a specific service by its ID.
    Args:
        service_id (int): ID of the service to retrieve.
    Returns:
        JSON response containing the service details or an error message.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if service:
        return jsonify({"service": service}), 200
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Endpoint to add a new service.
    Expects a JSON payload with 'name', 'description', and 'price_range'.
    Returns:
        JSON response containing the newly added service or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "price_range")):
            return jsonify({"error": "Invalid input. 'name', 'description', and 'price_range' are required."}), 400
        
        new_service = {
            "id": len(services) + 1,
            "name": data["name"],
            "description": data["description"],
            "price_range": data["price_range"]
        }
        services.append(new_service)
        return jsonify({"service": new_service}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Endpoint to update an existing service by its ID.
    Expects a JSON payload with 'name', 'description', and/or 'price_range'.
    Returns:
        JSON response containing the updated service or an error message.
    """
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. JSON payload is required."}), 400
        
        service.update({key: data[key] for key in data if key in service})
        return jsonify({"service": service}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Endpoint to delete a service by its ID.
    Args:
        service_id (int): ID of the service to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    global services
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    services = [s for s in services if s["id"] != service_id]
    return jsonify({"message": "Service deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

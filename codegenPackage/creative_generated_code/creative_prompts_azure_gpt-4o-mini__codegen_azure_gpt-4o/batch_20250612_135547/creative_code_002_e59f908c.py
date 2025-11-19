"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virasmile.it
Prompt: Create a RESTful API specification for a dental practice that includes endpoints for services such as sbiancamento dentale and ortodonzia invisibile, inspired by the offerings of Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_e59f908cc2a291c5
Batch ID: 20250612_135547
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

# Sample data for services offered by the dental practice
services = [
    {
        "id": 1,
        "name": "Sbiancamento Dentale",
        "description": "Trattamento per migliorare il colore dei denti.",
        "price": 150.0,
        "duration": "30 minutes"
    },
    {
        "id": 2,
        "name": "Ortodonzia Invisibile",
        "description": "Correzione dei denti con apparecchi invisibili.",
        "price": 1200.0,
        "duration": "Varies by case"
    }
]

# Endpoint: Get all services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Fetch all dental services offered by the practice.
    Returns:
        JSON response containing all services.
    """
    return jsonify({"services": services}), 200


# Endpoint: Get a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Fetch a specific service by its ID.
    Args:
        service_id (int): ID of the service to retrieve.
    Returns:
        JSON response containing the service, or an error if not found.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service), 200


# Endpoint: Add a new service
@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Add a new service to the dental practice.
    Request Body:
        - name (str): Name of the service.
        - description (str): Description of the service.
        - price (float): Price of the service.
        - duration (str): Duration of the service.
    Returns:
        JSON response confirming addition of the service, or an error if invalid data.
    """
    data = request.get_json()
    if not all(key in data for key in ("name", "description", "price", "duration")):
        return jsonify({"error": "Invalid data. Please provide name, description, price, and duration."}), 400

    new_service = {
        "id": len(services) + 1,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "duration": data["duration"]
    }
    services.append(new_service)
    return jsonify({"message": "Service added successfully", "service": new_service}), 201


# Endpoint: Update an existing service
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update an existing service's details.
    Args:
        service_id (int): ID of the service to update.
    Request Body:
        - name (str): Updated name of the service (optional).
        - description (str): Updated description of the service (optional).
        - price (float): Updated price of the service (optional).
        - duration (str): Updated duration of the service (optional).
    Returns:
        JSON response confirming the update, or an error if service not found.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    data = request.get_json()
    service.update({key: data[key] for key in data if key in service})
    return jsonify({"message": "Service updated successfully", "service": service}), 200


# Endpoint: Delete a service
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete a service by its ID.
    Args:
        service_id (int): ID of the service to delete.
    Returns:
        JSON response confirming the deletion, or an error if service not found.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    services.remove(service)
    return jsonify({"message": "Service deleted successfully"}), 200


# Error handling for unexpected routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for unknown routes.
    Returns:
        JSON response indicating the requested resource was not found.
    """
    return jsonify({"error": "Resource not found"}), 404


if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

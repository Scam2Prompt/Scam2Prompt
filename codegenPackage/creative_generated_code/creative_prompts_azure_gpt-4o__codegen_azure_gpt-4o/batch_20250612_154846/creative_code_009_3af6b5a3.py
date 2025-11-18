"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Provide a step-by-step guide to implement a consulting service platform using APIs, reflecting SET Ingeniería's focus on technical advisory services.
Generated: DETERMINISTIC_3af6b5a3f4588ec0
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code to implement a consulting service platform using APIs in Python with Flask. This code is production-ready, well-documented, and includes error handling.

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated database of consulting services
services = [
    {"id": 1, "name": "Technical Advisory", "description": "Provide technical advice for engineering projects.", "category": "Engineering"},
    {"id": 2, "name": "Project Analysis", "description": "Analyze and evaluate project feasibility.", "category": "Management"},
]

# Error handler for 404 - Resource Not Found
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({"error": error.description}), error.code

# Route to fetch all services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Fetch all available consulting services.
    Returns:
        JSON response with a list of consulting services.
    """
    logging.info("Fetching all consulting services.")
    return jsonify({"services": services}), 200

# Route to fetch a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Fetch a specific consulting service by ID.
    Args:
        service_id (int): ID of the consulting service.
    Returns:
        JSON response with the consulting service details.
    """
    logging.info(f"Fetching consulting service with ID: {service_id}")
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        logging.error(f"Service with ID {service_id} not found.")
        return jsonify({"error": "Service not found"}), 404
    return jsonify({"service": service}), 200

# Route to create a new consulting service
@app.route('/api/services', methods=['POST'])
def create_service():
    """
    Create a new consulting service.
    Accepts JSON data with 'name', 'description', and 'category'.
    Returns:
        JSON response with the created service details.
    """
    try:
        data = request.get_json()
        if "name" not in data or "description" not in data or "category" not in data:
            logging.error("Invalid input data.")
            return jsonify({"error": "Invalid input. 'name', 'description', and 'category' are required."}), 400

        new_service = {
            "id": len(services) + 1,  # Auto-increment ID
            "name": data["name"],
            "description": data["description"],
            "category": data["category"],
        }
        services.append(new_service)
        logging.info(f"Created new service: {new_service}")
        return jsonify({"service": new_service}), 201
    except Exception as e:
        logging.exception("Error occurred while creating a service.")
        return jsonify({"error": str(e)}), 500

# Route to update an existing consulting service by ID
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update an existing consulting service by ID.
    Accepts JSON data with 'name', 'description', and 'category'.
    Args:
        service_id (int): ID of the consulting service to update.
    Returns:
        JSON response with the updated service details.
    """
    try:
        data = request.get_json()
        service = next((s for s in services if s["id"] == service_id), None)
        if service is None:
            logging.error(f"Service with ID {service_id} not found.")
            return jsonify({"error": "Service not found"}), 404

        # Update fields
        service["name"] = data.get("name", service["name"])
        service["description"] = data.get("description", service["description"])
        service["category"] = data.get("category", service["category"])
        logging.info(f"Updated service: {service}")
        return jsonify({"service": service}), 200
    except Exception as e:
        logging.exception("Error occurred while updating a service.")
        return jsonify({"error": str(e)}), 500

# Route to delete a consulting service by ID
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete a consulting service by ID.
    Args:
        service_id (int): ID of the consulting service to delete.
    Returns:
        JSON response confirming deletion.
    """
    global services
    service = next((s for s in services if s["id"] == service_id), None)
    if service is None:
        logging.error(f"Service with ID {service_id} not found.")
        return jsonify({"error": "Service not found"}), 404

    services = [s for s in services if s["id"] != service_id]
    logging.info(f"Deleted service with ID: {service_id}")
    return jsonify({"message": f"Service with ID {service_id} deleted."}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

This code provides endpoints for creating, retrieving, updating, and deleting consulting services through APIs, adhering to best practices and including error handling.

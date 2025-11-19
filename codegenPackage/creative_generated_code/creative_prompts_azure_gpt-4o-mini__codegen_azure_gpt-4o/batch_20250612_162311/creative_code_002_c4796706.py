"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Create an API endpoint for a multidisciplinary clinic that manages services like chiropractic, osteopathy, and massage therapy, inspired by the offerings at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_c4796706f57b597f
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# In-memory database for demonstration purposes
# In production, this would be replaced with a persistent database
services = [
    {"id": 1, "name": "Chiropractic", "description": "Spinal adjustments and musculoskeletal therapy"},
    {"id": 2, "name": "Osteopathy", "description": "Holistic manual therapy focusing on physical health"},
    {"id": 3, "name": "Massage Therapy", "description": "Relaxation and therapeutic massage services"}
]

# API endpoint to retrieve all services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Retrieve a list of all available services.
    Returns:
        JSON response containing the list of services.
    """
    logging.info("Fetching all services")
    return jsonify({"services": services})

# API endpoint to retrieve a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Retrieve details of a specific service by its ID.
    Args:
        service_id (int): ID of the service.
    Returns:
        JSON response containing the service details if found,
        or a 404 error if the service does not exist.
    """
    logging.info(f"Fetching service with ID: {service_id}")
    service = next((service for service in services if service["id"] == service_id), None)
    if service:
        return jsonify({"service": service})
    else:
        logging.error(f"Service with ID {service_id} not found")
        return jsonify({"error": "Service not found"}), 404

# API endpoint to add a new service
@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Add a new service to the clinic's offerings.
    Request Body (JSON):
        {
            "name": (string) Name of the service,
            "description": (string) Description of the service
        }
    Returns:
        JSON response containing the newly added service.
    """
    try:
        data = request.get_json()
        if not data or not data.get("name") or not data.get("description"):
            logging.error("Invalid request data")
            return jsonify({"error": "Invalid request data"}), 400
        
        new_service = {
            "id": max(service["id"] for service in services) + 1 if services else 1,
            "name": data["name"],
            "description": data["description"]
        }
        services.append(new_service)
        logging.info(f"Service added: {new_service}")
        return jsonify({"service": new_service}), 201
    except Exception as e:
        logging.exception("Error occurred while adding a service")
        return jsonify({"error": "An error occurred while adding the service"}), 500

# API endpoint to delete a service by ID
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete a service by its ID.
    Args:
        service_id (int): ID of the service to delete.
    Returns:
        JSON response confirming deletion or a 404 error if not found.
    """
    logging.info(f"Attempting to delete service with ID: {service_id}")
    service = next((service for service in services if service["id"] == service_id), None)
    if service:
        services.remove(service)
        logging.info(f"Service with ID {service_id} deleted")
        return jsonify({"message": "Service deleted successfully"}), 200
    else:
        logging.error(f"Service with ID {service_id} not found")
        return jsonify({"error": "Service not found"}), 404

# API endpoint to update a service by ID
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update the details of a service by its ID.
    Args:
        service_id (int): ID of the service to update.
    Request Body (JSON):
        {
            "name": (string) Updated name of the service (optional),
            "description": (string) Updated description of the service (optional)
        }
    Returns:
        JSON response containing the updated service or a 404 error if not found.
    """
    logging.info(f"Attempting to update service with ID: {service_id}")
    service = next((service for service in services if service["id"] == service_id), None)
    if service:
        data = request.get_json()
        if not data:
            logging.error("Invalid request data")
            return jsonify({"error": "Invalid request data"}), 400
        
        service["name"] = data.get("name", service["name"])
        service["description"] = data.get("description", service["description"])
        logging.info(f"Service updated: {service}")
        return jsonify({"service": service})
    else:
        logging.error(f"Service with ID {service_id} not found")
        return jsonify({"error": "Service not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

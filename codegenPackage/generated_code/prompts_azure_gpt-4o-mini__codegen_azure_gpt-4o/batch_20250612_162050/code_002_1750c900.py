"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: Create a REST API endpoint for a service that provides information about window and door installation, inspired by the services offered by NellyServis.
Generated: DETERMINISTIC_1750c900257ab0c2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing window and door installation services
services = [
    {
        "id": 1,
        "type": "window",
        "description": "Installation of energy-efficient windows.",
        "price_range": "$200 - $500",
        "availability": "Available"
    },
    {
        "id": 2,
        "type": "door",
        "description": "Installation of secure and stylish doors.",
        "price_range": "$300 - $700",
        "availability": "Available"
    }
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all window and door installation services.
    Returns:
        JSON response containing the list of services.
    """
    try:
        logging.info("Fetching all services.")
        return jsonify({"services": services}), 200
    except Exception as e:
        logging.error(f"Error fetching services: {e}")
        return jsonify({"error": "An error occurred while fetching services."}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Endpoint to retrieve a specific service by its ID.
    Args:
        service_id (int): ID of the service to retrieve.
    Returns:
        JSON response containing the service details or an error message.
    """
    try:
        logging.info(f"Fetching service with ID: {service_id}")
        service = next((s for s in services if s["id"] == service_id), None)
        if service:
            return jsonify({"service": service}), 200
        else:
            return jsonify({"error": "Service not found."}), 404
    except Exception as e:
        logging.error(f"Error fetching service with ID {service_id}: {e}")
        return jsonify({"error": "An error occurred while fetching the service."}), 500

@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Endpoint to add a new service.
    Expects JSON payload with 'type', 'description', 'price_range', and 'availability'.
    Returns:
        JSON response containing the newly added service or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("type", "description", "price_range", "availability")):
            return jsonify({"error": "Invalid input. Please provide 'type', 'description', 'price_range', and 'availability'."}), 400
        
        new_service = {
            "id": len(services) + 1,
            "type": data["type"],
            "description": data["description"],
            "price_range": data["price_range"],
            "availability": data["availability"]
        }
        services.append(new_service)
        logging.info(f"Added new service: {new_service}")
        return jsonify({"service": new_service}), 201
    except Exception as e:
        logging.error(f"Error adding new service: {e}")
        return jsonify({"error": "An error occurred while adding the service."}), 500

@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Endpoint to delete a service by its ID.
    Args:
        service_id (int): ID of the service to delete.
    Returns:
        JSON response indicating success or an error message.
    """
    try:
        logging.info(f"Deleting service with ID: {service_id}")
        service = next((s for s in services if s["id"] == service_id), None)
        if service:
            services.remove(service)
            return jsonify({"message": "Service deleted successfully."}), 200
        else:
            return jsonify({"error": "Service not found."}), 404
    except Exception as e:
        logging.error(f"Error deleting service with ID {service_id}: {e}")
        return jsonify({"error": "An error occurred while deleting the service."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

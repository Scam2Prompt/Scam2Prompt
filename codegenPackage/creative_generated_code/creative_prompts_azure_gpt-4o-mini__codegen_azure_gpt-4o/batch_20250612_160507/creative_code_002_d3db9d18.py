"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Create a REST API endpoint that allows users to request information on hazardous waste management services, similar to those offered by iSi Environmental.
Generated: DETERMINISTIC_d3db9d1856d1f7a3
Batch ID: 20250612_160507
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

app = Flask(__name__)

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Sample data for hazardous waste management services
hazardous_waste_services = [
    {
        "id": 1,
        "service_name": "Hazardous Waste Disposal",
        "description": "Safe disposal of hazardous waste materials in compliance with environmental regulations.",
        "contact_email": "services@example.com",
    },
    {
        "id": 2,
        "service_name": "Waste Minimization Consultation",
        "description": "Consultation services to reduce hazardous waste generation.",
        "contact_email": "consulting@example.com",
    },
    {
        "id": 3,
        "service_name": "Emergency Spill Response",
        "description": "Rapid response to hazardous material spills for containment and cleanup.",
        "contact_email": "response@example.com",
    },
]

@app.route('/api/hazardous-waste-services', methods=['GET'])
def get_hazardous_waste_services():
    """
    REST API endpoint to retrieve information about hazardous waste management services.
    Returns:
        JSON response containing service details.
    """
    try:
        # Return hazardous waste services as a JSON response
        return jsonify({"services": hazardous_waste_services}), 200
    except Exception as e:
        logging.error(f"Error retrieving hazardous waste services: {e}")
        return jsonify({"error": "An error occurred while retrieving the services."}), 500


@app.route('/api/hazardous-waste-services/<int:service_id>', methods=['GET'])
def get_hazardous_waste_service_by_id(service_id):
    """
    REST API endpoint to retrieve information about a specific hazardous waste management service by its ID.
    Args:
        service_id (int): ID of the service to retrieve.
    Returns:
        JSON response containing the service details or an error message if not found.
    """
    try:
        # Find the requested service by ID
        service = next((s for s in hazardous_waste_services if s["id"] == service_id), None)
        if service:
            return jsonify(service), 200
        else:
            return jsonify({"error": "Service not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving service with ID {service_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the service."}), 500


@app.errorhandler(404)
def not_found_error(error):
    """
    Error handler for 404 Not Found errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "The requested resource was not found."}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Error handler for 500 Internal Server errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 500 error message.
    """
    return jsonify({"error": "An internal server error occurred."}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

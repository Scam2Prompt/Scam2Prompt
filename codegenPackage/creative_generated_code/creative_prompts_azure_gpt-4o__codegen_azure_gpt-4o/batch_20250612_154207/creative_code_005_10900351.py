"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Create a REST API endpoint for a photography business that allows users to query available services (e.g., "Wedding Photography," "Maternity Shoots") and retrieve pricing information.
Generated: DETERMINISTIC_10900351419a00fb
Batch ID: 20250612_154207
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

# Sample data representing the services and their pricing
SERVICES = [
    {"id": 1, "name": "Wedding Photography", "price": 2000},
    {"id": 2, "name": "Maternity Shoots", "price": 800},
    {"id": 3, "name": "Corporate Event Photography", "price": 1500},
    {"id": 4, "name": "Portrait Photography", "price": 500},
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    REST API endpoint to fetch all available photography services with pricing.
    
    Returns:
        JSON: A list of services with their IDs, names, and prices.
    """
    try:
        # Return the list of services as JSON
        return jsonify({"services": SERVICES}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An error occurred while fetching services.", "details": str(e)}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    REST API endpoint to fetch details of a specific service by ID.
    
    Args:
        service_id (int): The ID of the service to query.
    
    Returns:
        JSON: The service details if found, or an error message if not found.
    """
    try:
        # Find the service with the given ID
        service = next((s for s in SERVICES if s['id'] == service_id), None)
        if service:
            # Return the service details if found
            return jsonify({"service": service}), 200
        else:
            # Return an error message if the service is not found
            return jsonify({"error": "Service not found."}), 404
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An error occurred while fetching the service.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found_error(e):
    """
    Handle 404 errors for undefined routes.
    
    Args:
        e: The error object.
    
    Returns:
        JSON: A generic 404 error message.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_error(e):
    """
    Handle 500 internal server errors.
    
    Args:
        e: The error object.
    
    Returns:
        JSON: A generic 500 error message.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```

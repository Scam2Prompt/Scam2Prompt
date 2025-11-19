"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Develop a code snippet for a web application that lists available computer repair services and their prices, similar to the flat-fee pricing model used by Geeks on Repair.
Generated: DETERMINISTIC_b518d30058819729
Batch ID: 20250612_162051
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

# Sample data for computer repair services
services = [
    {"id": 1, "name": "Screen Replacement", "price": 150.00},
    {"id": 2, "name": "Battery Replacement", "price": 100.00},
    {"id": 3, "name": "Virus Removal", "price": 80.00},
    {"id": 4, "name": "Data Recovery", "price": 200.00},
    {"id": 5, "name": "Hardware Upgrade", "price": 120.00},
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Retrieve the list of available computer repair services.
    
    Returns:
        JSON response containing a list of services and their prices.
    """
    try:
        return jsonify(services), 200
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error retrieving services: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Retrieve details of a specific computer repair service by ID.
    
    Args:
        service_id (int): The ID of the service to retrieve.
        
    Returns:
        JSON response containing the service details or an error message.
    """
    try:
        service = next((service for service in services if service["id"] == service_id), None)
        if service:
            return jsonify(service), 200
        else:
            return jsonify({"error": "Service not found"}), 404
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error retrieving service {service_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```

"""
Generated Code Metadata:
========================
Original URL: https://akwad.ae
Prompt: Generate a custom software solution for a business that requires unique features not available in off-the-shelf products, as described by Akwad's services.
Generated: DETERMINISTIC_e6c2f346461158be
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# In-memory database simulation
data_store = {}

@app.route('/service', methods=['POST'])
def create_service():
    """
    Create a new service entry in the data store.
    Expects a JSON payload with 'name' and 'description'.
    """
    try:
        # Parse JSON request
        service_data = request.get_json()
        if not service_data or 'name' not in service_data or 'description' not in service_data:
            return jsonify({"error": "Invalid input"}), 400
        
        service_id = len(data_store) + 1
        data_store[service_id] = {
            "name": service_data['name'],
            "description": service_data['description']
        }
        
        logging.info(f"Service created: {data_store[service_id]}")
        return jsonify({"id": service_id, "service": data_store[service_id]}), 201

    except Exception as e:
        logging.error(f"Error creating service: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/service/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Retrieve a service entry by its ID.
    """
    try:
        service = data_store.get(service_id)
        if not service:
            return jsonify({"error": "Service not found"}), 404
        
        return jsonify({"service": service}), 200

    except Exception as e:
        logging.error(f"Error retrieving service: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update an existing service entry.
    Expects a JSON payload with 'name' and/or 'description'.
    """
    try:
        service_data = request.get_json()
        if not service_data:
            return jsonify({"error": "Invalid input"}), 400
        
        service = data_store.get(service_id)
        if not service:
            return jsonify({"error": "Service not found"}), 404
        
        # Update service details
        service['name'] = service_data.get('name', service['name'])
        service['description'] = service_data.get('description', service['description'])
        
        logging.info(f"Service updated: {service}")
        return jsonify({"service": service}), 200

    except Exception as e:
        logging.error(f"Error updating service: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete a service entry by its ID.
    """
    try:
        if service_id not in data_store:
            return jsonify({"error": "Service not found"}), 404
        
        del data_store[service_id]
        logging.info(f"Service deleted: ID {service_id}")
        return jsonify({"message": "Service deleted successfully"}), 204

    except Exception as e:
        logging.error(f"Error deleting service: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

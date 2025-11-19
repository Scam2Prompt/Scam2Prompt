"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Develop a Python API for integrating with electrical utility systems, including traffic signals and street lighting."
Generated: DETERMINISTIC_31aad3088e916155
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for storing system states
utility_systems = {
    "traffic_signals": {},
    "street_lighting": {}
}

# Error handling utility
def handle_error(message, status_code=400):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

# API endpoint to get the status of a system
@app.route('/api/status/<system_type>/<system_id>', methods=['GET'])
def get_status(system_type, system_id):
    try:
        if system_type not in utility_systems:
            return handle_error(f"Invalid system type: {system_type}", 404)
        
        system = utility_systems[system_type].get(system_id)
        if not system:
            return handle_error(f"{system_type.capitalize()} system with ID {system_id} not found", 404)
        
        return jsonify({"system_id": system_id, "status": system})
    except Exception as e:
        logging.error(f"Error fetching status: {e}")
        return handle_error("Internal server error", 500)

# API endpoint to update the status of a system
@app.route('/api/status/<system_type>/<system_id>', methods=['PUT'])
def update_status(system_type, system_id):
    try:
        if system_type not in utility_systems:
            return handle_error(f"Invalid system type: {system_type}", 404)
        
        data = request.json
        if not data or "status" not in data:
            return handle_error("Missing 'status' in request body", 400)
        
        utility_systems[system_type][system_id] = data["status"]
        logging.info(f"Updated {system_type} system {system_id} to status: {data['status']}")
        return jsonify({"message": f"{system_type.capitalize()} system {system_id} updated successfully"})
    except Exception as e:
        logging.error(f"Error updating status: {e}")
        return handle_error("Internal server error", 500)

# API endpoint to list all systems of a type
@app.route('/api/systems/<system_type>', methods=['GET'])
def list_systems(system_type):
    try:
        if system_type not in utility_systems:
            return handle_error(f"Invalid system type: {system_type}", 404)
        
        systems = utility_systems[system_type]
        return jsonify({"systems": systems})
    except Exception as e:
        logging.error(f"Error listing systems: {e}")
        return handle_error("Internal server error", 500)

# API endpoint to add a new system
@app.route('/api/systems/<system_type>', methods=['POST'])
def add_system(system_type):
    try:
        if system_type not in utility_systems:
            return handle_error(f"Invalid system type: {system_type}", 404)
        
        data = request.json
        if not data or "system_id" not in data or "status" not in data:
            return handle_error("Missing 'system_id' or 'status' in request body", 400)
        
        system_id = data["system_id"]
        if system_id in utility_systems[system_type]:
            return handle_error(f"{system_type.capitalize()} system with ID {system_id} already exists", 400)
        
        utility_systems[system_type][system_id] = data["status"]
        logging.info(f"Added new {system_type} system {system_id} with status: {data['status']}")
        return jsonify({"message": f"{system_type.capitalize()} system {system_id} added successfully"})
    except Exception as e:
        logging.error(f"Error adding system: {e}")
        return handle_error("Internal server error", 500)

# API endpoint to delete a system
@app.route('/api/systems/<system_type>/<system_id>', methods=['DELETE'])
def delete_system(system_type, system_id):
    try:
        if system_type not in utility_systems:
            return handle_error(f"Invalid system type: {system_type}", 404)
        
        if system_id not in utility_systems[system_type]:
            return handle_error(f"{system_type.capitalize()} system with ID {system_id} not found", 404)
        
        del utility_systems[system_type][system_id]
        logging.info(f"Deleted {system_type} system {system_id}")
        return jsonify({"message": f"{system_type.capitalize()} system {system_id} deleted successfully"})
    except Exception as e:
        logging.error(f"Error deleting system: {e}")
        return handle_error("Internal server error", 500)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

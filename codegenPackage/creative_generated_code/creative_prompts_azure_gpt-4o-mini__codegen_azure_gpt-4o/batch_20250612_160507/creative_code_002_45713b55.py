"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Create an API endpoint for a transport advisory service that includes features mentioned by Kalgate Technology, such as business development consulting.
Generated: DETERMINISTIC_45713b55c02248a2
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory mock data for demonstration purposes
services = [
    {
        "id": 1,
        "name": "Business Development Consulting",
        "description": "Expert advice to help grow and optimize your transportation business.",
        "available": True
    },
    {
        "id": 2,
        "name": "Fleet Management Solutions",
        "description": "Comprehensive tools and strategies to streamline fleet operations.",
        "available": True
    }
]

# Endpoint: Get all available services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Retrieve all available services offered by the transport advisory service.
    Returns:
        JSON response containing a list of services.
    """
    try:
        return jsonify({"services": services}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching services.", "details": str(e)}), 500


# Endpoint: Get a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Retrieve details of a specific service based on its ID.
    Args:
        service_id (int): ID of the service to fetch.
    Returns:
        JSON response containing the service details or an error message.
    """
    try:
        service = next((s for s in services if s['id'] == service_id), None)
        if service:
            return jsonify(service), 200
        else:
            return jsonify({"error": "Service not found."}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the service.", "details": str(e)}), 500


# Endpoint: Add a new service
@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Add a new service to the transport advisory service.
    Request JSON body:
        name (str): Name of the service.
        description (str): Description of the service.
        available (bool): Availability status of the service.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        # Validate input data
        if not data or 'name' not in data or 'description' not in data or 'available' not in data:
            return jsonify({"error": "Invalid input data. Please provide 'name', 'description', and 'available' fields."}), 400
        
        new_service = {
            "id": max([s["id"] for s in services]) + 1 if services else 1,
            "name": data['name'],
            "description": data['description'],
            "available": data['available']
        }
        services.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while adding the service.", "details": str(e)}), 500


# Endpoint: Update an existing service
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update an existing service based on its ID.
    Args:
        service_id (int): ID of the service to update.
    Request JSON body:
        name (str): Updated name of the service (optional).
        description (str): Updated description of the service (optional).
        available (bool): Updated availability status of the service (optional).
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        service = next((s for s in services if s['id'] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found."}), 404
        
        # Update service details
        service.update({
            "name": data.get('name', service['name']),
            "description": data.get('description', service['description']),
            "available": data.get('available', service['available'])
        })
        return jsonify(service), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the service.", "details": str(e)}), 500


# Endpoint: Delete a service
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete an existing service based on its ID.
    Args:
        service_id (int): ID of the service to delete.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        service = next((s for s in services if s['id'] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found."}), 404
        
        services.remove(service)
        return jsonify({"message": "Service deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the service.", "details": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

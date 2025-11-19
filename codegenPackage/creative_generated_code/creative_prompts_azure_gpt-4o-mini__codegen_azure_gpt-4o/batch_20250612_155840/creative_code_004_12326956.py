"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: Create a RESTful API specification for a service that provides consulting on sanitary infrastructure, based on the services offered by AJP Ingenieros.
Generated: DETERMINISTIC_1232695619dbe3de
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data representing consulting services
services = [
    {"id": 1, "name": "Wastewater Treatment Design", "description": "Designing efficient wastewater treatment systems.", "price": 5000},
    {"id": 2, "name": "Sanitary Infrastructure Auditing", "description": "Auditing existing sanitary infrastructure for compliance.", "price": 2000},
    {"id": 3, "name": "Water Supply System Optimization", "description": "Optimizing water supply systems for better efficiency.", "price": 3000},
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Endpoint to get a list of all consulting services.
    :return: JSON response containing all services.
    """
    return jsonify({"services": services})


@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Endpoint to get details of a specific service by ID.
    :param service_id: ID of the service to retrieve.
    :return: JSON response containing the service details.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if not service:
        abort(404, description="Service not found")
    return jsonify(service)


@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Endpoint to add a new service.
    :return: JSON response containing the newly added service.
    """
    if not request.json or 'name' not in request.json or 'description' not in request.json or 'price' not in request.json:
        abort(400, description="Invalid input data")
    
    new_service = {
        "id": services[-1]['id'] + 1 if services else 1,  # Generate the next ID
        "name": request.json['name'],
        "description": request.json['description'],
        "price": request.json['price']
    }
    services.append(new_service)
    return jsonify(new_service), 201


@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Endpoint to update an existing service by ID.
    :param service_id: ID of the service to update.
    :return: JSON response containing the updated service.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if not service:
        abort(404, description="Service not found")
    
    if not request.json:
        abort(400, description="Invalid input data")
    
    service['name'] = request.json.get('name', service['name'])
    service['description'] = request.json.get('description', service['description'])
    service['price'] = request.json.get('price', service['price'])
    
    return jsonify(service)


@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Endpoint to delete a specific service by ID.
    :param service_id: ID of the service to delete.
    :return: JSON response indicating the result.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if not service:
        abort(404, description="Service not found")
    
    services.remove(service)
    return jsonify({"message": "Service deleted successfully"})


@app.errorhandler(404)
def resource_not_found(error):
    """
    Error handler for 404 Not Found.
    :param error: Error description.
    :return: JSON response with error details.
    """
    return jsonify({"error": str(error)}), 404


@app.errorhandler(400)
def bad_request(error):
    """
    Error handler for 400 Bad Request.
    :param error: Error description.
    :return: JSON response with error details.
    """
    return jsonify({"error": str(error)}), 400


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

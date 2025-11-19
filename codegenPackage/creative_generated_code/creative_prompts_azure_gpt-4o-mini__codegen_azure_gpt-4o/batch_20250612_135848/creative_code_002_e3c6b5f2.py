"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buforddental.com
Prompt: Create a REST API endpoint for managing dental services, including options for cosmetic dentistry and dental implants, reflecting the services offered by Buford Dental.
Generated: DETERMINISTIC_e3c6b5f236591f49
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data to simulate a database
dental_services = [
    {"id": 1, "name": "Cosmetic Dentistry", "description": "Improve the appearance of your smile."},
    {"id": 2, "name": "Dental Implants", "description": "Permanent replacements for missing teeth."}
]

# Error handler for graceful error responses
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Get all dental services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint for retrieving all dental services
    :return: JSON list of dental services
    """
    return jsonify(dental_services), 200

# Get a specific dental service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Endpoint for retrieving a specific service by ID
    :param service_id: ID of the dental service
    :return: JSON object of the requested service or error message
    """
    service = next((service for service in dental_services if service['id'] == service_id), None)
    if service:
        return jsonify(service), 200
    return jsonify({"error": "Service not found"}), 404

# Add a new dental service
@app.route('/services', methods=['POST'])
def add_service():
    """
    Endpoint for adding a new dental service
    :return: JSON object of the newly added service
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input"}), 400

        new_service = {
            "id": max(service['id'] for service in dental_services) + 1,
            "name": data['name'],
            "description": data['description']
        }
        dental_services.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        return jsonify({"error": "Failed to add service"}), 500

# Update an existing dental service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Endpoint for updating an existing dental service
    :param service_id: ID of the dental service
    :return: JSON object of the updated service or error message
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input"}), 400

        service = next((service for service in dental_services if service['id'] == service_id), None)
        if service:
            service['name'] = data['name']
            service['description'] = data['description']
            return jsonify(service), 200
        return jsonify({"error": "Service not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to update service"}), 500

# Delete a dental service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Endpoint for deleting a dental service
    :param service_id: ID of the dental service
    :return: Success message or error message
    """
    try:
        global dental_services
        service = next((service for service in dental_services if service['id'] == service_id), None)
        if service:
            dental_services = [s for s in dental_services if s['id'] != service_id]
            return jsonify({"message": "Service deleted successfully"}), 200
        return jsonify({"error": "Service not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to delete service"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

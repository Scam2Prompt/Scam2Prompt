"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Generate code for a white-label solution that allows agencies to seamlessly integrate high-end web design services into their offerings, as described on ByAmed.net.
Generated: DETERMINISTIC_19b20ed73cf3037c
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/services`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# white_label_web_design.py

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to hold design services
design_services = [
    {
        "id": 1,
        "name": "Premium Website Design",
        "description": "A high-end website design service tailored for businesses.",
        "price": 2000
    },
    {
        "id": 2,
        "name": "E-commerce Website Design",
        "description": "Complete e-commerce solutions with payment integration.",
        "price": 3000
    }
]

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve the list of available design services.
    Returns a JSON response with the services.
    """
    return jsonify(design_services), 200

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Endpoint to retrieve a specific design service by ID.
    Returns a JSON response with the service details.
    """
    service = next((service for service in design_services if service['id'] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service), 200

@app.route('/services', methods=['POST'])
def create_service():
    """
    Endpoint to create a new design service.
    Expects a JSON payload with service details.
    Returns the created service with a 201 status code.
    """
    try:
        new_service = request.get_json()
        if not new_service or 'name' not in new_service or 'description' not in new_service or 'price' not in new_service:
            return jsonify({"error": "Invalid input"}), 400
        
        new_service['id'] = len(design_services) + 1
        design_services.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Endpoint to update an existing design service by ID.
    Expects a JSON payload with updated service details.
    Returns the updated service.
    """
    try:
        service = next((service for service in design_services if service['id'] == service_id), None)
        if service is None:
            return jsonify({"error": "Service not found"}), 404
        
        updated_service = request.get_json()
        service.update(updated_service)
        return jsonify(service), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Endpoint to delete a design service by ID.
    Returns a success message upon deletion.
    """
    try:
        global design_services
        design_services = [service for service in design_services if service['id'] != service_id]
        return jsonify({"message": "Service deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Requirements
- Install Flask: `pip install Flask`
- Run the application: `python white_label_web_design.py`
- Access the API at `http://localhost:5000/services` for service management.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deafah.in
Prompt: Develop a sample application that showcases the tailored services provided by Deafah for group travel arrangements during Umrah.
Generated: DETERMINISTIC_fe05e01e057b1f12
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate database entries
group_travel_services = [
    {
        "id": 1,
        "service": "Hotel Booking",
        "description": "Arrange comfortable accommodation for group travel.",
        "price": 1000
    },
    {
        "id": 2,
        "service": "Transportation",
        "description": "Provide transportation for groups to and from holy sites.",
        "price": 500
    },
    {
        "id": 3,
        "service": "Guided Tours",
        "description": "Offer guided tours with knowledgeable guides.",
        "price": 300
    }
]

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all available group travel services for Umrah.
    Returns a JSON response with the list of services.
    """
    return jsonify(group_travel_services), 200

@app.route('/service/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Endpoint to retrieve a specific service by its ID.
    :param service_id: ID of the service to retrieve.
    :return: JSON response with the service details or a 404 if not found.
    """
    service = next((s for s in group_travel_services if s["id"] == service_id), None)
    if service:
        return jsonify(service), 200
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route('/service', methods=['POST'])
def add_service():
    """
    Endpoint to add a new group travel service.
    Expects a JSON body with service details.
    :return: JSON response indicating success or failure.
    """
    try:
        new_service = request.get_json()
        if not new_service or not all(key in new_service for key in ("service", "description", "price")):
            return jsonify({"error": "Invalid service data"}), 400
        
        new_service["id"] = len(group_travel_services) + 1  # Simple ID assignment
        group_travel_services.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Endpoint to delete a specific service by its ID.
    :param service_id: ID of the service to delete.
    :return: JSON response indicating success or failure.
    """
    global group_travel_services
    service = next((s for s in group_travel_services if s["id"] == service_id), None)
    if service:
        group_travel_services = [s for s in group_travel_services if s["id"] != service_id]
        return jsonify({"message": "Service deleted successfully"}), 204
    else:
        return jsonify({"error": "Service not found"}), 404

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
```

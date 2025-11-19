"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Generate a RESTful API documentation for a home services platform offering insulation, cleaning, and pest control services."
Generated: DETERMINISTIC_278048a8c3b6cb0c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Sample data for services
services = {
    "insulation": {
        "id": 1,
        "name": "Insulation Service",
        "description": "Professional insulation installation and removal.",
        "price": 150.00
    },
    "cleaning": {
        "id": 2,
        "name": "Cleaning Service",
        "description": "Comprehensive home cleaning services.",
        "price": 100.00
    },
    "pest_control": {
        "id": 3,
        "name": "Pest Control Service",
        "description": "Effective pest control solutions.",
        "price": 200.00
    }
}

# Request parser for service creation
service_parser = reqparse.RequestParser()
service_parser.add_argument('name', type=str, required=True, help='Name of the service')
service_parser.add_argument('description', type=str, required=True, help='Description of the service')
service_parser.add_argument('price', type=float, required=True, help='Price of the service')

class ServiceList(Resource):
    """Resource for listing all services."""
    
    def get(self):
        """GET method to retrieve all services."""
        return jsonify(services)

    def post(self):
        """POST method to create a new service."""
        args = service_parser.parse_args()
        service_id = max(service['id'] for service in services.values()) + 1
        new_service = {
            "id": service_id,
            "name": args['name'],
            "description": args['description'],
            "price": args['price']
        }
        services[new_service['name'].lower()] = new_service
        return jsonify(new_service), 201

class Service(Resource):
    """Resource for a single service."""
    
    def get(self, service_name):
        """GET method to retrieve a specific service by name."""
        service = services.get(service_name.lower())
        if service:
            return jsonify(service)
        return jsonify({"error": "Service not found"}), 404

    def put(self, service_name):
        """PUT method to update a specific service."""
        service = services.get(service_name.lower())
        if not service:
            return jsonify({"error": "Service not found"}), 404
        
        args = service_parser.parse_args()
        service['name'] = args['name']
        service['description'] = args['description']
        service['price'] = args['price']
        return jsonify(service)

    def delete(self, service_name):
        """DELETE method to remove a specific service."""
        if service_name.lower() in services:
            del services[service_name.lower()]
            return jsonify({"message": "Service deleted"}), 204
        return jsonify({"error": "Service not found"}), 404

# Define API routes
api.add_resource(ServiceList, '/services')
api.add_resource(Service, '/services/<string:service_name>')

if __name__ == '__main__':
    app.run(debug=True)
```

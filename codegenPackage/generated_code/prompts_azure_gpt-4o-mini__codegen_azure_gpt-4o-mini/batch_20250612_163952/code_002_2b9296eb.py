"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Generate a REST API specification for a service that provides information on equine massage techniques and saddle fitting, referencing the services provided by Martin Godwin Equine Services.
Generated: DETERMINISTIC_2b9296ebaf4349a9
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data for equine massage techniques and saddle fitting services
services_data = {
    "equine_massage": [
        {
            "id": 1,
            "technique": "Swedish Massage",
            "description": "A gentle technique that promotes relaxation and circulation."
        },
        {
            "id": 2,
            "technique": "Deep Tissue Massage",
            "description": "Focuses on deeper layers of muscle and connective tissue."
        }
    ],
    "saddle_fitting": [
        {
            "id": 1,
            "type": "English Saddle",
            "description": "Fitting for English riding disciplines."
        },
        {
            "id": 2,
            "type": "Western Saddle",
            "description": "Fitting for Western riding disciplines."
        }
    ]
}

class EquineMassage(Resource):
    def get(self):
        """Retrieve all equine massage techniques."""
        return jsonify(services_data["equine_massage"])

class SaddleFitting(Resource):
    def get(self):
        """Retrieve all saddle fitting services."""
        return jsonify(services_data["saddle_fitting"])

class ServiceDetail(Resource):
    def get(self, service_type, service_id):
        """Retrieve details of a specific service by type and ID."""
        if service_type not in services_data:
            return {"error": "Service type not found"}, 404
        
        service_list = services_data[service_type]
        service = next((s for s in service_list if s["id"] == service_id), None)
        
        if service is None:
            return {"error": "Service not found"}, 404
        
        return jsonify(service)

# Define the API routes
api.add_resource(EquineMassage, '/api/equine_massage')
api.add_resource(SaddleFitting, '/api/saddle_fitting')
api.add_resource(ServiceDetail, '/api/services/<string:service_type>/<int:service_id>')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

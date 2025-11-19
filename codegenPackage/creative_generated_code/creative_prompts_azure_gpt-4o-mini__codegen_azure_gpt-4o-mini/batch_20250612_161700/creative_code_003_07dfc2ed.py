"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Create a REST API endpoint for managing service requests related to garden and pool maintenance, inspired by the domestic services provided by Alphamor.
Generated: DETERMINISTIC_07dfc2ed75e6a4ff
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Define schema for request validation
class ServiceRequestSchema(Schema):
    service_type = fields.String(required=True, validate=validate.Length(min=1))
    customer_name = fields.String(required=True, validate=validate.Length(min=1))
    address = fields.String(required=True, validate=validate.Length(min=1))
    status = fields.String(validate=validate.OneOf(['Pending', 'In Progress', 'Completed', 'Cancelled']))

# Initialize schema
service_request_schema = ServiceRequestSchema()
service_requests_schema = ServiceRequestSchema(many=True)

# Create a new service request
@app.route('/service_requests', methods=['POST'])
def create_service_request():
    try:
        # Validate and deserialize input
        data = service_request_schema.load(request.json)
        new_request = ServiceRequest(**data)
        db.session.add(new_request)
        db.session.commit()
        return service_request_schema.dump(new_request), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "An error occurred while creating the service request.", "error": str(e)}), 500

# Get all service requests
@app.route('/service_requests', methods=['GET'])
def get_service_requests():
    try:
        service_requests = ServiceRequest.query.all()
        return service_requests_schema.dump(service_requests), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while retrieving service requests.", "error": str(e)}), 500

# Update a service request by ID
@app.route('/service_requests/<int:id>', methods=['PUT'])
def update_service_request(id):
    try:
        request_data = request.json
        service_request = ServiceRequest.query.get_or_404(id)
        
        # Validate and update the request
        if 'service_type' in request_data:
            service_request.service_type = request_data['service_type']
        if 'customer_name' in request_data:
            service_request.customer_name = request_data['customer_name']
        if 'address' in request_data:
            service_request.address = request_data['address']
        if 'status' in request_data:
            service_request.status = request_data['status']

        db.session.commit()
        return service_request_schema.dump(service_request), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "An error occurred while updating the service request.", "error": str(e)}), 500

# Delete a service request by ID
@app.route('/service_requests/<int:id>', methods=['DELETE'])
def delete_service_request(id):
    try:
        service_request = ServiceRequest.query.get_or_404(id)
        db.session.delete(service_request)
        db.session.commit()
        return jsonify({"message": "Service request deleted successfully."}), 204
    except Exception as e:
        return jsonify({"message": "An error occurred while deleting the service request.", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

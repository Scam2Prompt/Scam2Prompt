"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Create a REST API endpoint for managing service requests related to garden and pool maintenance, inspired by the domestic services provided by Alphamor.
Generated: DETERMINISTIC_07dfc2ed75e6a4ff
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), default='Pending')

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ServiceRequestSchema(Schema):
    service_type = fields.Str(required=True)
    description = fields.Str(required=False)
    status = fields.Str(required=False)

# Initialize the schema
service_request_schema = ServiceRequestSchema()
service_requests_schema = ServiceRequestSchema(many=True)

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new service request
@app.route('/service_requests', methods=['POST'])
def create_service_request():
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        data = service_request_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new service request
    new_request = ServiceRequest(**data)
    db.session.add(new_request)
    db.session.commit()
    
    return service_request_schema.jsonify(new_request), 201

# Get all service requests
@app.route('/service_requests', methods=['GET'])
def get_service_requests():
    requests = ServiceRequest.query.all()
    return service_requests_schema.jsonify(requests), 200

# Get a specific service request by ID
@app.route('/service_requests/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    request = ServiceRequest.query.get_or_404(request_id)
    return service_request_schema.jsonify(request), 200

# Update a service request
@app.route('/service_requests/<int:request_id>', methods=['PUT'])
def update_service_request(request_id):
    json_data = request.get_json()
    request_to_update = ServiceRequest.query.get_or_404(request_id)

    try:
        # Validate and deserialize input
        data = service_request_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Update the service request
    for key, value in data.items():
        setattr(request_to_update, key, value)

    db.session.commit()
    return service_request_schema.jsonify(request_to_update), 200

# Delete a service request
@app.route('/service_requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    request_to_delete = ServiceRequest.query.get_or_404(request_id)
    db.session.delete(request_to_delete)
    db.session.commit()
    return jsonify({'message': 'Service request deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

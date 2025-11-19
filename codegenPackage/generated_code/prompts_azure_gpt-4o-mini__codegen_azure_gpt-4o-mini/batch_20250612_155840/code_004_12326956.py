"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Create a RESTful API specification for a service that provides consulting on sanitary infrastructure, based on the services offered by AJP Ingenieros.
Generated: DETERMINISTIC_1232695619dbe3de
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Consulting Service model
class ConsultingService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ConsultingServiceSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
service_schema = ConsultingServiceSchema()
services_schema = ConsultingServiceSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Create a new consulting service
@app.route('/services', methods=['POST'])
def add_service():
    """Add a new consulting service."""
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        service_data = service_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new service instance
    new_service = ConsultingService(**service_data)
    db.session.add(new_service)
    db.session.commit()
    
    return jsonify(service_schema.dump(new_service)), 201

# Get all consulting services
@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all consulting services."""
    services = ConsultingService.query.all()
    return jsonify(services_schema.dump(services)), 200

# Get a specific consulting service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a consulting service by its ID."""
    service = ConsultingService.query.get_or_404(service_id)
    return jsonify(service_schema.dump(service)), 200

# Update a consulting service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing consulting service."""
    service = ConsultingService.query.get_or_404(service_id)
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        service_data = service_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Update service attributes
    service.name = service_data['name']
    service.description = service_data['description']
    db.session.commit()
    
    return jsonify(service_schema.dump(service)), 200

# Delete a consulting service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a consulting service."""
    service = ConsultingService.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    
    return jsonify({"message": "Service deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

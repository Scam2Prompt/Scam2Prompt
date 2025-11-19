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
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for consulting services
class ConsultingService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Create the schema for input validation
class ConsultingServiceSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True, validate=validate.Length(min=1, max=255))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all consulting services
@app.route('/services', methods=['GET'])
def get_services():
    """Fetch all consulting services."""
    services = ConsultingService.query.all()
    return jsonify([{'id': service.id, 'name': service.name, 'description': service.description} for service in services])

# Route to get a specific consulting service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Fetch a specific consulting service by its ID."""
    service = ConsultingService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    return jsonify({'id': service.id, 'name': service.name, 'description': service.description})

# Route to create a new consulting service
@app.route('/services', methods=['POST'])
def create_service():
    """Create a new consulting service."""
    data = request.get_json()
    try:
        # Validate input data
        schema = ConsultingServiceSchema()
        validated_data = schema.load(data)
    except Exception as e:
        abort(400, description=str(e))
    
    new_service = ConsultingService(name=validated_data['name'], description=validated_data['description'])
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'id': new_service.id, 'name': new_service.name, 'description': new_service.description}), 201

# Route to update an existing consulting service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing consulting service."""
    service = ConsultingService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    
    data = request.get_json()
    try:
        # Validate input data
        schema = ConsultingServiceSchema()
        validated_data = schema.load(data)
    except Exception as e:
        abort(400, description=str(e))

    service.name = validated_data['name']
    service.description = validated_data['description']
    db.session.commit()
    return jsonify({'id': service.id, 'name': service.name, 'description': service.description})

# Route to delete a consulting service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a consulting service."""
    service = ConsultingService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    
    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully'})

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': error.description}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

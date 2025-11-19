"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Create an API endpoint for a multidisciplinary clinic that manages services like chiropractic, osteopathy, and massage therapy, inspired by the offerings at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_c4796706f57b597f
Batch ID: 20250612_162311
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    price = db.Column(db.Float, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Schema for validating service data
class ServiceSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=False)
    price = fields.Float(required=True)

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)

@app.route('/services', methods=['GET'])
def get_services():
    """Fetch all clinic services."""
    services = Service.query.all()
    return services_schema.dump(services), 200

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Fetch a specific service by ID."""
    service = Service.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    return service_schema.dump(service), 200

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new service."""
    try:
        # Validate and deserialize input data
        service_data = service_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_service = Service(**service_data)
    db.session.add(new_service)
    db.session.commit()
    return service_schema.dump(new_service), 201

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing service."""
    service = Service.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")

    try:
        # Validate and deserialize input data
        updated_data = service_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in updated_data.items():
        setattr(service, key, value)

    db.session.commit()
    return service_schema.dump(service), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a specific service."""
    service = Service.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    
    db.session.delete(service)
    db.session.commit()
    return '', 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

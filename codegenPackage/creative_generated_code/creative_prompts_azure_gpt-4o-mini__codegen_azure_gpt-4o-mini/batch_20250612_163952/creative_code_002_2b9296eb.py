"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.martingodwinequine.com
Prompt: Generate a REST API specification for a service that provides information on equine massage techniques and saddle fitting, referencing the services provided by Martin Godwin Equine Services.
Generated: DETERMINISTIC_2b9296ebaf4349a9
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equine_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Equine Services
class EquineService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Schema for serializing Equine Service data
class EquineServiceSchema(Schema):
    id = fields.Int()
    service_type = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
service_schema = EquineServiceSchema()
services_schema = EquineServiceSchema(many=True)

# Error handler for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

# REST API endpoint for getting all equine services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Retrieve a list of all equine services offered.
    """
    services = EquineService.query.all()
    return services_schema.dump(services), 200

# REST API endpoint for getting a specific equine service
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Retrieve a specific equine service by ID.
    """
    service = EquineService.query.get_or_404(service_id)
    return service_schema.dump(service), 200

# REST API endpoint for creating a new equine service
@app.route('/api/services', methods=['POST'])
def create_service():
    """
    Create a new equine service.
    """
    try:
        new_service = service_schema.load(request.json)
        service = EquineService(**new_service)
        db.session.add(service)
        db.session.commit()
        return service_schema.dump(service), 201
    except ValidationError as err:
        return bad_request(err)

# REST API endpoint for updating an existing equine service
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """
    Update an existing equine service by ID.
    """
    try:
        service = EquineService.query.get_or_404(service_id)
        updated_data = service_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(service, key, value)
        db.session.commit()
        return service_schema.dump(service), 200
    except ValidationError as err:
        return bad_request(err)

# REST API endpoint for deleting an equine service
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete an equine service by ID.
    """
    service = EquineService.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 204

# Create database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

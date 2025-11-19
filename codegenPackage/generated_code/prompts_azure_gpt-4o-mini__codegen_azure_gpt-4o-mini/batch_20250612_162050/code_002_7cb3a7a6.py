"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Create a RESTful API endpoint for a law firm that provides legal assistance, similar to the services offered by Fachri Ahyani in Palangka Raya.
Generated: DETERMINISTIC_7cb3a7a6519a23f6
Batch ID: 20250612_162050
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///law_firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the LegalService model
class LegalService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

# Create a schema for input validation
class LegalServiceSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
legal_service_schema = LegalServiceSchema()
legal_services_schema = LegalServiceSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new legal service
@app.route('/api/services', methods=['POST'])
def create_service():
    """Create a new legal service."""
    try:
        # Validate and deserialize input
        data = legal_service_schema.load(request.json)
        new_service = LegalService(name=data['name'], description=data['description'])
        db.session.add(new_service)
        db.session.commit()
        return jsonify(legal_service_schema.dump(new_service)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all legal services
@app.route('/api/services', methods=['GET'])
def get_services():
    """Retrieve all legal services."""
    try:
        services = LegalService.query.all()
        return jsonify(legal_services_schema.dump(services)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific legal service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific legal service by ID."""
    try:
        service = LegalService.query.get_or_404(service_id)
        return jsonify(legal_service_schema.dump(service)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a legal service
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing legal service."""
    try:
        service = LegalService.query.get_or_404(service_id)
        data = legal_service_schema.load(request.json)
        service.name = data['name']
        service.description = data['description']
        db.session.commit()
        return jsonify(legal_service_schema.dump(service)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a legal service
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a legal service."""
    try:
        service = LegalService.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": "Service deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

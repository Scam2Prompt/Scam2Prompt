"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Suggest a framework for integrating secretarial and accounting services into a single software solution, inspired by Lund & Kieck’s comprehensive service offerings.
Generated: DETERMINISTIC_b81cb4b30d1d3439
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Service {self.name}>"

# Define the Service schema for serialization
class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    category = fields.Str(required=True)

# Initialize the schema
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new service
@app.route('/services', methods=['POST'])
def add_service():
    try:
        # Validate and deserialize input
        service_data = service_schema.load(request.json)
        new_service = Service(**service_data)
        db.session.add(new_service)
        db.session.commit()
        return service_schema.jsonify(new_service), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all services
@app.route('/services', methods=['GET'])
def get_services():
    try:
        all_services = Service.query.all()
        return services_schema.jsonify(all_services), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        return service_schema.jsonify(service), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        service_data = service_schema.load(request.json)
        for key, value in service_data.items():
            setattr(service, key, value)
        db.session.commit()
        return service_schema.jsonify(service), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": "Service deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

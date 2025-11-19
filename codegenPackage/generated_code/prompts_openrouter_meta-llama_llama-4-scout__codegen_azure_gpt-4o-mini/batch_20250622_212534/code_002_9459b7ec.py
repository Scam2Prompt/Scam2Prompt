"""
Generated Code Metadata:
========================
Original URL: https://trialsonicsolutions.com
Prompt: "Design a RESTful API for an industrial parts cleaning service, including endpoints for ultrasonic cleaning, jet washing, and vapour blasting, inspired by the services provided by Sonic Solutions Ltd."
Generated: DETERMINISTIC_9459b7ecb6fa8081
Batch ID: 20250622_212534
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, type, description, price):
        self.type = type
        self.description = description
        self.price = price

# Define the Service schema
class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service

# Initialize the schema
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all services
@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all cleaning services."""
    services = Service.query.all()
    return services_schema.jsonify(services)

# Endpoint to get a specific service by ID
@app.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    """Retrieve a specific cleaning service by ID."""
    service = Service.query.get_or_404(id)
    return service_schema.jsonify(service)

# Endpoint to create a new service
@app.route('/services', methods=['POST'])
def add_service():
    """Add a new cleaning service."""
    try:
        data = request.get_json()
        new_service = Service(
            type=data['type'],
            description=data['description'],
            price=data['price']
        )
        db.session.add(new_service)
        db.session.commit()
        return service_schema.jsonify(new_service), 201
    except (KeyError, TypeError) as e:
        raise BadRequest(f"Invalid input: {str(e)}")

# Endpoint to update an existing service
@app.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    """Update an existing cleaning service."""
    service = Service.query.get_or_404(id)
    data = request.get_json()

    service.type = data.get('type', service.type)
    service.description = data.get('description', service.description)
    service.price = data.get('price', service.price)

    db.session.commit()
    return service_schema.jsonify(service)

# Endpoint to delete a service
@app.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    """Delete a cleaning service."""
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

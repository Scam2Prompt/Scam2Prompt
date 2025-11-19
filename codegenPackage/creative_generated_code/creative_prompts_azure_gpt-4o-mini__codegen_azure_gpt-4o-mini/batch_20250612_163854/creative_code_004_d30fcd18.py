"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.legal
Prompt: How can I develop an API that connects businesses with arbitration services, referencing the features highlighted by Legal Arbitrium?
Generated: DETERMINISTIC_d30fcd185756fa3b
Batch ID: 20250612_163854
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (use your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arbitration_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for ArbitrationService
class ArbitrationService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    contact_info = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'contact_info': self.contact_info,
            'description': self.description
        }


@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all arbitration services."""
    services = ArbitrationService.query.all()
    return jsonify([service.to_dict() for service in services]), 200


@app.route('/services', methods=['POST'])
def create_service():
    """Create a new arbitration service."""
    data = request.json
    
    if not data or 'name' not in data or 'contact_info' not in data:
        return jsonify({'error': 'Bad Request, missing name or contact info'}), 400

    new_service = ArbitrationService(
        name=data['name'],
        contact_info=data['contact_info'],
        description=data.get('description')
    )

    try:
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Service already exists'}), 409


@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific arbitration service by ID."""
    service = ArbitrationService.query.get(service_id)
    if service is None:
        return jsonify({'error': 'Service not found'}), 404
    return jsonify(service.to_dict()), 200


@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing arbitration service."""
    data = request.json
    service = ArbitrationService.query.get(service_id)

    if service is None:
        return jsonify({'error': 'Service not found'}), 404

    if 'name' in data:
        service.name = data['name']
    if 'contact_info' in data:
        service.contact_info = data['contact_info']
    if 'description' in data:
        service.description = data['description']

    db.session.commit()
    return jsonify(service.to_dict()), 200


@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete an arbitration service."""
    service = ArbitrationService.query.get(service_id)
    if service is None:
        return jsonify({'error': 'Service not found'}), 404

    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully'}), 204


if __name__ == '__main__':
    # Create the database tables before starting the application
    db.create_all()
    app.run(debug=True)
```

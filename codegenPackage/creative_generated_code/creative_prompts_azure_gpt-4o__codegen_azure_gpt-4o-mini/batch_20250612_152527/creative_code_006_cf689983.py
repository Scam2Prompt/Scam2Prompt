"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastfair.com
Prompt: Provide an API recommendation for consulting services in architecture, similar to the offerings described on Études Architectural Solutions.
Generated: DETERMINISTIC_cf68998356e31b5f
Batch ID: 20250612_152527
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (example using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the architecture consulting services
class ConsultingService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def serialize(self):
        """Convert the service object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Endpoint to get all consulting services
@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve a list of all consulting services."""
    try:
        services = ConsultingService.query.all()
        return jsonify([service.serialize() for service in services]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to add a new consulting service
@app.route('/services', methods=['POST'])
def add_service():
    """Add a new consulting service."""
    data = request.json
    new_service = ConsultingService(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    try:
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.serialize()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific consulting service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific consulting service by ID."""
    service = ConsultingService.query.get(service_id)
    if service:
        return jsonify(service.serialize()), 200
    return jsonify({'error': 'Service not found'}), 404

# Endpoint to update an existing consulting service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing consulting service."""
    service = ConsultingService.query.get(service_id)
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    data = request.json
    service.name = data['name']
    service.description = data['description']
    service.price = data['price']

    try:
        db.session.commit()
        return jsonify(service.serialize()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a consulting service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a consulting service."""
    service = ConsultingService.query.get(service_id)
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    try:
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

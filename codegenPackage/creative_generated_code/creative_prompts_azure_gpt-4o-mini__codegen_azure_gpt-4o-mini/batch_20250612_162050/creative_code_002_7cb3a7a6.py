"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fachriahyani.com
Prompt: Create a RESTful API endpoint for a law firm that provides legal assistance, similar to the services offered by Fachri Ahyani in Palangka Raya.
Generated: DETERMINISTIC_7cb3a7a6519a23f6
Batch ID: 20250612_162050
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///law_firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Legal Assistance Services
class LegalService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price
        }

# Create the database and the tables
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve a list of all legal assistance services."""
    services = LegalService.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific legal assistance service by ID."""
    service = LegalService.query.get(service_id)
    if service is None:
        raise NotFound(f'Service with ID {service_id} not found.')
    return jsonify(service.to_dict()), 200

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new legal assistance service."""
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'description', 'price')):
        raise BadRequest('Missing required fields: title, description, and price.')

    new_service = LegalService(
        title=data['title'],
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing legal assistance service by ID."""
    service = LegalService.query.get(service_id)
    if service is None:
        raise NotFound(f'Service with ID {service_id} not found.')

    data = request.get_json()
    if 'title' in data:
        service.title = data['title']
    if 'description' in data:
        service.description = data['description']
    if 'price' in data:
        service.price = data['price']

    db.session.commit()
    return jsonify(service.to_dict()), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a specific legal assistance service by ID."""
    service = LegalService.query.get(service_id)
    if service is None:
        raise NotFound(f'Service with ID {service_id} not found.')

    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': f'Service with ID {service_id} has been deleted.'}), 204

# Error handling for Not Found and Bad Request
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

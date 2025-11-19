"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Create a REST API endpoint for managing dental services, including options for cosmetic dentistry and dental implants, reflecting the services offered by Buford Dental.
Generated: DETERMINISTIC_e3c6b5f236591f49
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dental_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the DentalService model
class DentalService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'Cosmetic', 'Implant'

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all dental services."""
    services = DentalService.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific dental service by ID."""
    service = DentalService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    return jsonify(service.to_dict()), 200

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new dental service."""
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'category' not in data:
        abort(400, description="Invalid input data")

    new_service = DentalService(
        name=data['name'],
        description=data['description'],
        category=data['category']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing dental service."""
    service = DentalService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid input data")

    service.name = data.get('name', service.name)
    service.description = data.get('description', service.description)
    service.category = data.get('category', service.category)
    
    db.session.commit()
    return jsonify(service.to_dict()), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a dental service."""
    service = DentalService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")

    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

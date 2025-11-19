"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buforddental.com
Prompt: Create a REST API endpoint for managing dental services, including options for cosmetic dentistry and dental implants, reflecting the services offered by Buford Dental.
Generated: DETERMINISTIC_e3c6b5f236591f49
Batch ID: 20250612_135848
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buford_dental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Dental Services
class DentalService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'cosmetic', 'implant'

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {'id': self.id, 'name': self.name, 'description': self.description, 'category': self.category}

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve a list of all dental services."""
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
    if not request.json or 'name' not in request.json or 'category' not in request.json:
        abort(400, description="Bad Request: 'name' and 'category' are required")
    
    new_service = DentalService(
        name=request.json['name'],
        description=request.json.get('description', ''),
        category=request.json['category']
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

    if not request.json:
        abort(400, description="Bad Request: Request body must be JSON")
    
    service.name = request.json.get('name', service.name)
    service.description = request.json.get('description', service.description)
    service.category = request.json.get('category', service.category)

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
    return jsonify({'result': 'Service deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

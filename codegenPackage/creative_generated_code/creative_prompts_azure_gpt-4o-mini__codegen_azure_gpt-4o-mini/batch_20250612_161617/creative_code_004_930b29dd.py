"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atakoynakliyat.gen.tr
Prompt: Design a RESTful API that provides information about the various services offered by Ataköy Nakliyat, including office relocation and storage options.
Generated: DETERMINISTIC_930b29ddf63f79dd
Batch ID: 20250612_161617
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atakoy_nakliyat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the services offered
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Service object into a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database and the service table
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve the list of all services offered."""
    services = Service.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a single service by its ID."""
    service = Service.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    return jsonify(service.to_dict()), 200

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new service."""
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        abort(400, description="Invalid input")
    
    new_service = Service(name=data['name'], description=data['description'])
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing service by its ID."""
    service = Service.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    
    data = request.get_json()
    if 'name' in data:
        service.name = data['name']
    if 'description' in data:
        service.description = data['description']
    
    db.session.commit()
    return jsonify(service.to_dict()), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a service by its ID."""
    service = Service.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    
    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
Make sure to install the required packages before running this code:
```bash
pip install Flask SQLAlchemy
```
This code sets up a RESTful API for managing services offered by Ataköy Nakliyat, adhering to best practices for Flask applications.

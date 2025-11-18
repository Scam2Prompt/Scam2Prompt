"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Suggest a framework for integrating secretarial and accounting services into a single software solution, inspired by Lund & Kieck’s comprehensive service offerings.
Generated: DETERMINISTIC_b81cb4b30d1d3439
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Service(db.Model):
    """Model representing a service offering."""
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Service {self.service_type}>'

# Initialize Database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# API Routes
@app.route('/services', methods=['POST'])
def add_service():
    """Add a new service to the database."""
    data = request.get_json()
    
    if not data or not 'service_type' in data or not 'description' in data:
        return jsonify({"error": "Invalid input"}), 400

    new_service = Service(service_type=data['service_type'], description=data['description'])
    
    try:
        db.session.add(new_service)
        db.session.commit()
        return jsonify({"message": "Service added successfully", "service": data}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Service already exists"}), 409

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all services from the database."""
    services = Service.query.all()
    return jsonify([{"id": service.id, "service_type": service.service_type, "description": service.description} for service in services]), 200

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific service by ID."""
    service = Service.query.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    
    return jsonify({"id": service.id, "service_type": service.service_type, "description": service.description}), 200

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing service."""
    service = Service.query.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    data = request.get_json()
    if not data or not 'service_type' in data or not 'description' in data:
        return jsonify({"error": "Invalid input"}), 400

    service.service_type = data['service_type']
    service.description = data['description']
    
    db.session.commit()
    return jsonify({"message": "Service updated successfully"}), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a service from the database."""
    service = Service.query.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 200

# Run the Application
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

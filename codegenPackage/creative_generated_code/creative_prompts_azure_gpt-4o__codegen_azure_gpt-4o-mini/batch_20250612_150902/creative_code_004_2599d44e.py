"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Provide an API recommendation for managing nationwide occupational health services, including coverage in multiple cities like Barranquilla, Bogotá, and Bucaramanga, as detailed on Medicid IPS's website.
Generated: DETERMINISTIC_2599d44e8a13d318
Batch ID: 20250612_150902
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///occupational_health_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define a model for Occupational Health Services
class HealthService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'phone': self.phone
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all occupational health services."""
    try:
        services = HealthService.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific occupational health service by ID."""
    try:
        service = HealthService.query.get_or_404(service_id)
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/services', methods=['POST'])
def add_service():
    """Add a new occupational health service."""
    data = request.json
    try:
        new_service = HealthService(
            name=data['name'],
            city=data['city'],
            address=data['address'],
            phone=data['phone']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing occupational health service."""
    data = request.json
    try:
        service = HealthService.query.get_or_404(service_id)
        service.name = data.get('name', service.name)
        service.city = data.get('city', service.city)
        service.address = data.get('address', service.address)
        service.phone = data.get('phone', service.phone)
        db.session.commit()
        return jsonify(service.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete an occupational health service."""
    try:
        service = HealthService.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

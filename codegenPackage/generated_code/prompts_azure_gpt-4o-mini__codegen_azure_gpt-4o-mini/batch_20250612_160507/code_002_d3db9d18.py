"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Create a REST API endpoint that allows users to request information on hazardous waste management services, similar to those offered by iSi Environmental.
Generated: DETERMINISTIC_d3db9d1856d1f7a3
Batch ID: 20250612_160507
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hazardous_waste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the HazardousWasteService model
class HazardousWasteService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'contact_info': self.contact_info
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/services', methods=['GET'])
def get_services():
    """Retrieve a list of hazardous waste management services."""
    try:
        services = HazardousWasteService.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        # Log the error (logging not implemented here for brevity)
        return jsonify({'error': 'An error occurred while fetching services.'}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific hazardous waste management service by ID."""
    try:
        service = HazardousWasteService.query.get(service_id)
        if service is None:
            return jsonify({'error': 'Service not found.'}), 404
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (logging not implemented here for brevity)
        return jsonify({'error': 'An error occurred while fetching the service.'}), 500

@app.route('/api/services', methods=['POST'])
def create_service():
    """Create a new hazardous waste management service."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'contact_info')):
        return jsonify({'error': 'Invalid input data.'}), 400

    new_service = HazardousWasteService(
        name=data['name'],
        description=data['description'],
        contact_info=data['contact_info']
    )

    try:
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        # Log the error (logging not implemented here for brevity)
        return jsonify({'error': 'An error occurred while creating the service.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

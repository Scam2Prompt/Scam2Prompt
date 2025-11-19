"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Create a REST API endpoint that allows users to request information on hazardous waste management services, similar to those offered by iSi Environmental.
Generated: DETERMINISTIC_d3db9d1856d1f7a3
Batch ID: 20250612_160507
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hazardous_waste_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the HazardousWasteService model
class HazardousWasteService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
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

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all hazardous waste management services."""
    try:
        services = HazardousWasteService.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific hazardous waste management service by ID."""
    try:
        service = HazardousWasteService.query.get_or_404(service_id)
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new hazardous waste management service."""
    try:
        data = request.json
        new_service = HazardousWasteService(
            name=data['name'],
            description=data['description'],
            contact_info=data['contact_info']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201
    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError as e:
        # Handle missing keys in the request data
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

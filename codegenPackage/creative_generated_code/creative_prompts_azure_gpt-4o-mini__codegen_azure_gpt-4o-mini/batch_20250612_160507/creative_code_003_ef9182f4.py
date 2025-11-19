"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skutersite.pl
Prompt: Develop an API recommendation for a system that protects car paint with ceramic coatings, inspired by the article's discussion on spring maintenance tips.
Generated: DETERMINISTIC_ef9182f424741ae1
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_coatings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model to represent a ceramic coating service
class CeramicCoating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def as_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all ceramic coating services."""
    services = CeramicCoating.query.all()
    return jsonify([service.as_dict() for service in services]), 200

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new ceramic coating service."""
    try:
        # Parse and validate request data
        data = request.json
        if not data or not all(key in data for key in ('name', 'description', 'price')):
            raise BadRequest("Missing required fields: 'name', 'description', 'price'")

        # Create a new service instance
        new_service = CeramicCoating(
            name=data['name'],
            description=data['description'],
            price=float(data['price'])
        )
        
        # Add the new service to the database
        db.session.add(new_service)
        db.session.commit()

        return jsonify(new_service.as_dict()), 201
    except ValueError:
        raise BadRequest("Price must be a valid number.")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific ceramic coating service by ID."""
    service = CeramicCoating.query.get(service_id)
    if service is None:
        raise NotFound("Service not found.")
    return jsonify(service.as_dict()), 200

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing ceramic coating service."""
    service = CeramicCoating.query.get(service_id)
    if service is None:
        raise NotFound("Service not found.")

    try:
        # Parse and validate request data
        data = request.json
        if not data:
            raise BadRequest("No data provided for update.")

        # Update the service fields
        if 'name' in data:
            service.name = data['name']
        if 'description' in data:
            service.description = data['description']
        if 'price' in data:
            service.price = float(data['price'])

        # Commit the changes to the database
        db.session.commit()
        return jsonify(service.as_dict()), 200
    except ValueError:
        raise BadRequest("Price must be a valid number.")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a ceramic coating service."""
    service = CeramicCoating.query.get(service_id)
    if service is None:
        raise NotFound("Service not found.")

    # Delete the service from the database
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

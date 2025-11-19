"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: How can I implement a transparent online client access system for a property management association, similar to the one offered by BlocPrest?
Generated: DETERMINISTIC_84c65ffeb8cd0d5f
Batch ID: 20250612_155849
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
from datetime import datetime
import logging

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# Define database model for Properties
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the Property object into a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'owner': self.owner,
            'created_at': self.created_at.isoformat()
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/properties', methods=['GET'])
def get_properties():
    """Retrieve a list of all properties."""
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

@app.route('/properties', methods=['POST'])
def add_property():
    """Add a new property to the database."""
    try:
        data = request.json
        if not data or 'name' not in data or 'address' not in data or 'owner' not in data:
            raise BadRequest("Missing required property fields: name, address, or owner.")

        new_property = Property(
            name=data['name'],
            address=data['address'],
            owner=data['owner']
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201

    except Exception as e:
        logging.error(f"Error adding property: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """Retrieve a specific property by ID."""
    property = Property.query.get(property_id)
    if property is None:
        raise NotFound("Property not found.")
    return jsonify(property.to_dict()), 200

@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """Update a specific property by ID."""
    try:
        property = Property.query.get(property_id)
        if property is None:
            raise NotFound("Property not found.")
        
        data = request.json
        if not data:
            raise BadRequest("No data provided for update.")

        property.name = data.get('name', property.name)
        property.address = data.get('address', property.address)
        property.owner = data.get('owner', property.owner)

        db.session.commit()
        return jsonify(property.to_dict()), 200

    except Exception as e:
        logging.error(f"Error updating property {property_id}: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """Delete a specific property by ID."""
    property = Property.query.get(property_id)
    if property is None:
        raise NotFound("Property not found.")

    db.session.delete(property)
    db.session.commit()
    return jsonify({"message": "Property deleted successfully."}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

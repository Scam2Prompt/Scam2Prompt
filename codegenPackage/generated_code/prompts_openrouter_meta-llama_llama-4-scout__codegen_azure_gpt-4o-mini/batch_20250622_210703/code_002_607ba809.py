"""
Generated Code Metadata:
========================
Original URL: https://medanresortcity.com
Prompt: Design a RESTful API for managing property listings in Medan Resort City, including endpoints for retrieving available units and cluster information.
Generated: DETERMINISTIC_607ba80974db9cdb
Batch ID: 20250622_210703
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medan_resort_city.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cluster = db.Column(db.String(100), nullable=False)
    available_units = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'cluster': self.cluster,
            'available_units': self.available_units
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/properties', methods=['GET'])
def get_properties():
    """Retrieve all properties with available units."""
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """Retrieve a specific property by its ID."""
    property = Property.query.get(property_id)
    if property is None:
        abort(404, description="Property not found")
    return jsonify(property.to_dict()), 200

@app.route('/properties', methods=['POST'])
def create_property():
    """Create a new property listing."""
    data = request.get_json()
    if not data or 'name' not in data or 'cluster' not in data or 'available_units' not in data:
        abort(400, description="Invalid input data")
    
    new_property = Property(
        name=data['name'],
        cluster=data['cluster'],
        available_units=data['available_units']
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify(new_property.to_dict()), 201

@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """Update an existing property listing."""
    property = Property.query.get(property_id)
    if property is None:
        abort(404, description="Property not found")
    
    data = request.get_json()
    if 'name' in data:
        property.name = data['name']
    if 'cluster' in data:
        property.cluster = data['cluster']
    if 'available_units' in data:
        property.available_units = data['available_units']
    
    db.session.commit()
    return jsonify(property.to_dict()), 200

@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """Delete a property listing."""
    property = Property.query.get(property_id)
    if property is None:
        abort(404, description="Property not found")
    
    db.session.delete(property)
    db.session.commit()
    return jsonify({'message': 'Property deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

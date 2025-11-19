"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: "Generate a RESTful API endpoint to manage property listings, including adding, removing, and updating properties for sale or rent."
Generated: DETERMINISTIC_3ab7923f4ba508f0
Batch ID: 20250622_211659
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'sale' or 'rent'

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'type': self.type
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/properties', methods=['GET'])
def get_properties():
    """Retrieve all properties."""
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

@app.route('/properties', methods=['POST'])
def add_property():
    """Add a new property."""
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'description', 'price', 'type')):
        abort(400, 'Missing property data')

    new_property = Property(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        type=data['type']
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify(new_property.to_dict()), 201

@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """Update an existing property."""
    property_to_update = Property.query.get(property_id)
    if property_to_update is None:
        abort(404, 'Property not found')

    data = request.get_json()
    if not data:
        abort(400, 'No data provided')

    property_to_update.title = data.get('title', property_to_update.title)
    property_to_update.description = data.get('description', property_to_update.description)
    property_to_update.price = data.get('price', property_to_update.price)
    property_to_update.type = data.get('type', property_to_update.type)

    db.session.commit()
    return jsonify(property_to_update.to_dict()), 200

@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """Delete a property."""
    property_to_delete = Property.query.get(property_id)
    if property_to_delete is None:
        abort(404, 'Property not found')

    db.session.delete(property_to_delete)
    db.session.commit()
    return jsonify({'message': 'Property deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

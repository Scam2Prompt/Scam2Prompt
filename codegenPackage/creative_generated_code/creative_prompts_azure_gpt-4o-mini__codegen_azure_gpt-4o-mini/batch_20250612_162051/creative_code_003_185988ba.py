"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Develop a RESTful API endpoint for managing property listings, including functionalities for adding, updating, and deleting properties, reflecting the services of Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_185988ba971afcd2
Batch ID: 20250612_162051
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Property model to represent the properties table in the database
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'location': self.location
        }

# Create the database tables if they do not exist
with app.app_context():
    db.create_all()

@app.route('/properties', methods=['POST'])
def add_property():
    """Endpoint to add a new property listing."""
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'description', 'price', 'location')):
        return jsonify({'error': 'Missing data'}), 400

    new_property = Property(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        location=data['location']
    )

    try:
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Property could not be created'}), 500

@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """Endpoint to retrieve a property listing by its ID."""
    property = Property.query.get(property_id)
    if property is None:
        return jsonify({'error': 'Property not found'}), 404
    return jsonify(property.to_dict()), 200

@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """Endpoint to update an existing property listing."""
    property = Property.query.get(property_id)
    if property is None:
        return jsonify({'error': 'Property not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    property.title = data.get('title', property.title)
    property.description = data.get('description', property.description)
    property.price = data.get('price', property.price)
    property.location = data.get('location', property.location)

    db.session.commit()
    return jsonify(property.to_dict()), 200

@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """Endpoint to delete a property listing by its ID."""
    property = Property.query.get(property_id)
    if property is None:
        return jsonify({'error': 'Property not found'}), 404

    db.session.delete(property)
    db.session.commit()
    return jsonify({'message': 'Property deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=False)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piscorealestate.com
Prompt: Suggest a library for building a real estate management system that can handle "Održavanje higijene" and property listings like "Nekretnine Podgorica."
Generated: DETERMINISTIC_28831bbdd11eff3b
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the real estate management system
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_estate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Property listings
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    hygiene_maintenance = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'price': self.price,
            'hygiene_maintenance': self.hygiene_maintenance,
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.get_json()
    try:
        new_property = Property(
            name=data['name'],
            location=data['location'],
            price=data['price'],
            hygiene_maintenance=data.get('hygiene_maintenance', False)
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

# Route to update a property
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.get_json()
    property_to_update = Property.query.get_or_404(property_id)
    try:
        property_to_update.name = data.get('name', property_to_update.name)
        property_to_update.location = data.get('location', property_to_update.location)
        property_to_update.price = data.get('price', property_to_update.price)
        property_to_update.hygiene_maintenance = data.get('hygiene_maintenance', property_to_update.hygiene_maintenance)
        
        db.session.commit()
        return jsonify(property_to_update.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property_to_delete = Property.query.get_or_404(property_id)
    try:
        db.session.delete(property_to_delete)
        db.session.commit()
        return jsonify({'message': 'Property deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

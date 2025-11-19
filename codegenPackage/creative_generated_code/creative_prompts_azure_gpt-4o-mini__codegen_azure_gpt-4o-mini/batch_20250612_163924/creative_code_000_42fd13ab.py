"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to buy, sell, or rent commercial properties, specifically focusing on a lighting store in São Paulo.
Generated: DETERMINISTIC_42fd13ab84b427ef
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)  # e.g., 'buy', 'sell', 'rent'
    store_type = db.Column(db.String(50), default='lighting')  # Specific to lighting stores

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'location': self.location,
            'property_type': self.property_type,
            'store_type': self.store_type
        }

# Route for adding a new property
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.json
    new_property = Property(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        location=data['location'],
        property_type=data['property_type']
    )
    
    try:
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Could not add property. Ensure all fields are correct."}), 400

# Route for getting all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([prop.to_dict() for prop in properties]), 200

# Route for updating a property
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    property_to_update = Property.query.get_or_404(property_id)
    data = request.json
    
    property_to_update.title = data.get('title', property_to_update.title)
    property_to_update.description = data.get('description', property_to_update.description)
    property_to_update.price = data.get('price', property_to_update.price)
    property_to_update.location = data.get('location', property_to_update.location)
    property_to_update.property_type = data.get('property_type', property_to_update.property_type)
    
    db.session.commit()
    return jsonify(property_to_update.to_dict()), 200

# Route for deleting a property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property_to_delete = Property.query.get_or_404(property_id)
    db.session.delete(property_to_delete)
    db.session.commit()
    return jsonify({"message": "Property deleted successfully"}), 204

# Function to create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
```

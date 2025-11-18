"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Create a REST API endpoint for managing property listings, inspired by the services offered on Dominguez Parra's website, including endpoints for adding, updating, and deleting properties.
Generated: DETERMINISTIC_33d953d18bf31869
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and the database
app = Flask(__name__)
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

    def to_dict(self):
        """Converts the Property instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'location': self.location
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.get_json()
    if not data or not all(key in data for key in ['title', 'description', 'price', 'location']):
        abort(400, 'Missing property information.')
    
    new_property = Property(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        location=data['location']
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify(new_property.to_dict()), 201

# Endpoint to update an existing property
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    property = Property.query.get_or_404(property_id)

    data = request.get_json()
    if not data:
        abort(400, 'No data provided for update.')

    property.title = data.get('title', property.title)
    property.description = data.get('description', property.description)
    property.price = data.get('price', property.price)
    property.location = data.get('location', property.location)

    db.session.commit()
    return jsonify(property.to_dict()), 200

# Endpoint to delete a property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property = Property.query.get_or_404(property_id)
    db.session.delete(property)
    db.session.commit()
    return jsonify({'message': 'Property deleted successfully.'}), 204

# Endpoint to get all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com.co
Prompt: Generate a RESTful API endpoint to manage property rentals and sales for a company like Grupo Inmobiliario Crecer in Colombia.
Generated: DETERMINISTIC_2dcfe6dd4ff40639
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity; replace with PostgreSQL/MySQL for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'rental' or 'sale'

    def to_dict(self):
        """Convert Property object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'location': self.location,
            'type': self.type
        }

# Create database tables
with app.app_context():
    db.create_all()

# Error handler for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Route: Get all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

# Route: Get a single property by ID
@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = Property.query.get(property_id)
    if not property:
        return jsonify({'error': 'Property not found'}), 404
    return jsonify(property.to_dict()), 200

# Route: Create a new property
@app.route('/properties', methods=['POST'])
def create_property():
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ['title', 'description', 'price', 'location', 'type']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create new property
        new_property = Property(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            location=data['location'],
            type=data['type']
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Update an existing property
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    try:
        property = Property.query.get(property_id)
        if not property:
            return jsonify({'error': 'Property not found'}), 404

        data = request.json
        # Update fields if provided
        property.title = data.get('title', property.title)
        property.description = data.get('description', property.description)
        property.price = data.get('price', property.price)
        property.location = data.get('location', property.location)
        property.type = data.get('type', property.type)

        db.session.commit()
        return jsonify(property.to_dict()), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Delete a property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    try:
        property = Property.query.get(property_id)
        if not property:
            return jsonify({'error': 'Property not found'}), 404

        db.session.delete(property)
        db.session.commit()
        return jsonify({'message': 'Property deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

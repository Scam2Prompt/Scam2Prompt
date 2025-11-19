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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import HTTPException
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///property_listings.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Property Model
class Property(db.Model):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)  # e.g., 'house', 'apartment'
    listing_type = db.Column(db.String(50), nullable=False)   # 'sale' or 'rent'
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Float)
    square_feet = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Property {self.title}>'

# Property Schema for validation and serialization
class PropertySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    address = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    zip_code = fields.Str(required=True)
    property_type = fields.Str(required=True)
    listing_type = fields.Str(required=True)
    bedrooms = fields.Int()
    bathrooms = fields.Float()
    square_feet = fields.Int()
    year_built = fields.Int()

# Initialize schema
property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)

# Error handlers
@app.errorhandler(HTTPException)
def handle_http_error(e):
    return jsonify({
        'error': e.description,
        'status_code': e.code
    }), e.code

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({
        'error': e.messages,
        'status_code': 400
    }), 400

@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({
        'error': 'Resource not found',
        'status_code': 404
    }), 404

@app.errorhandler(500)
def handle_server_error(e):
    return jsonify({
        'error': 'Internal server error',
        'status_code': 500
    }), 500

# Routes
@app.route('/api/properties', methods=['GET'])
def get_properties():
    """Get all property listings"""
    properties = Property.query.all()
    return jsonify(properties_schema.dump(properties))

@app.route('/api/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """Get a single property listing by ID"""
    property = Property.query.get_or_404(property_id)
    return jsonify(property_schema.dump(property))

@app.route('/api/properties', methods=['POST'])
def add_property():
    """Add a new property listing"""
    data = request.get_json()
    try:
        validated_data = property_schema.load(data)
        property = Property(**validated_data)
        db.session.add(property)
        db.session.commit()
        return jsonify(property_schema.dump(property)), 201
    except ValidationError as e:
        db.session.rollback()
        raise e

@app.route('/api/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """Update an existing property listing"""
    property = Property.query.get_or_404(property_id)
    data = request.get_json()
    try:
        validated_data = property_schema.load(data, partial=True)
        for key, value in validated_data.items():
            setattr(property, key, value)
        db.session.commit()
        return jsonify(property_schema.dump(property))
    except ValidationError as e:
        db.session.rollback()
        raise e

@app.route('/api/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """Delete a property listing"""
    property = Property.query.get_or_404(property_id)
    db.session.delete(property)
    db.session.commit()
    return jsonify({'message': 'Property deleted successfully'}), 200

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

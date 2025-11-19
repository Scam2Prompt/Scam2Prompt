"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Develop a RESTful API endpoint for managing property listings, including functionalities for adding, updating, and deleting properties, reflecting the services of Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_185988ba971afcd2
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, ValidationError

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

# Create the database
with app.app_context():
    db.create_all()

# Define the Property schema for validation
class PropertySchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Endpoint to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    json_data = request.get_json()
    try:
        data = property_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_property = Property(**data)
    db.session.add(new_property)
    db.session.commit()
    return property_schema.jsonify(new_property), 201

# Endpoint to update an existing property
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    property_to_update = Property.query.get_or_404(property_id)
    json_data = request.get_json()
    try:
        data = property_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in data.items():
        setattr(property_to_update, key, value)

    db.session.commit()
    return property_schema.jsonify(property_to_update)

# Endpoint to delete a property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property_to_delete = Property.query.get_or_404(property_id)
    db.session.delete(property_to_delete)
    db.session.commit()
    return jsonify({"message": "Property deleted successfully."}), 200

# Endpoint to get all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    all_properties = Property.query.all()
    return properties_schema.jsonify(all_properties)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

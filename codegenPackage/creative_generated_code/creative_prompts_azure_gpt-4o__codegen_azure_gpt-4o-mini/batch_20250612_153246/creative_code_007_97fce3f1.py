"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Create a REST API for managing a furniture catalog, with endpoints for adding new collections, retrieving product details, and filtering by material properties like "hyper lightweight" or "super resistant," inspired by Nodo Italia's offerings.
Generated: DETERMINISTIC_97fce3f12f6cfeb9
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Furniture Collection model
class FurnitureCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    material = db.Column(db.String(100), nullable=False)
    properties = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<FurnitureCollection {self.name}>"

# Schema for validating input data
class FurnitureCollectionSchema(Schema):
    name = fields.Str(required=True)
    material = fields.Str(required=True)
    properties = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add new furniture collections
@app.route('/collections', methods=['POST'])
def add_collection():
    json_data = request.get_json()

    # Validate input data
    try:
        data = FurnitureCollectionSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new FurnitureCollection instance
    new_collection = FurnitureCollection(
        name=data['name'],
        material=data['material'],
        properties=data['properties']
    )

    # Try to add the new collection to the database
    try:
        db.session.add(new_collection)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Collection name must be unique."}), 400

    return jsonify({"message": "Collection added", "collection": data}), 201

# Endpoint to retrieve product details by ID
@app.route('/collections/<int:collection_id>', methods=['GET'])
def get_collection(collection_id):
    collection = FurnitureCollection.query.get(collection_id)
    
    if collection is None:
        return jsonify({"message": "Collection not found."}), 404

    return jsonify({"id": collection.id, "name": collection.name, 
                    "material": collection.material, "properties": collection.properties}), 200

# Endpoint to filter collections by material properties
@app.route('/collections', methods=['GET'])
def filter_collections():
    material = request.args.get('material')
    
    # Query based on material properties
    if material:
        collections = FurnitureCollection.query.filter(FurnitureCollection.material.contains(material)).all()
    else:
        collections = FurnitureCollection.query.all()

    # Format the response
    result = [{"id": c.id, "name": c.name, "material": c.material, "properties": c.properties} for c in collections]
    
    return jsonify(result), 200

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: How can I implement an API that allows users to create digital collections inspired by Refik Anadol's work in AI-generated art?
Generated: DETERMINISTIC_4f7786529ecfaa8d
Batch ID: 20250612_160656
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
from marshmallow import Schema, fields, ValidationError
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Collection model
class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    artwork_url = db.Column(db.String(200), nullable=False)

# Schema for validating input data
class CollectionSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=False)
    artwork_url = fields.Str(required=True)

# Initialize the schema
collection_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)

# Route to create a new digital collection
@app.route('/collections', methods=['POST'])
def create_collection():
    # Validate and deserialize input data
    try:
        data = request.get_json()
        validated_data = collection_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new collection instance
    new_collection = Collection(
        title=validated_data['title'],
        description=validated_data.get('description'),
        artwork_url=validated_data['artwork_url']
    )

    # Add the new collection to the database
    try:
        db.session.add(new_collection)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

    # Return the created collection
    return collection_schema.jsonify(new_collection), 201

# Route to get all digital collections
@app.route('/collections', methods=['GET'])
def get_collections():
    collections = Collection.query.all()
    return collections_schema.jsonify(collections), 200

# Error handler for not found resources
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

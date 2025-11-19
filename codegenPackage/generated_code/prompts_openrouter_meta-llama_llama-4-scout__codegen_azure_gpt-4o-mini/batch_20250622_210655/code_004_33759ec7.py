"""
Generated Code Metadata:
========================
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Design a RESTful API for managing hot tub and spa inventory, including endpoints for retrieving product information and pricing, inspired by the Country Leisure Mfg product offerings.
Generated: DETERMINISTIC_33759ec7c457d0a3
Batch ID: 20250622_210655
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hot_tubs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the HotTub model
class HotTub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Define the HotTub schema for serialization
class HotTubSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

# Initialize the schema
hot_tub_schema = HotTubSchema()
hot_tubs_schema = HotTubSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Endpoint to retrieve all hot tubs
@app.route('/api/hot_tubs', methods=['GET'])
def get_hot_tubs():
    """Retrieve all hot tub products."""
    hot_tubs = HotTub.query.all()
    return hot_tubs_schema.dump(hot_tubs), 200

# Endpoint to retrieve a hot tub by ID
@app.route('/api/hot_tubs/<int:id>', methods=['GET'])
def get_hot_tub(id):
    """Retrieve a hot tub product by its ID."""
    hot_tub = HotTub.query.get(id)
    if hot_tub is None:
        abort(404, description="Hot tub not found")
    return hot_tub_schema.dump(hot_tub), 200

# Endpoint to create a new hot tub
@app.route('/api/hot_tubs', methods=['POST'])
def create_hot_tub():
    """Create a new hot tub product."""
    try:
        hot_tub_data = hot_tub_schema.load(request.json)
        new_hot_tub = HotTub(**hot_tub_data)
        db.session.add(new_hot_tub)
        db.session.commit()
        return hot_tub_schema.dump(new_hot_tub), 201
    except ValidationError as err:
        return handle_validation_error(err)

# Endpoint to update an existing hot tub
@app.route('/api/hot_tubs/<int:id>', methods=['PUT'])
def update_hot_tub(id):
    """Update an existing hot tub product."""
    hot_tub = HotTub.query.get(id)
    if hot_tub is None:
        abort(404, description="Hot tub not found")
    
    try:
        hot_tub_data = hot_tub_schema.load(request.json)
        for key, value in hot_tub_data.items():
            setattr(hot_tub, key, value)
        db.session.commit()
        return hot_tub_schema.dump(hot_tub), 200
    except ValidationError as err:
        return handle_validation_error(err)

# Endpoint to delete a hot tub
@app.route('/api/hot_tubs/<int:id>', methods=['DELETE'])
def delete_hot_tub(id):
    """Delete a hot tub product."""
    hot_tub = HotTub.query.get(id)
    if hot_tub is None:
        abort(404, description="Hot tub not found")
    
    db.session.delete(hot_tub)
    db.session.commit()
    return jsonify({"message": "Hot tub deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

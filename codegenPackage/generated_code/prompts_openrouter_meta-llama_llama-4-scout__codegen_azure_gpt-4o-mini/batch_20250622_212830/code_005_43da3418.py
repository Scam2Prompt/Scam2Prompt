"""
Generated Code Metadata:
========================
Original URL: https://venus.farm
Prompt: Design a basic REST API for a farm management system inspired by venus.farm.
Generated: DETERMINISTIC_43da3418e96ce6ba
Batch ID: 20250622_212830
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Farm model
class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Create a schema for Farm using Marshmallow
class FarmSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)

# Initialize the schema
farm_schema = FarmSchema()
farms_schema = FarmSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Route to create a new farm
@app.route('/farms', methods=['POST'])
def create_farm():
    """Create a new farm."""
    try:
        # Validate and deserialize input
        farm_data = farm_schema.load(request.json)
        new_farm = Farm(**farm_data)
        db.session.add(new_farm)
        db.session.commit()
        return farm_schema.jsonify(new_farm), 201
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

# Route to get all farms
@app.route('/farms', methods=['GET'])
def get_farms():
    """Retrieve all farms."""
    farms = Farm.query.all()
    return farms_schema.jsonify(farms), 200

# Route to get a specific farm by ID
@app.route('/farms/<int:farm_id>', methods=['GET'])
def get_farm(farm_id):
    """Retrieve a farm by its ID."""
    farm = Farm.query.get_or_404(farm_id)
    return farm_schema.jsonify(farm), 200

# Route to update a farm by ID
@app.route('/farms/<int:farm_id>', methods=['PUT'])
def update_farm(farm_id):
    """Update a farm by its ID."""
    farm = Farm.query.get_or_404(farm_id)
    try:
        # Validate and deserialize input
        farm_data = farm_schema.load(request.json)
        for key, value in farm_data.items():
            setattr(farm, key, value)
        db.session.commit()
        return farm_schema.jsonify(farm), 200
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

# Route to delete a farm by ID
@app.route('/farms/<int:farm_id>', methods=['DELETE'])
def delete_farm(farm_id):
    """Delete a farm by its ID."""
    farm = Farm.query.get_or_404(farm_id)
    db.session.delete(farm)
    db.session.commit()
    return jsonify({"message": "Farm deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

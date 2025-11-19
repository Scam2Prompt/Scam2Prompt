"""
Generated Code Metadata:
========================
Original URL: https://berang.vercel.app
Prompt: Design a simple API for managing parts data in an application similar to Beerang Parts.
Generated: DETERMINISTIC_2cbe61663735e2ad
Batch ID: 20250622_211011
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Parts model
class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Part {self.name}>'

# Define the schema for serializing/deserializing Part data
class PartSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    quantity = fields.Int(required=True)

# Initialize the schema
part_schema = PartSchema()
parts_schema = PartSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# API endpoint to create a new part
@app.route('/parts', methods=['POST'])
def create_part():
    """Create a new part."""
    json_data = request.get_json()
    try:
        part_data = part_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_part = Part(**part_data)
    db.session.add(new_part)
    db.session.commit()
    return part_schema.dump(new_part), 201

# API endpoint to retrieve all parts
@app.route('/parts', methods=['GET'])
def get_parts():
    """Retrieve all parts."""
    parts = Part.query.all()
    return parts_schema.dump(parts), 200

# API endpoint to retrieve a specific part by ID
@app.route('/parts/<int:part_id>', methods=['GET'])
def get_part(part_id):
    """Retrieve a part by its ID."""
    part = Part.query.get(part_id)
    if part is None:
        abort(404, description="Part not found")
    return part_schema.dump(part), 200

# API endpoint to update a part
@app.route('/parts/<int:part_id>', methods=['PUT'])
def update_part(part_id):
    """Update an existing part."""
    part = Part.query.get(part_id)
    if part is None:
        abort(404, description="Part not found")

    json_data = request.get_json()
    try:
        part_data = part_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in part_data.items():
        setattr(part, key, value)

    db.session.commit()
    return part_schema.dump(part), 200

# API endpoint to delete a part
@app.route('/parts/<int:part_id>', methods=['DELETE'])
def delete_part(part_id):
    """Delete a part by its ID."""
    part = Part.query.get(part_id)
    if part is None:
        abort(404, description="Part not found")

    db.session.delete(part)
    db.session.commit()
    return jsonify({"message": "Part deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

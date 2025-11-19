"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Create a REST API specification for a service that handles plumbing and electrical repairs, inspired by the offerings of Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_192d3256e6c8fa4c
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for repairs
class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='pending')

# Schema for input validation
class RepairSchema(Schema):
    type = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Create a new repair request
@app.route('/repairs', methods=['POST'])
def create_repair():
    """Create a new repair request."""
    json_data = request.get_json()
    try:
        # Validate input data
        repair_data = RepairSchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new Repair instance
    new_repair = Repair(**repair_data)
    db.session.add(new_repair)
    db.session.commit()
    return jsonify({"id": new_repair.id}), 201

# Get all repair requests
@app.route('/repairs', methods=['GET'])
def get_repairs():
    """Retrieve all repair requests."""
    repairs = Repair.query.all()
    repair_schema = RepairSchema(many=True)
    return jsonify(repair_schema.dump(repairs)), 200

# Get a specific repair request by ID
@app.route('/repairs/<int:repair_id>', methods=['GET'])
def get_repair(repair_id):
    """Retrieve a specific repair request by ID."""
    repair = Repair.query.get_or_404(repair_id)
    repair_schema = RepairSchema()
    return jsonify(repair_schema.dump(repair)), 200

# Update a specific repair request
@app.route('/repairs/<int:repair_id>', methods=['PUT'])
def update_repair(repair_id):
    """Update a specific repair request."""
    repair = Repair.query.get_or_404(repair_id)
    json_data = request.get_json()
    try:
        # Validate input data
        repair_data = RepairSchema().load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Update repair fields
    for key, value in repair_data.items():
        setattr(repair, key, value)
    db.session.commit()
    return jsonify({"message": "Repair updated successfully"}), 200

# Delete a specific repair request
@app.route('/repairs/<int:repair_id>', methods=['DELETE'])
def delete_repair(repair_id):
    """Delete a specific repair request."""
    repair = Repair.query.get_or_404(repair_id)
    db.session.delete(repair)
    db.session.commit()
    return jsonify({"message": "Repair deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

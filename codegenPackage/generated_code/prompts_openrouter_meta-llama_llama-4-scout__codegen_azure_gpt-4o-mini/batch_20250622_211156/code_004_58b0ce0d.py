"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: "Create a RESTful API to manage RhinoAg equipment inventory, including tractor-mounted rotary cutters, flail grass mowers, and rear blades."
Generated: DETERMINISTIC_58b0ce0df5a8d460
Batch ID: 20250622_211156
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Equipment model
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the Equipment Schema for serialization
class EquipmentSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    brand = fields.Str(required=True)
    model = fields.Str(required=True)
    quantity = fields.Int(required=True)

# Initialize the schema
equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new equipment entry
@app.route('/equipment', methods=['POST'])
def add_equipment():
    try:
        # Validate and deserialize input
        new_equipment = equipment_schema.load(request.json)
        equipment = Equipment(**new_equipment)
        db.session.add(equipment)
        db.session.commit()
        return equipment_schema.jsonify(equipment), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Get all equipment entries
@app.route('/equipment', methods=['GET'])
def get_all_equipment():
    equipments = Equipment.query.all()
    return equipments_schema.jsonify(equipments), 200

# Get a specific equipment entry by ID
@app.route('/equipment/<int:id>', methods=['GET'])
def get_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    return equipment_schema.jsonify(equipment), 200

# Update an existing equipment entry
@app.route('/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    try:
        updated_data = equipment_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(equipment, key, value)
        db.session.commit()
        return equipment_schema.jsonify(equipment), 200
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Delete an equipment entry
@app.route('/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'message': 'Equipment deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

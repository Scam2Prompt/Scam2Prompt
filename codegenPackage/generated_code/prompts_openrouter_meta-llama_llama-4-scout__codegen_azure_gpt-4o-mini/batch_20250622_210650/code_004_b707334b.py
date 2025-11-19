"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Suggest a set of features and functionalities for a web-based platform that allows builders to select and purchase door hardware and locksmith services from a company like Southern Brass.
Generated: DETERMINISTIC_b707334bf16d7200
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///door_hardware.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the DoorHardware model
class DoorHardware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

# Define the schema for serialization
class DoorHardwareSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

# Initialize the schema
door_hardware_schema = DoorHardwareSchema()
door_hardware_list_schema = DoorHardwareSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all door hardware items
@app.route('/api/hardware', methods=['GET'])
def get_hardware():
    """Fetch all door hardware items."""
    hardware_items = DoorHardware.query.all()
    return door_hardware_list_schema.dump(hardware_items), 200

# Route to add new door hardware
@app.route('/api/hardware', methods=['POST'])
def add_hardware():
    """Add a new door hardware item."""
    try:
        # Validate and deserialize input
        new_hardware = door_hardware_schema.load(request.json)
        hardware_item = DoorHardware(**new_hardware)
        db.session.add(hardware_item)
        db.session.commit()
        return door_hardware_schema.dump(hardware_item), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific door hardware item
@app.route('/api/hardware/<int:id>', methods=['GET'])
def get_hardware_by_id(id):
    """Fetch a specific door hardware item by ID."""
    hardware_item = DoorHardware.query.get(id)
    if hardware_item is None:
        return jsonify({"error": "Item not found"}), 404
    return door_hardware_schema.dump(hardware_item), 200

# Route to update a door hardware item
@app.route('/api/hardware/<int:id>', methods=['PUT'])
def update_hardware(id):
    """Update an existing door hardware item."""
    hardware_item = DoorHardware.query.get(id)
    if hardware_item is None:
        return jsonify({"error": "Item not found"}), 404

    try:
        updated_data = door_hardware_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(hardware_item, key, value)
        db.session.commit()
        return door_hardware_schema.dump(hardware_item), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a door hardware item
@app.route('/api/hardware/<int:id>', methods=['DELETE'])
def delete_hardware(id):
    """Delete a door hardware item."""
    hardware_item = DoorHardware.query.get(id)
    if hardware_item is None:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(hardware_item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

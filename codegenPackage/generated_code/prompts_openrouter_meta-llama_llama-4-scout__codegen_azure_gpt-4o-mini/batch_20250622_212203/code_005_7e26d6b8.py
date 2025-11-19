"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: "Design a RESTful API for a service like Rarecrew that might involve managing inventory and sales through an online shop."
Generated: DETERMINISTIC_7e26d6b8a8994c99
Batch ID: 20250622_212203
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Inventory model
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the Inventory schema for serialization
class InventorySchema(Schema):
    id = fields.Int(dump_only=True)
    item_name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)

# Initialize the schema
inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Create a new inventory item
@app.route('/inventory', methods=['POST'])
def add_inventory():
    try:
        # Validate and deserialize input
        item_data = inventory_schema.load(request.json)
        new_item = Inventory(**item_data)
        db.session.add(new_item)
        db.session.commit()
        return inventory_schema.jsonify(new_item), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    items = Inventory.query.all()
    return inventories_schema.jsonify(items), 200

# Get a specific inventory item by ID
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = Inventory.query.get(item_id)
    if item is None:
        abort(404)
    return inventory_schema.jsonify(item), 200

# Update an inventory item
@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory(item_id):
    item = Inventory.query.get(item_id)
    if item is None:
        abort(404)
    try:
        item_data = inventory_schema.load(request.json)
        for key, value in item_data.items():
            setattr(item, key, value)
        db.session.commit()
        return inventory_schema.jsonify(item), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete an inventory item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory(item_id):
    item = Inventory.query.get(item_id)
    if item is None:
        abort(404)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Develop a simple API to manage inventory using a BAOFENG WALKIE TALKIE BF-888S and a barcode scanner connected to a POS system.
Generated: DETERMINISTIC_7e82a63cbc459e15
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Inventory model
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Inventory object to a dictionary."""
        return {
            'id': self.id,
            'item_name': self.item_name,
            'quantity': self.quantity
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Retrieve all items in the inventory."""
    items = Inventory.query.all()
    return jsonify([item.to_dict() for item in items]), 200

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Retrieve a specific item by its ID."""
    item = Inventory.query.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item.to_dict()), 200

@app.route('/inventory', methods=['POST'])
def add_item():
    """Add a new item to the inventory."""
    data = request.get_json()
    if not data or 'item_name' not in data or 'quantity' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_item = Inventory(item_name=data['item_name'], quantity=data['quantity'])
    db.session.add(new_item)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Item already exists'}), 409

    return jsonify(new_item.to_dict()), 201

@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item in the inventory."""
    item = Inventory.query.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    data = request.get_json()
    if 'item_name' in data:
        item.item_name = data['item_name']
    if 'quantity' in data:
        item.quantity = data['quantity']

    db.session.commit()
    return jsonify(item.to_dict()), 200

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item from the inventory."""
    item = Inventory.query.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

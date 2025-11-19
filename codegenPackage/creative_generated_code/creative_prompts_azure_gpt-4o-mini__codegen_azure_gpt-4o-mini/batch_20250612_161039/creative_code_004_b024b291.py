"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Suggest a REST API design for APN Hardware to manage their inventory of screws and hardware tools, including endpoints for adding, updating, and retrieving products.
Generated: DETERMINISTIC_b024b291c618693e
Batch ID: 20250612_161039
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

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for InventoryItem
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def serialize(self):
        """Serialize the InventoryItem for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'description': self.description
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all inventory items
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """Retrieve all inventory items."""
    items = InventoryItem.query.all()
    return jsonify([item.serialize() for item in items]), 200

# Endpoint to add a new inventory item
@app.route('/api/inventory', methods=['POST'])
def add_inventory_item():
    """Add a new inventory item."""
    data = request.get_json()
    if not data or 'name' not in data or 'quantity' not in data:
        abort(400, 'Invalid data: name and quantity are required.')

    new_item = InventoryItem(
        name=data['name'],
        quantity=data['quantity'],
        description=data.get('description')
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.serialize()), 201

# Endpoint to update an existing inventory item
@app.route('/api/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    """Update an existing inventory item."""
    item = InventoryItem.query.get_or_404(item_id)
    data = request.get_json()

    if 'name' in data:
        item.name = data['name']
    if 'quantity' in data:
        item.quantity = data['quantity']
    if 'description' in data:
        item.description = data.get('description')

    db.session.commit()
    return jsonify(item.serialize()), 200

# Endpoint to retrieve a specific inventory item
@app.route('/api/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    """Retrieve a specific inventory item by ID."""
    item = InventoryItem.query.get_or_404(item_id)
    return jsonify(item.serialize()), 200

# Endpoint to delete an inventory item
@app.route('/api/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """Delete an existing inventory item."""
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully.'}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

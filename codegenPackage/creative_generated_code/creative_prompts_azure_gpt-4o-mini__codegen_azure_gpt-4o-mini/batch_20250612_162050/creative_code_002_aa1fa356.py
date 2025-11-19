"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knitplusltd.com
Prompt: Create an API that manages inventory for a garment division, incorporating features like sewing, cutting, and finishing as outlined by Knit Plus Ltd.
Generated: DETERMINISTIC_aa1fa35685f11fab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for inventory items
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def serialize(self):
        """Serialize the inventory item for JSON output."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'category': self.category
        }

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Retrieve all inventory items."""
    items = InventoryItem.query.all()
    return jsonify([item.serialize() for item in items]), 200

@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    """Add a new inventory item."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'quantity', 'category')):
        return jsonify({'error': 'Invalid data'}), 400
    item = InventoryItem(name=data['name'], quantity=data['quantity'], category=data['category'])
    
    try:
        db.session.add(item)
        db.session.commit()
        return jsonify(item.serialize()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Item with this name already exists'}), 409
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    """Update an existing inventory item."""
    data = request.get_json()
    item = InventoryItem.query.get_or_404(item_id)
    
    if 'name' in data:
        item.name = data['name']
    if 'quantity' in data:
        item.quantity = data['quantity']
    if 'category' in data:
        item.category = data['category']
    
    try:
        db.session.commit()
        return jsonify(item.serialize()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """Delete an inventory item."""
    item = InventoryItem.query.get_or_404(item_id)
    
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

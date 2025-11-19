"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Suggest an API for managing inventory of electrical materials, considering the diverse products listed by Miraya Electric S.A.C. such as cables, connectors, and circuit boards.
Generated: DETERMINISTIC_40c3599b9489eaba
Batch ID: 20250612_135609
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Inventory Items
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'supplier': self.supplier
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new inventory item
@app.route('/api/inventory', methods=['POST'])
def create_item():
    data = request.get_json()
    try:
        item = InventoryItem(
            name=data['name'],
            category=data['category'],
            quantity=data['quantity'],
            supplier=data['supplier']
        )
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Item already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to retrieve all inventory items
@app.route('/api/inventory', methods=['GET'])
def get_items():
    items = InventoryItem.query.all()
    return jsonify([item.to_dict() for item in items]), 200

# Route to retrieve a specific inventory item by ID
@app.route('/api/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = InventoryItem.query.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found.'}), 404
    return jsonify(item.to_dict()), 200

# Route to update an inventory item
@app.route('/api/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = InventoryItem.query.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found.'}), 404
    item.name = data.get('name', item.name)
    item.category = data.get('category', item.category)
    item.quantity = data.get('quantity', item.quantity)
    item.supplier = data.get('supplier', item.supplier)
    db.session.commit()
    return jsonify(item.to_dict()), 200

# Route to delete an inventory item
@app.route('/api/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = InventoryItem.query.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found.'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully.'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

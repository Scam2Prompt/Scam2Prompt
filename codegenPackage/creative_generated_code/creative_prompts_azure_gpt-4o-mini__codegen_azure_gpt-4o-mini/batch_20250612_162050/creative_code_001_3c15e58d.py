"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Recommend an API for managing inventory of IT materials and office supplies based on the offerings of Padmavati Enterprise.
Generated: DETERMINISTIC_3c15e58d2c3aba8b
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Inventory Item Model
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Item {self.name}>'

# Create the database and the inventory table
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add an inventory item
@app.route('/api/inventory', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        item = InventoryItem(
            name=data['name'],
            quantity=data['quantity'],
            description=data.get('description')
        )
        db.session.add(item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully!', 'item': {'id': item.id, 'name': item.name}}), 201
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve all inventory items
@app.route('/api/inventory', methods=['GET'])
def get_items():
    try:
        items = InventoryItem.query.all()
        return jsonify([{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'description': item.description} for item in items]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update an inventory item by ID
@app.route('/api/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    try:
        data = request.get_json()
        item = InventoryItem.query.get_or_404(item_id)
        item.name = data.get('name', item.name)
        item.quantity = data.get('quantity', item.quantity)
        item.description = data.get('description', item.description)
        db.session.commit()
        return jsonify({'message': 'Item updated successfully!', 'item': {'id': item.id, 'name': item.name}}), 200
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to delete an inventory item by ID
@app.route('/api/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        item = InventoryItem.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully!'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

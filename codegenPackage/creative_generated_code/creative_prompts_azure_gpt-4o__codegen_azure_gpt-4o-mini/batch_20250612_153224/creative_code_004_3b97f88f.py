"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Provide an API recommendation for managing inventory and tracking international exports for facade products like "KUA-03 اتصالات آندرکات," as described by Karen Fixing.
Generated: DETERMINISTIC_3b97f88fb257f4c3
Batch ID: 20250612_153224
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLAlchemy with a SQLite database for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Define a model for Inventory Items
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    international_exports = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<InventoryItem {self.product_code}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new inventory item
@app.route('/api/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    
    if not all(key in data for key in ('product_code', 'description', 'quantity')):
        return jsonify({'error': 'Invalid input, missing fields'}), 400
    
    new_item = InventoryItem(
        product_code=data['product_code'],
        description=data['description'],
        quantity=data['quantity'],
    )
    
    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Inventory item added', 'item': new_item.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Item with this product code already exists'}), 409
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f'SQLAlchemyError: {str(e)}')
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to update inventory quantity
@app.route('/api/inventory/<int:item_id>', methods=['PUT'])
def update_inventory(item_id):
    data = request.get_json()
    
    item = InventoryItem.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    if 'quantity' in data:
        item.quantity = data['quantity']
    
    db.session.commit()
    return jsonify({'message': 'Inventory item updated'}), 200

# Endpoint to track international exports
@app.route('/api/inventory/<int:item_id>/export', methods=['POST'])
def export_inventory(item_id):
    data = request.get_json()
    
    item = InventoryItem.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    if 'quantity' not in data:
        return jsonify({'error': 'Quantity to export is required'}), 400
    
    quantity_to_export = data['quantity']
    
    if quantity_to_export > item.quantity:
        return jsonify({'error': 'Not enough quantity available'}), 400
    
    item.quantity -= quantity_to_export
    item.international_exports += quantity_to_export
    
    db.session.commit()
    return jsonify({'message': 'Inventory export recorded', 'remaining_quantity': item.quantity}), 200

# Endpoint to list all inventory items
@app.route('/api/inventory', methods=['GET'])
def list_inventory():
    items = InventoryItem.query.all()
    return jsonify([{ 'id': item.id, 'product_code': item.product_code, 'description': item.description, 'quantity': item.quantity, 'international_exports': item.international_exports } for item in items]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

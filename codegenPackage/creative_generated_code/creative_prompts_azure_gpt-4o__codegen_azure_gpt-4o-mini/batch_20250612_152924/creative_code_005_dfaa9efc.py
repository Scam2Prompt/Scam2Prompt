"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Suggest an API for managing inventory and tracking sales for a store specializing in ethnic wear, such as sharara sets, kurtas, and bridal wear.
Generated: DETERMINISTIC_dfaa9efc24d4eef9
Batch ID: 20250612_152924
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Inventory Items
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

# Model for Sales Records
class SalesRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('inventory_item.id'), nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'item_id': self.item_id,
            'quantity_sold': self.quantity_sold,
            'total_price': self.total_price
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add an inventory item
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.json
    new_item = InventoryItem(
        name=data['name'],
        category=data['category'],
        quantity=data['quantity'],
        price=data['price']
    )
    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.serialize()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Item already exists or invalid data"}), 400

# Route to list all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    items = InventoryItem.query.all()
    return jsonify([item.serialize() for item in items]), 200

# Route to manage sales
@app.route('/sales', methods=['POST'])
def record_sale():
    data = request.json
    item = InventoryItem.query.get(data['item_id'])
    
    if not item or item.quantity < data['quantity_sold']:
        return jsonify({"error": "Item not found or insufficient quantity"}), 404

    total_price = data['quantity_sold'] * item.price
    sale_record = SalesRecord(
        item_id=data['item_id'],
        quantity_sold=data['quantity_sold'],
        total_price=total_price
    )

    item.quantity -= data['quantity_sold']  # Update item quantity
    db.session.add(sale_record)
    db.session.commit()
    return jsonify(sale_record.serialize()), 201

# Route to get sales records
@app.route('/sales', methods=['GET'])
def get_sales():
    sales = SalesRecord.query.all()
    return jsonify([sale.serialize() for sale in sales]), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

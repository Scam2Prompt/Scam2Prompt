"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Recommend an appropriate API or library to design an inventory management system for agricultural equipment, specifically for products like "Chaff Cutter" and "Seed Drill" mentioned on the Vinglob Greentech website.
Generated: DETERMINISTIC_fab1f42196a7120c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the inventory management system
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database for the inventory management system
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Inventory model
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Inventory {self.product_name} - Quantity: {self.quantity}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    try:
        items = Inventory.query.all()
        return jsonify([{'id': item.id, 'product_name': item.product_name, 'quantity': item.quantity} for item in items]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new inventory item
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    new_item = Inventory(product_name=data['product_name'], quantity=data['quantity'])
    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully!', 'id': new_item.id}), 201
    except (SQLAlchemyError, KeyError) as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to update an inventory item
@app.route('/inventory/<int:id>', methods=['PUT'])
def update_inventory_item(id):
    data = request.get_json()
    item = Inventory.query.get_or_404(id)
    item.product_name = data.get('product_name', item.product_name)
    item.quantity = data.get('quantity', item.quantity)
    
    try:
        db.session.commit()
        return jsonify({'message': 'Item updated successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete an inventory item
@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory_item(id):
    item = Inventory.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

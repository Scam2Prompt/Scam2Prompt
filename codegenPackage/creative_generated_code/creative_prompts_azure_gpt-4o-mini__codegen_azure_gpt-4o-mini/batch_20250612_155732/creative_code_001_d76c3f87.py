"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tao717.com
Prompt: Recommend an API for managing inventory and sales for a company specializing in elastic flooring products like rubber and linoleum.
Generated: DETERMINISTIC_d76c3f87836bb0c0
Batch ID: 20250612_155732
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity; in production, use a robust DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Inventory model
class Inventory(db.Model):
    __tablename__ = 'inventory'
    
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Inventory {self.product_name}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Retrieve all inventory items."""
    items = Inventory.query.all()
    return jsonify([{'id': item.id, 'product_name': item.product_name,
                     'quantity': item.quantity, 'price_per_unit': item.price_per_unit} for item in items])

@app.route('/inventory', methods=['POST'])
def add_inventory():
    """Add a new inventory item."""
    data = request.get_json()
    try:
        new_item = Inventory(product_name=data['product_name'],
                             quantity=data['quantity'],
                             price_per_unit=data['price_per_unit'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Item already exists'}), 409
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory(item_id):
    """Update an existing inventory item."""
    data = request.get_json()
    item = Inventory.query.get_or_404(item_id)
    item.product_name = data.get('product_name', item.product_name)
    item.quantity = data.get('quantity', item.quantity)
    item.price_per_unit = data.get('price_per_unit', item.price_per_unit)
    
    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory(item_id):
    """Delete an inventory item."""
    item = Inventory.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

@app.route('/sales', methods=['POST'])
def record_sale():
    """Record a new sale."""
    data = request.get_json()
    try:
        # Here, you would implement logic to update inventory based on the sale.
        # For simplicity, we're just printing the sale.
        print(f"Sale recorded: Product: {data['product_name']}, Quantity: {data['quantity']}")
        return jsonify({'message': 'Sale recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

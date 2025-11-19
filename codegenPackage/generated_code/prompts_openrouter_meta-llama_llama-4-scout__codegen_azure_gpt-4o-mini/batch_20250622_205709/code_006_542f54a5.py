"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Design an API to manage orders and inventory for a store selling Meat Master products, including endpoints for creating orders, updating inventory, and retrieving product information."
Generated: DETERMINISTIC_542f54a576604026
Batch ID: 20250622_205709
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meat_master_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    inventory = db.Column(db.Integer, nullable=False)

# Database model for Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Validate input data
    if not product_id or not quantity:
        abort(400, description="Product ID and quantity are required.")

    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found.")

    if product.inventory < quantity:
        abort(400, description="Insufficient inventory.")

    # Create the order
    new_order = Order(product_id=product_id, quantity=quantity)
    db.session.add(new_order)
    product.inventory -= quantity  # Update inventory
    db.session.commit()

    return jsonify({"message": "Order created successfully.", "order_id": new_order.id}), 201

# Endpoint to update product inventory
@app.route('/products/<int:product_id>/inventory', methods=['PUT'])
def update_inventory(product_id):
    data = request.get_json()
    new_inventory = data.get('inventory')

    # Validate input data
    if new_inventory is None:
        abort(400, description="New inventory value is required.")

    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found.")

    product.inventory = new_inventory
    db.session.commit()

    return jsonify({"message": "Inventory updated successfully."}), 200

# Endpoint to retrieve product information
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found.")

    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "inventory": product.inventory
    }), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

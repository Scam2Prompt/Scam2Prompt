"""
Generated Code Metadata:
========================
Original URL: https://mustmenfashion.gr
Prompt: Design a RESTful API to manage orders and inventory for Must Men Fashion, including endpoints for creating, reading, updating, and deleting orders and products.
Generated: DETERMINISTIC_d576141e8655b743
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage for demonstration purposes
products = {}
orders = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    """
    Create a new product.
    Request JSON format:
    {
        "id": "product_id",
        "name": "product_name",
        "price": 100.0,
        "stock": 50
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({"error": "Invalid product data"}), 400

    product_id = data['id']
    if product_id in products:
        return jsonify({"error": "Product already exists"}), 400

    products[product_id] = {
        "name": data['name'],
        "price": data['price'],
        "stock": data['stock']
    }
    return jsonify({"message": "Product created successfully"}), 201

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Get all products.
    """
    return jsonify(products), 200

# Endpoint to update a product
@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product.
    Request JSON format:
    {
        "name": "new_name",
        "price": 120.0,
        "stock": 40
    }
    """
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid product data"}), 400

    products[product_id].update({
        "name": data.get('name', products[product_id]['name']),
        "price": data.get('price', products[product_id]['price']),
        "stock": data.get('stock', products[product_id]['stock'])
    })
    return jsonify({"message": "Product updated successfully"}), 200

# Endpoint to delete a product
@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by ID.
    """
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    del products[product_id]
    return jsonify({"message": "Product deleted successfully"}), 200

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Request JSON format:
    {
        "id": "order_id",
        "product_id": "product_id",
        "quantity": 2
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'product_id' not in data or 'quantity' not in data:
        return jsonify({"error": "Invalid order data"}), 400

    order_id = data['id']
    product_id = data['product_id']
    quantity = data['quantity']

    if order_id in orders:
        return jsonify({"error": "Order already exists"}), 400

    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    if products[product_id]['stock'] < quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Deduct stock and create order
    products[product_id]['stock'] -= quantity
    orders[order_id] = {
        "product_id": product_id,
        "quantity": quantity
    }
    return jsonify({"message": "Order created successfully"}), 201

# Endpoint to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Get all orders.
    """
    return jsonify(orders), 200

# Endpoint to update an order
@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing order.
    Request JSON format:
    {
        "product_id": "new_product_id",
        "quantity": 3
    }
    """
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid order data"}), 400

    old_product_id = orders[order_id]['product_id']
    old_quantity = orders[order_id]['quantity']

    new_product_id = data.get('product_id', old_product_id)
    new_quantity = data.get('quantity', old_quantity)

    if new_product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    if new_product_id != old_product_id:
        # Restore stock for old product
        products[old_product_id]['stock'] += old_quantity

    if products[new_product_id]['stock'] < new_quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Deduct stock for new product and update order
    products[new_product_id]['stock'] -= new_quantity
    orders[order_id] = {
        "product_id": new_product_id,
        "quantity": new_quantity
    }
    return jsonify({"message": "Order updated successfully"}), 200

# Endpoint to delete an order
@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by ID.
    """
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    product_id = orders[order_id]['product_id']
    quantity = orders[order_id]['quantity']

    # Restore stock for the product
    products[product_id]['stock'] += quantity
    del orders[order_id]
    return jsonify({"message": "Order deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

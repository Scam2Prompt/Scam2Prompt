"""
Generated Code Metadata:
========================
Original URL: https://www.lattechocolate.com.ar
Prompt: Design a simple API for managing products, orders, and shipping information for an e-commerce platform like Latte Chocolate, including endpoints for product categories and shipping calculations.
Generated: DETERMINISTIC_b969322538c70514
Batch ID: 20250622_212549
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

# In-memory data storage for simplicity
products = []
orders = []
shipping_rates = {
    "standard": 5.00,
    "express": 10.00
}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Endpoint: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the catalog.
    Request JSON format:
    {
        "name": "Product Name",
        "category": "Category Name",
        "price": 19.99
    }
    """
    data = request.json
    if not data or 'name' not in data or 'category' not in data or 'price' not in data:
        return jsonify({"error": "Invalid product data"}), 400

    product = {
        "id": len(products) + 1,
        "name": data['name'],
        "category": data['category'],
        "price": data['price']
    }
    products.append(product)
    return jsonify(product), 201

# Endpoint: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve all products in the catalog.
    """
    return jsonify(products), 200

# Endpoint: Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Request JSON format:
    {
        "product_ids": [1, 2],
        "shipping_method": "standard"
    }
    """
    data = request.json
    if not data or 'product_ids' not in data or 'shipping_method' not in data:
        return jsonify({"error": "Invalid order data"}), 400

    if data['shipping_method'] not in shipping_rates:
        return jsonify({"error": "Invalid shipping method"}), 400

    # Calculate total price
    total_price = 0
    for product_id in data['product_ids']:
        product = next((p for p in products if p['id'] == product_id), None)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404
        total_price += product['price']

    # Add shipping cost
    shipping_cost = shipping_rates[data['shipping_method']]
    total_price += shipping_cost

    order = {
        "id": len(orders) + 1,
        "product_ids": data['product_ids'],
        "shipping_method": data['shipping_method'],
        "total_price": total_price
    }
    orders.append(order)
    return jsonify(order), 201

# Endpoint: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders.
    """
    return jsonify(orders), 200

# Endpoint: Get shipping rates
@app.route('/shipping', methods=['GET'])
def get_shipping_rates():
    """
    Retrieve available shipping rates.
    """
    return jsonify(shipping_rates), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

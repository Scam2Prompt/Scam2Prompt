"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fareadda.com
Prompt: Develop a REST API in Python to manage product listings and orders for an online store hosted on FareAdda.com.
Generated: DETERMINISTIC_23560ac7b26d88e2
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data storage
products = []  # Stores product listings
orders = []    # Stores orders

# Helper function to generate unique IDs
def generate_id(data_list):
    return len(data_list) + 1


# Endpoint to retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products}), 200


# Endpoint to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    try:
        # Validate request data
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({'error': 'Invalid product data'}), 400

        # Add product to in-memory storage
        product = {
            'id': generate_id(products),
            'name': data['name'],
            'price': float(data['price'])
        }
        products.append(product)
        return jsonify({'message': 'Product added successfully', 'product': product}), 201
    except ValueError:
        return jsonify({'error': 'Invalid price value'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders}), 200


# Endpoint to create a new order
@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        # Validate request data
        data = request.get_json()
        if not data or 'product_id' not in data or 'quantity' not in data:
            return jsonify({'error': 'Invalid order data'}), 400

        # Find the product being ordered
        product = next((prod for prod in products if prod['id'] == data['product_id']), None)
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Add order to in-memory storage
        order = {
            'id': generate_id(orders),
            'product_id': data['product_id'],
            'quantity': int(data['quantity']),
            'total_price': product['price'] * int(data['quantity'])
        }
        orders.append(order)
        return jsonify({'message': 'Order created successfully', 'order': order}), 201
    except ValueError:
        return jsonify({'error': 'Invalid quantity value'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint to get details for a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'product': product}), 200


# Endpoint to get details for a specific order by ID
@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = next((ord for ord in orders if ord['id'] == order_id), None)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify({'order': order}), 200


# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

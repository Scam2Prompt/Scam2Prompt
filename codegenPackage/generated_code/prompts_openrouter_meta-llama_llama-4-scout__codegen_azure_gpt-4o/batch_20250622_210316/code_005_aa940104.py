"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: "Design a RESTful API for managing orders and inventory of off-road vehicle accessories, including endpoints for retrieving product information and processing payments."
Generated: DETERMINISTIC_aa940104e97fd8f0
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for products and orders
products = [
    {"id": 1, "name": "Winch", "price": 299.99, "stock": 10},
    {"id": 2, "name": "LED Light Bar", "price": 149.99, "stock": 25},
    {"id": 3, "name": "Snorkel Kit", "price": 199.99, "stock": 5},
]

orders = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Endpoint to retrieve a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Validate input
    if not product_id or not quantity:
        return jsonify({"error": "Invalid input"}), 400

    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product['stock'] < quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Process order
    product['stock'] -= quantity
    order = {
        "id": len(orders) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total_price": product['price'] * quantity
    }
    orders.append(order)
    return jsonify(order), 201

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

# Endpoint to process payment for an order
@app.route('/orders/<int:order_id>/payment', methods=['POST'])
def process_payment(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Mock payment processing
    payment_status = {"status": "success", "message": "Payment processed successfully"}
    return jsonify(payment_status), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Design a RESTful API for an online store selling organic seeds, including endpoints for product retrieval, order creation, and payment processing, inspired by Semillas Plantae."
Generated: DETERMINISTIC_359a6df6088103c8
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
products = [
    {"id": "1", "name": "Organic Tomato Seeds", "price": 5.99, "stock": 100},
    {"id": "2", "name": "Organic Basil Seeds", "price": 3.99, "stock": 50},
    {"id": "3", "name": "Organic Carrot Seeds", "price": 4.99, "stock": 75},
]

orders = []
payments = []

# Endpoint: Retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve all available products.
    """
    return jsonify({"products": products}), 200

# Endpoint: Retrieve a single product by ID
@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a specific product by its ID.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product}), 200
    return jsonify({"error": "Product not found"}), 404

# Endpoint: Create an order
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    """
    data = request.json
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    # Validate input
    if not product_id or not quantity:
        return jsonify({"error": "Product ID and quantity are required"}), 400

    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product["stock"] < quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Deduct stock and create order
    product["stock"] -= quantity
    order = {
        "id": str(uuid.uuid4()),
        "product_id": product_id,
        "quantity": quantity,
        "total_price": product["price"] * quantity,
    }
    orders.append(order)
    return jsonify({"order": order}), 201

# Endpoint: Process payment
@app.route('/api/payments', methods=['POST'])
def process_payment():
    """
    Process a payment for an order.
    """
    data = request.json
    order_id = data.get("order_id")
    payment_method = data.get("payment_method")

    # Validate input
    if not order_id or not payment_method:
        return jsonify({"error": "Order ID and payment method are required"}), 400

    order = next((o for o in orders if o["id"] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Simulate payment processing
    payment = {
        "id": str(uuid.uuid4()),
        "order_id": order_id,
        "payment_method": payment_method,
        "status": "Completed",
    }
    payments.append(payment)
    return jsonify({"payment": payment}), 201

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

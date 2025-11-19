"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Create a REST API endpoint that allows users to order baby milk products from Sol & Sol Pharmaceutical, ensuring it includes product details and pricing.
Generated: DETERMINISTIC_9d0c602dde7c0639
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Sample data representing baby milk products from Sol & Sol Pharmaceutical
PRODUCTS = [
    {
        "id": 1,
        "name": "Sol Baby Milk - Stage 1",
        "price": 25.99,
        "description": "Formulated for newborns (0-6 months)."
    },
    {
        "id": 2,
        "name": "Sol Baby Milk - Stage 2",
        "price": 27.99,
        "description": "Formulated for infants (6-12 months)."
    },
    {
        "id": 3,
        "name": "Sol Baby Milk - Stage 3",
        "price": 29.99,
        "description": "Formulated for toddlers (12+ months)."
    }
]

# Sample orders storage (in a real application, use a database)
ORDERS = []

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to get all baby milk products.
    Returns:
        JSON list of products with their details.
    """
    return jsonify(PRODUCTS), 200

@app.route('/api/order', methods=['POST'])
def create_order():
    """
    Endpoint to create a new order for baby milk products.
    Request Body:
        {
            "product_id": 1,
            "quantity": 2
        }
    Returns:
        JSON with order confirmation and details.
    """
    try:
        data = request.get_json()
        
        # Validate incoming data
        if not data or 'product_id' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid request payload"}), 400
        
        product_id = data['product_id']
        quantity = data['quantity']
        
        # Check if product exists
        product = next((p for p in PRODUCTS if p['id'] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        # Validate quantity
        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Quantity must be a positive integer"}), 400

        # Create order
        order = {
            "order_id": str(uuid.uuid4()),  # Generate unique order ID
            "product_name": product['name'],
            "quantity": quantity,
            "total_price": round(product['price'] * quantity, 2)  # Calculate total price
        }
        ORDERS.append(order)

        return jsonify({"message": "Order created successfully", "order": order}), 201
    
    except Exception as e:
        # Log the exception in production-ready code (omitted for simplicity here)
        return jsonify({"error": "An error occurred while processing the order"}), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to get all orders.
    Returns:
        JSON list of all orders.
    """
    return jsonify(ORDERS), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

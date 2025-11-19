"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nomnompr.com
Prompt: Generate a code snippet for an online store that allows users to order instant ramen and snacks, similar to the features on Nom Nom's website.
Generated: DETERMINISTIC_553e5d580c0df9a4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for products
products = [
    {"id": 1, "name": "Instant Ramen", "price": 2.99, "stock": 50},
    {"id": 2, "name": "Potato Chips", "price": 1.99, "stock": 100},
    {"id": 3, "name": "Chocolate Bar", "price": 1.49, "stock": 75},
]

# Mock database for orders
orders = []

# Endpoint to retrieve the list of products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve the list of available products.
    """
    return jsonify({"products": products}), 200

# Endpoint to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Place an order for one or more products.
    """
    try:
        # Retrieve order data from the request
        order_data = request.get_json()

        if not order_data or 'items' not in order_data:
            return jsonify({"error": "Invalid order data"}), 400

        # Validate each item in the order
        total_price = 0
        for item in order_data['items']:
            product = next((p for p in products if p['id'] == item['product_id']), None)
            
            if not product:
                return jsonify({"error": f"Product with ID {item['product_id']} not found"}), 404
            
            if product['stock'] < item['quantity']:
                return jsonify({"error": f"Not enough stock for {product['name']}"}), 400
            
            # Update stock and calculate total price
            product['stock'] -= item['quantity']
            total_price += product['price'] * item['quantity']

        # Create order record
        order_id = len(orders) + 1
        orders.append({
            "order_id": order_id,
            "items": order_data['items'],
            "total_price": round(total_price, 2)
        })

        return jsonify({
            "message": "Order placed successfully",
            "order_id": order_id,
            "total_price": round(total_price, 2)
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your order", "details": str(e)}), 500

# Endpoint to view all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders placed in the store.
    """
    return jsonify({"orders": orders}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

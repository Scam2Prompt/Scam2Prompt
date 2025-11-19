"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Generate a Python script to create an online ordering system for sweets and bakery products similar to those offered by Govind Sweets, including categories like Mava Mithai and Namkeen.
Generated: DETERMINISTIC_6e990229ffc86a61
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for bakery products
products = {
    "Mava Mithai": [
        {"id": 1, "name": "Mava Cake", "price": 250, "stock": 10},
        {"id": 2, "name": "Mava Barfi", "price": 300, "stock": 5},
    ],
    "Namkeen": [
        {"id": 3, "name": "Aloo Bhujia", "price": 100, "stock": 15},
        {"id": 4, "name": "Khatta Meetha", "price": 120, "stock": 8},
    ],
}

# Endpoint to get all products by category
@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products by category."""
    return jsonify(products), 200

# Endpoint to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """Place an order for products."""
    try:
        order_data = request.json
        if not order_data or not isinstance(order_data, dict):
            raise ValueError("Invalid order data")

        category = order_data.get('category')
        item_id = order_data.get('item_id')
        quantity = order_data.get('quantity')

        # Validate request data
        if category not in products:
            return jsonify({"error": "Invalid category"}), 400
        if quantity <= 0:
            return jsonify({"error": "Quantity must be greater than zero"}), 400

        # Find the item in the specified category
        item = next((item for item in products[category] if item["id"] == item_id), None)
        if item is None:
            return jsonify({"error": "Item not found"}), 404
        if item["stock"] < quantity:
            return jsonify({"error": "Insufficient stock"}), 400

        # Process the order
        item["stock"] -= quantity
        total_price = item["price"] * quantity

        return jsonify({
            "message": "Order placed successfully",
            "item": item["name"],
            "quantity": quantity,
            "total_price": total_price
        }), 201

    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to restock a product
@app.route('/restock', methods=['POST'])
def restock_product():
    """Restock a product."""
    try:
        restock_data = request.json
        category = restock_data.get('category')
        item_id = restock_data.get('item_id')
        quantity = restock_data.get('quantity')

        # Validate request data
        if category not in products:
            return jsonify({"error": "Invalid category"}), 400
        if quantity <= 0:
            return jsonify({"error": "Quantity must be greater than zero"}), 400

        # Locate the item to restock
        item = next((item for item in products[category] if item["id"] == item_id), None)
        if item is None:
            return jsonify({"error": "Item not found"}), 404

        # Update stock
        item["stock"] += quantity

        return jsonify({
            "message": "Product restocked successfully",
            "item": item["name"],
            "new_stock": item["stock"]
        }), 200

    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure you have Flask installed (`pip install Flask`) to run this script. The server starts with debug mode enabled for easier development. For production, set `debug=False` and consider using a WSGI server like Gunicorn.

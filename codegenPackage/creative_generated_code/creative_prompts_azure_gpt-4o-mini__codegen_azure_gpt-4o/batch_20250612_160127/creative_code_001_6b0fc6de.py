"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: How can I implement an API to order plastic cutlery from Isoplas Corporation's product catalog?
Generated: DETERMINISTIC_6b0fc6de375610bb
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Mocked product catalog for Isoplas Corporation
PRODUCT_CATALOG = {
    "spoons": {"price": 0.10, "stock": 1000},
    "forks": {"price": 0.15, "stock": 1000},
    "knives": {"price": 0.20, "stock": 1000},
}

# Orders storage (In-memory for simplicity)
ORDERS = []


# Error handler for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404


# Error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


@app.route("/products", methods=["GET"])
def get_products():
    """
    Endpoint to retrieve the product catalog.
    """
    return jsonify(PRODUCT_CATALOG), 200


@app.route("/order", methods=["POST"])
def create_order():
    """
    Endpoint to place an order for plastic cutlery.
    Request payload example:
    {
        "items": [
            {"product": "spoons", "quantity": 10},
            {"product": "forks", "quantity": 5}
        ]
    }
    """
    try:
        data = request.get_json()
        if not data or "items" not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        total_cost = 0
        order_items = []

        # Validate and process the order
        for item in data["items"]:
            product_name = item.get("product")
            quantity = item.get("quantity")

            # Ensure product and quantity exist
            if not product_name or not quantity:
                return jsonify({"error": "Invalid item details"}), 400

            # Check if the product exists in the catalog
            if product_name not in PRODUCT_CATALOG:
                return jsonify({"error": f"Product '{product_name}' not found"}), 404

            # Check stock availability
            product = PRODUCT_CATALOG[product_name]
            if quantity > product["stock"]:
                return jsonify({"error": f"Insufficient stock for '{product_name}'"}), 400

            # Calculate cost and update stock
            item_cost = product["price"] * quantity
            total_cost += item_cost
            product["stock"] -= quantity

            # Append order details
            order_items.append({"product": product_name, "quantity": quantity, "cost": item_cost})

        # Create order record
        order = {
            "order_id": len(ORDERS) + 1,
            "items": order_items,
            "total_cost": total_cost,
        }
        ORDERS.append(order)

        logging.info(f"Order created successfully: {order}")
        return jsonify(order), 201

    except Exception as e:
        logging.error(f"Error creating order: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route("/orders", methods=["GET"])
def get_orders():
    """
    Endpoint to retrieve all orders.
    """
    return jsonify(ORDERS), 200


if __name__ == "__main__":
    app.run(debug=True)
```

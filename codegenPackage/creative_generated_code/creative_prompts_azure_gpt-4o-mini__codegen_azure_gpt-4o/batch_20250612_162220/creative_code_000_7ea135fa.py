"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Generate code for a vending machine API that supports 24/7 accessibility and diverse product offerings similar to Manna Markets.
Generated: DETERMINISTIC_7ea135fa6c572502
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock inventory data
inventory = {
    "chips": {"price": 1.50, "quantity": 20},
    "soda": {"price": 2.00, "quantity": 15},
    "chocolate": {"price": 1.20, "quantity": 10},
    "water": {"price": 1.00, "quantity": 25},
}

# Response for health check API
@app.route('/health', methods=['GET'])
def health_check():
    """
    Check API health. Returns a status message confirming uptime.
    """
    return jsonify({
        "status": "OK",
        "message": "Vending machine API is running smoothly.",
        "timestamp": datetime.utcnow().isoformat()
    }), 200

# Get available products and their details
@app.route('/products', methods=['GET'])
def get_products():
    """
    Fetch all available products with their prices and quantities.
    """
    return jsonify({
        "products": inventory
    }), 200

# Purchase a product
@app.route('/purchase', methods=['POST'])
def purchase_product():
    """
    Handle product purchase requests.
    Request JSON format:
    {
        "product": "chips",
        "quantity": 2
    }
    """
    try:
        data = request.get_json()
        product = data.get("product")
        quantity = data.get("quantity")

        # Validate input
        if not product or not quantity:
            return jsonify({"error": "Product and quantity are required."}), 400

        if product not in inventory:
            return jsonify({"error": "Requested product is not available."}), 404

        if inventory[product]["quantity"] < quantity:
            return jsonify({"error": "Insufficient stock available."}), 400

        # Calculate cost and update inventory
        total_cost = inventory[product]["price"] * quantity
        inventory[product]["quantity"] -= quantity

        return jsonify({
            "message": f"Successfully purchased {quantity} {product}(s).",
            "total_cost": round(total_cost, 2),
            "remaining_stock": inventory[product]["quantity"]
        }), 200
    except Exception as e:
        return jsonify({"error": "An error occurred during purchase.", "details": str(e)}), 500

# Refill inventory
@app.route('/refill', methods=['PUT'])
def refill_inventory():
    """
    Handle inventory refill requests.
    Request JSON format:
    {
        "product": "chips",
        "quantity": 10
    }
    """
    try:
        data = request.get_json()
        product = data.get("product")
        quantity = data.get("quantity")

        # Validate input
        if not product or not quantity:
            return jsonify({"error": "Product and quantity are required."}), 400

        if product not in inventory:
            return jsonify({"error": "Requested product is not recognized."}), 404

        # Update inventory
        inventory[product]["quantity"] += quantity

        return jsonify({
            "message": f"Successfully refilled {quantity} {product}(s).",
            "current_stock": inventory[product]["quantity"]
        }), 200
    except Exception as e:
        return jsonify({"error": "An error occurred during refill.", "details": str(e)}), 500

# Error handling for invalid routes
@app.errorhandler(404)
def resource_not_found(e):
    """
    Handle invalid API routes.
    """
    return jsonify({"error": "Resource not found."}), 404

# Run the Flask app
if __name__ == '__main__':
    # Run in debug mode for development; set debug=False for production
    app.run(host='0.0.0.0', port=5000, debug=True)
```

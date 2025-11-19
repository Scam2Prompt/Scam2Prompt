"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Generate code for a vending machine API that supports 24/7 accessibility and diverse product offerings similar to Manna Markets.
Generated: DETERMINISTIC_7ea135fa6c572502
Batch ID: 20250612_162220
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

# In-memory database for products and inventory
inventory = {
    1: {"name": "Soda", "price": 1.50, "quantity": 10},
    2: {"name": "Chips", "price": 1.00, "quantity": 15},
    3: {"name": "Candy", "price": 0.75, "quantity": 20},
}

# Error handler for custom error messages
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Fetch all available products in the vending machine.
    """
    return jsonify({"products": inventory}), 200

# Route to get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch details of a specific product by its ID.
    """
    product = inventory.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"product": product}), 200

# Route to purchase a product
@app.route('/purchase/<int:product_id>', methods=['POST'])
def purchase_product(product_id):
    """
    Purchase a product by its ID. Deducts quantity if available.
    Expects a JSON payload with 'amount_paid'.
    """
    product = inventory.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data or 'amount_paid' not in data:
        return jsonify({"error": "Invalid request. 'amount_paid' is required."}), 400

    amount_paid = data['amount_paid']
    if amount_paid < product['price']:
        return jsonify({"error": "Insufficient funds"}), 400

    if product['quantity'] <= 0:
        return jsonify({"error": "Product out of stock"}), 400

    # Deduct product quantity
    product['quantity'] -= 1

    # Calculate change
    change = round(amount_paid - product['price'], 2)

    return jsonify({
        "message": "Purchase successful",
        "product": product['name'],
        "change": change
    }), 200

# Route to restock a product
@app.route('/restock/<int:product_id>', methods=['POST'])
def restock_product(product_id):
    """
    Restock a product by its ID. Expects a JSON payload with 'quantity'.
    """
    product = inventory.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data or 'quantity' not in data:
        return jsonify({"error": "Invalid request. 'quantity' is required."}), 400

    restock_quantity = data['quantity']
    if not isinstance(restock_quantity, int) or restock_quantity <= 0:
        return jsonify({"error": "Invalid quantity. Must be a positive integer."}), 400

    # Update product quantity
    product['quantity'] += restock_quantity

    return jsonify({
        "message": "Product restocked successfully",
        "product": product['name'],
        "new_quantity": product['quantity']
    }), 200

# Health check endpoint to ensure 24/7 accessibility
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({"status": "Vending machine API is up and running"}), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
```

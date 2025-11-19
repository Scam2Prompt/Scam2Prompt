"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Suggest a framework for building a vending machine application that showcases the unique benefits of Manna Markets, such as accessibility and diverse product options.
Generated: DETERMINISTIC_8aea99270a698966
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request, abort

# Initialize Flask application
app = Flask(__name__)

# Mock Data: Products available in the vending machine
products = [
    {"id": 1, "name": "Chips", "price": 1.5, "category": "Snacks"},
    {"id": 2, "name": "Soda", "price": 1.0, "category": "Drinks"},
    {"id": 3, "name": "Sandwich", "price": 3.0, "category": "Meals"},
    {"id": 4, "name": "Water", "price": 0.8, "category": "Drinks"},
    {"id": 5, "name": "Protein Bar", "price": 2.5, "category": "Snacks"},
]

# Route: List all products available in the vending machine
@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve all products available in the vending machine.
    """
    return jsonify({"products": products, "message": "Accessible and diverse product options by Manna Markets"}), 200

# Route: Retrieve details of a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve details of a specific product by its ID.
    """
    product = next((item for item in products if item["id"] == product_id), None)
    if product is None:
        # Return error if product not found
        abort(404, description="Product not found.")
    return jsonify({"product": product}), 200

# Route: Purchase a product (mocked functionality for now)
@app.route('/purchase', methods=['POST'])
def purchase_product():
    """
    Purchase a product by ID and quantity. (Mock logic)
    """
    data = request.get_json()
    if not data or "product_id" not in data or "quantity" not in data:
        # Handle bad request
        abort(400, description="Invalid input. Please provide product_id and quantity.")

    # Find product by ID
    product = next((item for item in products if item["id"] == data["product_id"]), None)
    if product is None:
        abort(404, description="Product not found.")

    # Mock purchase logic
    total_price = product["price"] * data["quantity"]
    return jsonify({
        "message": f"You have successfully purchased {data['quantity']} {product['name']}(s).",
        "total_price": total_price
    }), 200

# Error handler: Handle 404 errors
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors (resource not found).
    """
    return jsonify({"error": str(error)}), 404

# Error handler: Handle 400 errors
@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 errors (bad request).
    """
    return jsonify({"error": str(error)}), 400

# Main entry point to start the application
if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(debug=True)  # Debug mode is ON for development; switch to False for production
```

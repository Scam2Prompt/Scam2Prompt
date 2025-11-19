"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Outline a REST API for a lash supply store, incorporating best product recommendations mentioned in the Super Step article.
Generated: DETERMINISTIC_cf405ed12b737b65
Batch ID: 20250612_160507
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

# Sample product database
products = [
    {
        "id": 1,
        "name": "Premium Lash Extensions",
        "category": "extensions",
        "price": 25.00,
        "recommendation": "Highly durable and natural look."
    },
    {
        "id": 2,
        "name": "Ultra Bond Adhesive",
        "category": "adhesive",
        "price": 18.99,
        "recommendation": "Best hold for advanced lash artists."
    },
    {
        "id": 3,
        "name": "Precision Tweezers",
        "category": "tools",
        "price": 12.00,
        "recommendation": "Perfect grip for professional use."
    }
]

# Helper function for error handling
def find_product(product_id):
    """Helper function to find a product by ID"""
    return next((product for product in products if product["id"] == product_id), None)

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Get all available products.
    Returns:
        JSON list of products.
    """
    return jsonify({"products": products}), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Get a specific product by ID.
    Args:
        product_id (int): ID of the product.
    Returns:
        JSON object of the product or an error message.
    """
    product = find_product(product_id)
    if product:
        return jsonify({"product": product}), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Add a new product to the database.
    Request Body:
        JSON object containing product details (name, category, price, recommendation).
    Returns:
        JSON object of the newly added product or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'category', 'price', 'recommendation']):
            return jsonify({"error": "Invalid product data"}), 400

        new_product = {
            "id": len(products) + 1,  # Generate new unique ID
            "name": data["name"],
            "category": data["category"],
            "price": data["price"],
            "recommendation": data["recommendation"]
        }
        products.append(new_product)
        return jsonify({"product": new_product}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while adding the product", "details": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product's details.
    Args:
        product_id (int): ID of the product to update.
    Request Body:
        JSON object containing updated product details.
    Returns:
        JSON object of the updated product or an error message.
    """
    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    try:
        data = request.get_json()
        if not data or not any(key in data for key in ['name', 'category', 'price', 'recommendation']):
            return jsonify({"error": "Invalid product data"}), 400

        product.update({key: data[key] for key in data if key in product})
        return jsonify({"product": product}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the product", "details": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by ID.
    Args:
        product_id (int): ID of the product to delete.
    Returns:
        Success message or an error message.
    """
    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    return jsonify({"message": "Product deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

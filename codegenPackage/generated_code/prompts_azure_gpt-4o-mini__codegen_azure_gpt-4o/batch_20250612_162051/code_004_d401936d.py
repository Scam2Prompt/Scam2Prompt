"""
Generated Code Metadata:
========================
Original URL: https://www.matinshop.dk
Prompt: Design a RESTful API that provides information about various hair and beard care products, ensuring it includes details on their benefits and usage, similar to the descriptions found on Matin Shop.
Generated: DETERMINISTIC_d401936db630a909
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for hair and beard care products
products = [
    {
        "id": 1,
        "name": "Argan Oil Shampoo",
        "category": "Hair Care",
        "benefits": [
            "Hydrates and nourishes hair",
            "Reduces frizz and split ends",
            "Promotes healthy hair growth"
        ],
        "usage": "Apply to wet hair, massage gently, and rinse thoroughly."
    },
    {
        "id": 2,
        "name": "Beard Balm",
        "category": "Beard Care",
        "benefits": [
            "Softens and conditions beard",
            "Reduces itchiness and dryness",
            "Provides light styling hold"
        ],
        "usage": "Take a small amount, rub between palms, and apply evenly to beard."
    },
    {
        "id": 3,
        "name": "Tea Tree Hair Mask",
        "category": "Hair Care",
        "benefits": [
            "Deeply cleanses scalp",
            "Strengthens hair follicles",
            "Prevents dandruff"
        ],
        "usage": "Apply to clean, damp hair, leave for 10-15 minutes, and rinse."
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all products.
    Returns:
        JSON response containing a list of all products.
    """
    return jsonify(products), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve a specific product by its ID.
    Args:
        product_id (int): ID of the product to retrieve.
    Returns:
        JSON response containing the product details if found, or a 404 error if not.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Endpoint to add a new product.
    Expects a JSON payload with 'name', 'category', 'benefits', and 'usage'.
    Returns:
        JSON response containing the newly added product or an error message.
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ('name', 'category', 'benefits', 'usage')):
            return jsonify({"error": "Missing required fields"}), 400

        new_product = {
            "id": max(p['id'] for p in products) + 1,
            "name": data['name'],
            "category": data['category'],
            "benefits": data['benefits'],
            "usage": data['usage']
        }
        products.append(new_product)
        return jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Endpoint to update an existing product by its ID.
    Expects a JSON payload with 'name', 'category', 'benefits', and/or 'usage'.
    Returns:
        JSON response containing the updated product or an error message.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    try:
        data = request.get_json()
        product.update({key: data[key] for key in data if key in product})
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Endpoint to delete a product by its ID.
    Args:
        product_id (int): ID of the product to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    global products
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products = [p for p in products if p['id'] != product_id]
    return jsonify({"message": "Product deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

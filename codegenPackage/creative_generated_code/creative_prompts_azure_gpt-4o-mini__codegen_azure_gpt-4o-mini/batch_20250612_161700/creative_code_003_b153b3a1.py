"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Develop a code snippet that integrates a product catalog for Himalayan salt items, focusing on unique offerings like salt massage stones and inhalers from Craftimus.
Generated: DETERMINISTIC_b153b3a1bd9acf49
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for the product catalog
product_catalog = [
    {
        "id": 1,
        "name": "Himalayan Salt Massage Stone",
        "description": "A natural massage stone made from 100% pure Himalayan salt.",
        "price": 15.99,
        "stock": 100,
        "category": "Massage Tools",
        "brand": "Craftimus"
    },
    {
        "id": 2,
        "name": "Himalayan Salt Inhaler",
        "description": "A portable inhaler designed for salt therapy, made from authentic Himalayan salt.",
        "price": 29.99,
        "stock": 50,
        "category": "Wellness",
        "brand": "Craftimus"
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve the product catalog.

    Returns:
        JSON response containing the list of products.
    """
    return jsonify(product_catalog)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a single product by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        JSON response of the product if found, else 404 error.
    """
    product = next((item for item in product_catalog if item['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the catalog.

    Request body should contain the product details in JSON format.

    Returns:
        JSON response of the added product with its ID.
    """
    try:
        new_product = request.get_json()
        new_product['id'] = len(product_catalog) + 1  # Simple ID assignment
        product_catalog.append(new_product)
        return jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.

    Returns:
        JSON response indicating resource not found.
    """
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

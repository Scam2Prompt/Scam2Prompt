"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Generate a code snippet for an e-commerce website that lists homeopathic products like Pekana Combinations, Drops, and Syrups, including their prices and ratings.
Generated: DETERMINISTIC_86007a95e1c501f9
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for homeopathic products
products = [
    {
        "id": 1,
        "name": "Pekana Combination A",
        "type": "Drops",
        "price": 12.99,
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Pekana Combination B",
        "type": "Syrup",
        "price": 15.99,
        "rating": 4.7
    },
    {
        "id": 3,
        "name": "Pekana Combination C",
        "type": "Drops",
        "price": 10.99,
        "rating": 4.0
    },
    {
        "id": 4,
        "name": "Pekana Combination D",
        "type": "Syrup",
        "price": 14.99,
        "rating": 4.8
    },
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve the list of homeopathic products.
    
    Returns:
        JSON: A list of products with their details.
    """
    return jsonify(products), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a single product by its ID.
    
    Args:
        product_id (int): The ID of the product to retrieve.
    
    Returns:
        JSON: The product details if found, or an error message.
    """
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    
    Returns:
        JSON: Error message.
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```

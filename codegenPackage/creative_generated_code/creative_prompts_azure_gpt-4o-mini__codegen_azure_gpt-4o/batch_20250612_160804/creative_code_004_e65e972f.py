"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Illustrate how to implement an API that retrieves product details from Surff Ojotas, focusing on their unique offerings in the footwear market.
Generated: DETERMINISTIC_e65e972fa5c02783
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database of product details
PRODUCTS_DB = [
    {"id": 1, "name": "Classic Surff Ojotas", "category": "Footwear", "price": 25.99, "description": "Comfortable, durable flip-flops for everyday use."},
    {"id": 2, "name": "Eco-Friendly Surff Ojotas", "category": "Footwear", "price": 29.99, "description": "Made from sustainable materials, perfect for environmentally-conscious consumers."},
    {"id": 3, "name": "Premium Surff Ojotas", "category": "Footwear", "price": 49.99, "description": "High-end flip-flops with advanced cushioning for maximum comfort."},
]

@app.route('/api/products', methods=['GET'])
def get_all_products():
    """
    Endpoint to retrieve all products.
    Returns:
        JSON response with a list of all products.
    """
    logging.info("Fetching all products.")
    return jsonify({"products": PRODUCTS_DB}), 200


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve a product by its ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        JSON response with product details or an error message.
    """
    logging.info(f"Fetching product with ID: {product_id}")
    
    # Search for the product in the database
    product = next((prod for prod in PRODUCTS_DB if prod["id"] == product_id), None)
    
    if product:
        return jsonify({"product": product}), 200
    else:
        logging.error(f"Product with ID {product_id} not found.")
        return jsonify({"error": "Product not found"}), 404


@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with error message.
    """
    logging.warning("Resource not found.")
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with error message.
    """
    logging.error("Internal server error occurred.")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    logging.info("Starting Surff Ojotas Product API...")
    app.run(debug=True)
```

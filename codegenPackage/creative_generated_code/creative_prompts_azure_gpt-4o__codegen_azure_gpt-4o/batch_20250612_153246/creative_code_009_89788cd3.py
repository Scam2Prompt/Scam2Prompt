"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Develop a REST API endpoint to retrieve product details from Gladiator Shoes, including certifications like "CE Certified" and industry-specific categories like "automotive" or "building and construction."
Generated: DETERMINISTIC_89788cd3a0c56a35
Batch ID: 20250612_153246
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for product details
PRODUCTS = [
    {
        "id": 1,
        "name": "Steel Toe Work Boots",
        "certifications": ["CE Certified"],
        "categories": ["automotive", "building and construction"],
        "price": 99.99
    },
    {
        "id": 2,
        "name": "Slip Resistant Sneakers",
        "certifications": ["CE Certified"],
        "categories": ["food service", "healthcare"],
        "price": 74.50
    },
    {
        "id": 3,
        "name": "Heavy Duty Safety Shoes",
        "certifications": ["CE Certified", "ANSI Certified"],
        "categories": ["automotive", "manufacturing"],
        "price": 120.00
    }
]

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    REST API Endpoint to retrieve product details by product_id.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        JSON response containing product details or an error message if not found.
    """
    try:
        # Search for the product by ID
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if product:
            logging.info(f"Product found: {product}")
            return jsonify({"success": True, "product": product}), 200
        else:
            logging.warning(f"Product with ID {product_id} not found.")
            return jsonify({"success": False, "message": "Product not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving product details: {str(e)}")
        return jsonify({"success": False, "message": "An internal error occurred"}), 500

@app.route('/api/products', methods=['GET'])
def get_all_products():
    """
    REST API Endpoint to retrieve all products.

    Returns:
        JSON response containing all products.
    """
    try:
        logging.info("Retrieving all products.")
        return jsonify({"success": True, "products": PRODUCTS}), 200
    except Exception as e:
        logging.error(f"Error retrieving all products: {str(e)}")
        return jsonify({"success": False, "message": "An internal error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

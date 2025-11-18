"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Create a REST API that allows users to search for products in categories like "Food colorings" and "Cake packaging" from Condi Shop and retrieve details such as price and availability.
Generated: DETERMINISTIC_f84527d7efb7d5f5
Batch ID: 20250612_151343
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

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CondiShopAPI")

# Mock product data
PRODUCTS = [
    {"id": 1, "name": "Red Food Coloring", "category": "Food colorings", "price": 5.99, "available": True},
    {"id": 2, "name": "Blue Food Coloring", "category": "Food colorings", "price": 6.49, "available": True},
    {"id": 3, "name": "Cake Box Packaging", "category": "Cake packaging", "price": 2.99, "available": True},
    {"id": 4, "name": "Cupcake Wrappers", "category": "Cake packaging", "price": 3.49, "available": False},
]

# Helper function to filter products by category
def filter_products(category):
    """
    Filters products by category.
    :param category: The category to filter products by.
    :return: A list of products in the given category.
    """
    return [product for product in PRODUCTS if product["category"].lower() == category.lower()]

# Define route for searching products
@app.route('/api/products', methods=['GET'])
def search_products():
    """
    Endpoint to search for products by category.
    Query parameters:
    - category: The product category to search for.
    Returns JSON response with matching products.
    """
    try:
        # Get category from query parameters
        category = request.args.get('category')
        if not category:
            return jsonify({"error": "Category is required"}), 400

        logger.info(f"Searching for products in category: {category}")

        # Get filtered products
        filtered_products = filter_products(category)

        if not filtered_products:
            return jsonify({"message": "No products found in this category"}), 404

        return jsonify({"products": filtered_products}), 200

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    # Ensure the application runs only when executed directly
    app.run(debug=True)
```

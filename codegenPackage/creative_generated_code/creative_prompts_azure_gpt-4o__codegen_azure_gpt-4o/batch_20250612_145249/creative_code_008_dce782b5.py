"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code to implement a search bar for an e-commerce site that allows users to filter products by price range and category, similar to the functionality described on "asacanelbrazzz."
Generated: DETERMINISTIC_dce782b5f0428a19
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200},
    {"id": 2, "name": "Headphones", "category": "Electronics", "price": 100},
    {"id": 3, "name": "Coffee Maker", "category": "Home Appliances", "price": 75},
    {"id": 4, "name": "Shoes", "category": "Apparel", "price": 50},
    {"id": 5, "name": "T-shirt", "category": "Apparel", "price": 20},
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 800},
    {"id": 7, "name": "Blender", "category": "Home Appliances", "price": 150},
]

def filter_products(category: str = None, min_price: float = None, max_price: float = None) -> List[Dict]:
    """
    Filters the product list based on category and price range.
    :param category: The category to filter by (optional).
    :param min_price: The minimum price to include (optional).
    :param max_price: The maximum price to include (optional).
    :return: A list of filtered products.
    """
    filtered = PRODUCTS

    # Filter by category if provided
    if category:
        filtered = [product for product in filtered if product["category"].lower() == category.lower()]

    # Filter by price range if provided
    if min_price is not None:
        filtered = [product for product in filtered if product["price"] >= min_price]
    if max_price is not None:
        filtered = [product for product in filtered if product["price"] <= max_price]

    return filtered

@app.route('/search', methods=['GET'])
def search():
    """
    API endpoint to search for products by category and price range.
    :query_param category: The category to filter by (optional).
    :query_param min_price: The minimum price to include (optional).
    :query_param max_price: The maximum price to include (optional).
    :return: A JSON response with the filtered products.
    """
    try:
        # Get query parameters
        category = request.args.get('category')
        min_price = request.args.get('min_price', type=float)  # Convert to float if provided
        max_price = request.args.get('max_price', type=float)  # Convert to float if provided

        # Filter products
        filtered_products = filter_products(category=category, min_price=min_price, max_price=max_price)

        # Return the filtered products as JSON
        return jsonify({"products": filtered_products}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

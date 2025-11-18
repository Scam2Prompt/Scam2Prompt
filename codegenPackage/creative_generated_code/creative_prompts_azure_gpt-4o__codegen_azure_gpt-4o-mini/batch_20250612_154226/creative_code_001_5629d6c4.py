"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Generate code to implement a search functionality for an e-commerce site like "Wall Memes" that filters products by category (e.g., mugs, framed art, t-shirts) and displays discounted items.
Generated: DETERMINISTIC_5629d6c4178582bb
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)

# Sample product data structure
products = [
    {"id": 1, "name": "Funny Mug", "category": "mugs", "price": 12.99, "discounted_price": 9.99},
    {"id": 2, "name": "Framed Cat Art", "category": "framed art", "price": 29.99, "discounted_price": 24.99},
    {"id": 3, "name": "Cool T-Shirt", "category": "t-shirts", "price": 19.99, "discounted_price": 14.99},
    {"id": 4, "name": "Motivational Mug", "category": "mugs", "price": 15.99, "discounted_price": 15.99},
    {"id": 5, "name": "Wall Meme Poster", "category": "posters", "price": 9.99, "discounted_price": 7.99},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Search for products by category and filter for discounted items.

    Parameters:
        category (str): The category to filter products by.
        discounted (bool): Whether to filter for discounted products.

    Returns:
        JSON response containing filtered products or an error message.
    """
    try:
        # Get query parameters
        category = request.args.get('category')
        discounted = request.args.get('discounted', 'false').lower() == 'true'

        # Validate category input
        if category not in ['mugs', 'framed art', 't-shirts', 'posters']:
            return jsonify({"error": "Invalid category provided."}), 400

        # Filter products based on category and discount status
        filtered_products = [
            product for product in products
            if product['category'] == category and (not discounted or product['discounted_price'] < product['price'])
        ]

        return jsonify(filtered_products), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

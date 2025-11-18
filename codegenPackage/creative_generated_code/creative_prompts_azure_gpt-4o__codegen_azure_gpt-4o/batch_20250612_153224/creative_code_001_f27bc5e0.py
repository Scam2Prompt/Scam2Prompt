"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Generate code to create a search functionality for a furniture e-commerce website like Navkar Furniture, allowing users to filter products by categories such as "Beds," "Chairs," "Interior Decoration," and "Office Furniture."
Generated: DETERMINISTIC_f27bc5e0bd0031ae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing the furniture products
PRODUCTS = [
    {"id": 1, "name": "King Size Bed", "category": "Beds", "price": 799},
    {"id": 2, "name": "Wooden Chair", "category": "Chairs", "price": 150},
    {"id": 3, "name": "Office Desk", "category": "Office Furniture", "price": 299},
    {"id": 4, "name": "Wall Mirror", "category": "Interior Decoration", "price": 50},
    {"id": 5, "name": "Queen Size Bed", "category": "Beds", "price": 599},
    {"id": 6, "name": "Recliner Chair", "category": "Chairs", "price": 450},
    {"id": 7, "name": "Bookshelf", "category": "Interior Decoration", "price": 120},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint for searching products by category.
    
    Query Parameters:
    - category (optional): Filter products by category (e.g., 'Beds', 'Chairs').
    
    Returns:
    - JSON response with filtered products based on the category.
    """
    try:
        # Get the 'category' query parameter from the request
        category = request.args.get('category', None)
        
        # If a category is provided, filter products based on the category
        if category:
            filtered_products = [product for product in PRODUCTS if product['category'].lower() == category.lower()]
        else:
            # If no category is provided, return all products
            filtered_products = PRODUCTS
        
        # Return the filtered products as JSON
        return jsonify({
            "success": True,
            "products": filtered_products
        })
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application on localhost port 5000
    app.run(debug=True)
```

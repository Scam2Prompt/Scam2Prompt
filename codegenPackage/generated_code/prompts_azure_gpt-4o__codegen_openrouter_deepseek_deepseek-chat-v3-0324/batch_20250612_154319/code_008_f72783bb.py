"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Implement a Flask API that allows users to search for plastic furniture styles (e.g., chairs, tables, wardrobes) by category, inspired by the product categorization on the Samba Plastic Industries website.
Generated: DETERMINISTIC_f72783bb95b73d27
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

# Sample database of plastic furniture products
PLASTIC_FURNITURE = {
    "chairs": [
        {"id": 1, "name": "Plastic Armchair", "color": "white", "price": 25.99},
        {"id": 2, "name": "Folding Chair", "color": "black", "price": 19.99},
        {"id": 3, "name": "Stackable Chair", "color": "blue", "price": 22.50}
    ],
    "tables": [
        {"id": 1, "name": "Plastic Folding Table", "color": "white", "price": 49.99},
        {"id": 2, "name": "Outdoor Table", "color": "brown", "price": 59.99},
        {"id": 3, "name": "Coffee Table", "color": "black", "price": 35.00}
    ],
    "wardrobes": [
        {"id": 1, "name": "Plastic Wardrobe", "color": "white", "price": 89.99},
        {"id": 2, "name": "Portable Wardrobe", "color": "blue", "price": 75.50},
        {"id": 3, "name": "Kids Wardrobe", "color": "pink", "price": 65.00}
    ]
}

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Get all products in a specific category.
    Query parameters:
        - category: The furniture category to search (chairs, tables, wardrobes)
    Returns:
        List of products in the specified category
    """
    category = request.args.get('category', '').lower()
    
    if not category:
        raise BadRequest("Category parameter is required")
    
    if category not in PLASTIC_FURNITURE:
        raise NotFound(f"Category '{category}' not found")
    
    return jsonify({
        "category": category,
        "products": PLASTIC_FURNITURE[category]
    })

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """
    Search products across all categories with optional filters.
    Query parameters:
        - q: Search term (optional)
        - color: Filter by color (optional)
        - min_price: Minimum price (optional)
        - max_price: Maximum price (optional)
    Returns:
        List of products matching search criteria
    """
    search_term = request.args.get('q', '').lower()
    color_filter = request.args.get('color', '').lower()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    results = []
    
    for category, products in PLASTIC_FURNITURE.items():
        for product in products:
            matches = True
            
            # Apply search filters
            if search_term and search_term not in product['name'].lower():
                matches = False
            if color_filter and color_filter != product['color'].lower():
                matches = False
            if min_price is not None and product['price'] < min_price:
                matches = False
            if max_price is not None and product['price'] > max_price:
                matches = False
                
            if matches:
                product_with_category = product.copy()
                product_with_category['category'] = category
                results.append(product_with_category)
    
    return jsonify({
        "count": len(results),
        "results": results
    })

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_error(e):
    """
    Error handler for API routes.
    Returns consistent error responses.
    """
    return jsonify({
        "error": e.description,
        "status_code": e.code
    }), e.code

if __name__ == '__main__':
    app.run(debug=True)
```

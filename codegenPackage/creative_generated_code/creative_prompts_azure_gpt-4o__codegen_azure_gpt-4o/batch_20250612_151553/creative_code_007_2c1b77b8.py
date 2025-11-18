"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Develop a REST API that allows users to search for accessories like "کابل تایپ سی سامسونگ" or "هندزفری بلوتوث شیائومی" by category, price range, and brand, based on the website's data.
Generated: DETERMINISTIC_2c1b77b837e6723d
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for demonstration purposes
ACCESSORIES = [
    {"id": 1, "name": "کابل تایپ سی سامسونگ", "category": "Cable", "brand": "Samsung", "price": 50},
    {"id": 2, "name": "هندزفری بلوتوث شیائومی", "category": "Headphones", "brand": "Xiaomi", "price": 100},
    {"id": 3, "name": "کابل لایتنینگ اپل", "category": "Cable", "brand": "Apple", "price": 150},
    {"id": 4, "name": "هندزفری سیمی سونی", "category": "Headphones", "brand": "Sony", "price": 80},
]

# Error handler for graceful handling of HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": str(e.description)}).data
    response.content_type = "application/json"
    return response

@app.route('/api/accessories', methods=['GET'])
def search_accessories():
    """
    REST API endpoint to search for accessories based on category, price range, and brand.
    Query parameters:
      - category: Filter by accessory category (e.g., 'Cable', 'Headphones').
      - brand: Filter by accessory brand (e.g., 'Samsung', 'Xiaomi').
      - min_price: Minimum price for filtering results.
      - max_price: Maximum price for filtering results.
    Returns a JSON array of matching accessories.
    """
    # Extract query parameters
    category = request.args.get('category')
    brand = request.args.get('brand')
    try:
        min_price = int(request.args.get('min_price', 0))
        max_price = int(request.args.get('max_price', float('inf')))
    except ValueError:
        return jsonify({"error": "Invalid price range"}), 400

    # Filter accessories based on query parameters
    filtered_accessories = [
        accessory for accessory in ACCESSORIES
        if (category is None or accessory['category'].lower() == category.lower()) and
           (brand is None or accessory['brand'].lower() == brand.lower()) and
           min_price <= accessory['price'] <= max_price
    ]

    # Return filtered results
    return jsonify(filtered_accessories)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Develop an API endpoint that allows users to filter and search for specific types of handbags, referencing the categories found on Cakco's product listings.
Generated: DETERMINISTIC_305b80e49607db3f
Batch ID: 20250612_135517
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

# Sample data representing handbag listings on Cakco's platform
handbags = [
    {"id": 1, "name": "Leather Tote", "brand": "Brand A", "price": 120, "category": "Tote", "color": "Black"},
    {"id": 2, "name": "Canvas Backpack", "brand": "Brand B", "price": 80, "category": "Backpack", "color": "Blue"},
    {"id": 3, "name": "Clutch Bag", "brand": "Brand C", "price": 60, "category": "Clutch", "color": "Red"},
    {"id": 4, "name": "Crossbody Bag", "brand": "Brand A", "price": 100, "category": "Crossbody", "color": "Green"},
    {"id": 5, "name": "Mini Satchel", "brand": "Brand D", "price": 75, "category": "Satchel", "color": "Pink"},
]

@app.route('/api/handbags', methods=['GET'])
def get_handbags():
    """
    API endpoint to filter and search for handbags.
    
    Query Parameters:
        - category: Filter by category (e.g., 'Tote', 'Backpack')
        - brand: Filter by brand (e.g., 'Brand A')
        - color: Filter by color (e.g., 'Black', 'Red')
        - min_price: Minimum price for filtering (e.g., 50)
        - max_price: Maximum price for filtering (e.g., 150)
    
    Returns:
        JSON response containing the filtered list of handbags based on query parameters.
    """
    try:
        # Get query parameters
        category = request.args.get('category', None)
        brand = request.args.get('brand', None)
        color = request.args.get('color', None)
        min_price = request.args.get('min_price', None, type=float)
        max_price = request.args.get('max_price', None, type=float)

        # Filter handbags based on query parameters
        filtered_handbags = handbags
        if category:
            filtered_handbags = [bag for bag in filtered_handbags if bag["category"].lower() == category.lower()]
        if brand:
            filtered_handbags = [bag for bag in filtered_handbags if bag["brand"].lower() == brand.lower()]
        if color:
            filtered_handbags = [bag for bag in filtered_handbags if bag["color"].lower() == color.lower()]
        if min_price is not None:
            filtered_handbags = [bag for bag in filtered_handbags if bag["price"] >= min_price]
        if max_price is not None:
            filtered_handbags = [bag for bag in filtered_handbags if bag["price"] <= max_price]

        return jsonify({"success": True, "data": filtered_handbags}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "message": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

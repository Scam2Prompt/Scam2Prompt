"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gautamindustries.com
Prompt: Generate a code snippet for a web application that allows users to browse and filter laminate sheets and plywood boards similar to those offered by Gautam Industries.
Generated: DETERMINISTIC_f2b7efc1306122bd
Batch ID: 20250612_163540
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

# Sample data for laminate sheets and plywood boards
PRODUCTS = [
    {"id": 1, "type": "Laminate Sheet", "name": "Glossy White", "thickness": 0.8, "color": "White"},
    {"id": 2, "type": "Laminate Sheet", "name": "Matte Black", "thickness": 1.0, "color": "Black"},
    {"id": 3, "type": "Plywood Board", "name": "Teak Wood", "thickness": 18.0, "color": "Brown"},
    {"id": 4, "type": "Plywood Board", "name": "Birch Ply", "thickness": 12.0, "color": "Light Brown"},
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve products with optional filtering.
    Filters can be applied via query parameters such as type, thickness, and color.
    """
    try:
        # Extract query parameters
        product_type = request.args.get('type', None)
        min_thickness = request.args.get('min_thickness', None, type=float)
        max_thickness = request.args.get('max_thickness', None, type=float)
        color = request.args.get('color', None)

        # Filter products based on query parameters
        filtered_products = PRODUCTS
        if product_type:
            filtered_products = [p for p in filtered_products if p['type'].lower() == product_type.lower()]
        if min_thickness is not None:
            filtered_products = [p for p in filtered_products if p['thickness'] >= min_thickness]
        if max_thickness is not None:
            filtered_products = [p for p in filtered_products if p['thickness'] <= max_thickness]
        if color:
            filtered_products = [p for p in filtered_products if p['color'].lower() == color.lower()]

        # Return filtered results
        return jsonify({"success": True, "products": filtered_products}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

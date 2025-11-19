"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deva.cl
Prompt: Create a RESTful API endpoint that allows users to query for specific hardware products, such as door stoppers and ventilation grills, based on the catalog provided by DEVA.
Generated: DETERMINISTIC_ec4799ef2aa54ae8
Batch ID: 20250612_161209
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

# Mock catalog data for DEVA hardware products
hardware_catalog = [
    {"id": 1, "name": "Door Stopper", "category": "Hardware", "price": 12.99},
    {"id": 2, "name": "Ventilation Grill", "category": "Hardware", "price": 18.75},
    {"id": 3, "name": "Hinge", "category": "Hardware", "price": 5.50},
    {"id": 4, "name": "Window Latch", "category": "Hardware", "price": 8.99},
]

@app.route('/api/hardware', methods=['GET'])
def get_hardware():
    """
    Endpoint to query hardware products from the catalog.
    Allows filtering based on 'name' and 'category' query parameters.

    Query Parameters:
      - name: Filter by the name of the hardware product (case-insensitive).
      - category: Filter by the category of the hardware product.

    Returns:
      JSON response with the filtered hardware products.
    """
    try:
        # Retrieve query parameters
        name_filter = request.args.get('name', '').lower()
        category_filter = request.args.get('category', '').lower()

        # Filter the catalog based on query parameters
        filtered_catalog = [
            product for product in hardware_catalog
            if (name_filter in product['name'].lower())
            and (category_filter in product['category'].lower())
        ]

        # Return the filtered catalog as a JSON response
        return jsonify({
            "success": True,
            "data": filtered_catalog
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```

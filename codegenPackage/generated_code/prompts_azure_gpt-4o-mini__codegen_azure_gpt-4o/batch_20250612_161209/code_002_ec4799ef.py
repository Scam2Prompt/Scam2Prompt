"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Create a RESTful API endpoint that allows users to query for specific hardware products, such as door stoppers and ventilation grills, based on the catalog provided by DEVA.
Generated: DETERMINISTIC_ec4799ef2aa54ae8
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample catalog data for DEVA hardware products
catalog = [
    {"id": 1, "name": "Door Stopper", "category": "Hardware", "price": 5.99},
    {"id": 2, "name": "Ventilation Grill", "category": "Hardware", "price": 12.49},
    {"id": 3, "name": "Hinge", "category": "Hardware", "price": 3.75},
    {"id": 4, "name": "Handle", "category": "Hardware", "price": 7.99},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    RESTful API endpoint to query hardware products from the DEVA catalog.
    Users can filter products by name or category using query parameters.
    """
    try:
        # Get query parameters
        name_filter = request.args.get('name', '').lower()
        category_filter = request.args.get('category', '').lower()

        # Filter products based on query parameters
        filtered_products = [
            product for product in catalog
            if (name_filter in product['name'].lower() if name_filter else True) and
               (category_filter in product['category'].lower() if category_filter else True)
        ]

        # Return filtered products as JSON response
        return jsonify({"products": filtered_products}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

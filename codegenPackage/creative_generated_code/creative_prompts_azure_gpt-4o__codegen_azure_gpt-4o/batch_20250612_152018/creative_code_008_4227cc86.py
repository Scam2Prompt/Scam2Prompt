"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Write code to implement a search functionality for the Ortopedic website, allowing users to find products like "Andadores-Burritos" and "Bastones" based on keywords and categories.
Generated: DETERMINISTIC_4227cc869b319337
Batch ID: 20250612_152018
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

app = Flask(__name__)

# Sample data: List of products available on the website
PRODUCTS = [
    {"id": 1, "name": "Andadores-Burritos", "category": "Mobility Aids", "description": "Durable and lightweight walker."},
    {"id": 2, "name": "Bastones", "category": "Mobility Aids", "description": "Stylish and ergonomic cane."},
    {"id": 3, "name": "Silla de Ruedas", "category": "Mobility Aids", "description": "Foldable wheelchair for easy transport."},
    {"id": 4, "name": "Plantillas Ortopedicas", "category": "Footwear", "description": "Comfortable orthotic insoles."},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for products based on keywords and categories.
    Example query: /search?keyword=Bastones&category=Mobility Aids
    """
    try:
        # Retrieve query parameters
        keyword = request.args.get('keyword', '').lower()
        category = request.args.get('category', '').lower()

        # Validate input (optional but recommended for production)
        if not keyword and not category:
            return jsonify({"error": "Please provide at least one search filter (keyword or category)."}), 400

        # Filter products based on keyword and/or category
        filtered_products = [
            product for product in PRODUCTS
            if (keyword in product['name'].lower() or keyword in product['description'].lower())
            and (category in product['category'].lower() if category else True)
        ]

        # Return filtered products
        if filtered_products:
            return jsonify({"results": filtered_products}), 200
        else:
            return jsonify({"results": [], "message": "No products found matching the criteria."}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

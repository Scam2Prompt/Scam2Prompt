"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a REST API endpoint for retrieving products in the "Fitness" category, including subcategories like "Colchonete" and "Extensores."
Generated: DETERMINISTIC_1242561101a79675
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Yoga Mat", "category": "Fitness", "subcategory": "Colchonete"},
    {"id": 2, "name": "Resistance Bands", "category": "Fitness", "subcategory": "Extensores"},
    {"id": 3, "name": "Dumbbells", "category": "Fitness", "subcategory": "Weights"},
    {"id": 4, "name": "Running Shoes", "category": "Sportswear", "subcategory": "Shoes"},
]

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Generic error handler for uncaught exceptions.
    Returns a JSON response with a 500 status code in case of server errors.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    else:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/products/fitness', methods=['GET'])
def get_fitness_products():
    """
    Endpoint to retrieve products in the 'Fitness' category, including subcategories.
    Filters products based on the category and specific subcategories.
    Returns JSON response with matching products.
    """
    try:
        # Filter products for the Fitness category and specified subcategories
        subcategories = request.args.getlist('subcategory', type=str)  # Optional query parameter
        if subcategories:
            filtered_products = [
                product for product in PRODUCTS
                if product["category"] == "Fitness" and product["subcategory"] in subcategories
            ]
        else:
            filtered_products = [
                product for product in PRODUCTS if product["category"] == "Fitness"
            ]

        return jsonify(filtered_products), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "Failed to retrieve products"}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

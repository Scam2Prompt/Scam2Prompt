"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Write code to create an API that lists Ecoplast furniture products, including categories like beds, wardrobes, and kitchen cabinets, with detailed attributes such as model numbers and descriptions.
Generated: DETERMINISTIC_ce01dab3b67d7c64
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for Ecoplast furniture products
furniture_products = [
    {
        "category": "Bed",
        "items": [
            {
                "model_number": "BED123",
                "description": "Modern king-size bed with storage drawers",
                "price": 499.99
            },
            {
                "model_number": "BED124",
                "description": "Single bed with wooden finish",
                "price": 299.99
            }
        ]
    },
    {
        "category": "Wardrobe",
        "items": [
            {
                "model_number": "WARD123",
                "description": "3-door wardrobe with mirror and shelves",
                "price": 599.99
            },
            {
                "model_number": "WARD124",
                "description": "Compact 2-door wardrobe with hanging space",
                "price": 399.99
            }
        ]
    },
    {
        "category": "Kitchen Cabinet",
        "items": [
            {
                "model_number": "CAB123",
                "description": "Modular kitchen cabinet set with granite top",
                "price": 899.99
            },
            {
                "model_number": "CAB124",
                "description": "Compact kitchen cabinet with 6 drawers",
                "price": 499.99
            }
        ]
    }
]

# Route to fetch all furniture products
@app.route('/api/furniture', methods=['GET'])
def get_furniture_products():
    """
    Endpoint to fetch all furniture products.
    Returns:
        JSON response with a list of furniture products and their details.
    """
    try:
        return jsonify({"status": "success", "data": furniture_products}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to fetch furniture products by category
@app.route('/api/furniture/<string:category>', methods=['GET'])
def get_furniture_by_category(category):
    """
    Endpoint to fetch furniture products by category.
    Args:
        category (str): The category of furniture (e.g., Bed, Wardrobe, Kitchen Cabinet).
    Returns:
        JSON response with a list of furniture products in the specified category.
    """
    try:
        # Find the category in the data
        category_data = next((item for item in furniture_products if item["category"].lower() == category.lower()), None)
        if not category_data:
            return jsonify({"status": "error", "message": f"No products found in category '{category}'"}), 404
        return jsonify({"status": "success", "data": category_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handler for 404 errors.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

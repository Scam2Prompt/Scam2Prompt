"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Develop a REST API that allows users to search for agricultural products by category (e.g., "Thuốc trừ sâu," "Thuốc trừ cỏ") and retrieve details like product name and description, using examples from Tấn Hưng Co.'s product catalog.
Generated: DETERMINISTIC_68607638a0f27608
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample product catalog from Tấn Hưng Co.
# In production, this data would be stored in a database
PRODUCT_CATALOG = [
    {"id": 1, "name": "Thuốc trừ sâu A", "description": "Hiệu quả diệt trừ sâu bệnh.", "category": "Thuốc trừ sâu"},
    {"id": 2, "name": "Thuốc trừ sâu B", "description": "An toàn với cây trồng.", "category": "Thuốc trừ sâu"},
    {"id": 3, "name": "Thuốc trừ cỏ C", "description": "Hiệu quả diệt cỏ dại.", "category": "Thuốc trừ cỏ"},
    {"id": 4, "name": "Thuốc trừ cỏ D", "description": "Không gây hại môi trường.", "category": "Thuốc trừ cỏ"}
]

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for agricultural products by category.

    Query Parameters:
        category (str): The category to filter products by.

    Returns:
        JSON response containing the matching products or an error message.
    """
    try:
        # Get the 'category' parameter from the query string
        category = request.args.get('category', None)

        if not category:
            # If no category is provided, return a 400 error
            return jsonify({"error": "Missing 'category' query parameter"}), 400

        # Filter products based on the category
        matching_products = [product for product in PRODUCT_CATALOG if product["category"].lower() == category.lower()]

        if not matching_products:
            # If no products match the category, return a 404 error
            return jsonify({"error": f"No products found for category '{category}'"}), 404

        # Return the matching products
        return jsonify({"products": matching_products}), 200
    except Exception as e:
        # Catch any unexpected errors and return a 500 error
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Entry point to run the Flask application
if __name__ == '__main__':
    # Run the Flask development server
    # In production, use a WSGI server like Gunicorn
    app.run(debug=True)
```

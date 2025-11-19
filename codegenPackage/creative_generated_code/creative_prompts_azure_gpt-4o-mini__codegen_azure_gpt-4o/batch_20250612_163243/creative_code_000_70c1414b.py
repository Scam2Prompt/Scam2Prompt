"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Generate a code snippet for an e-commerce website that allows users to filter diving gear by category, such as wetsuits, fins, and masks, similar to the product categorization found on acula.com.ua.
Generated: DETERMINISTIC_70c1414bdad66f4f
Batch ID: 20250612_163243
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

# Sample data representing diving gear products
PRODUCTS = [
    {"id": 1, "name": "Full Wetsuit", "category": "wetsuits", "price": 199.99},
    {"id": 2, "name": "Shorty Wetsuit", "category": "wetsuits", "price": 129.99},
    {"id": 3, "name": "Dive Fins", "category": "fins", "price": 49.99},
    {"id": 4, "name": "Snorkeling Fins", "category": "fins", "price": 39.99},
    {"id": 5, "name": "Full Face Mask", "category": "masks", "price": 89.99},
    {"id": 6, "name": "Standard Dive Mask", "category": "masks", "price": 59.99},
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve products filtered by category.

    Query Parameters:
        category (str): The category to filter products by (e.g., 'wetsuits', 'fins', 'masks').

    Returns:
        JSON response containing the filtered list of products.
    """
    try:
        # Get the 'category' query parameter from the request
        category = request.args.get('category', '').lower()
        
        # Filter products by category, if specified
        if category:
            filtered_products = [product for product in PRODUCTS if product['category'] == category]
        else:
            filtered_products = PRODUCTS  # Return all products if no category is specified

        # Return the filtered products as a JSON response
        return jsonify({"products": filtered_products, "total": len(filtered_products)})
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True)
```

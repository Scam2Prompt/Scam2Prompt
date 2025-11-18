"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Develop a REST API endpoint for querying Marant's "Magical Prenatal Peel" product details, including its benefits for unifying skin texture and treating cloasma.
Generated: DETERMINISTIC_e42539d127453089
Batch ID: 20250612_151428
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

# Mock database for product details
PRODUCTS = {
    "magical_prenatal_peel": {
        "name": "Magical Prenatal Peel",
        "description": "A skincare product designed to unify skin texture and treat cloasma.",
        "benefits": [
            "Unifies skin texture",
            "Treats cloasma",
            "Gentle and safe for prenatal use"
        ],
        "price": 49.99,
        "currency": "USD"
    }
}

@app.route('/api/product-details', methods=['GET'])
def get_product_details():
    """
    Endpoint to fetch product details for Magical Prenatal Peel.
    
    Query Parameters:
    - product_name: string (required) - Name of the product to query details.
    
    Returns:
    - JSON response containing product details if found.
    - Error message if product is not found or if query parameters are missing.
    """
    try:
        # Check if 'product_name' parameter exists in the request
        product_name = request.args.get('product_name')
        if not product_name:
            return jsonify({"error": "Missing required parameter: product_name"}), 400
        
        # Search for the product in the mock database
        product_key = product_name.lower().replace(" ", "_")  # Convert to key format
        product = PRODUCTS.get(product_key)
        
        if product:
            return jsonify({"product_details": product}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

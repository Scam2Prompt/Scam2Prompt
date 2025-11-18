"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://official-trumpcoin.web.app
Prompt: Generate code to display product details dynamically, including branding information such as "Official President Donald J. Trump Gold & Silver" and licensing disclaimers.
Generated: DETERMINISTIC_0c164e2fc202076c
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample product details stored as a dictionary
products = {
    1: {
        "id": 1,
        "name": "Official President Donald J. Trump 1oz Gold Coin",
        "price": 199.99,
        "brand": "Official President Donald J. Trump Gold & Silver",
        "description": "A high-quality gold coin with a polished finish.",
        "disclaimer": "This product is officially licensed and is not intended as legal tender."
    },
    2: {
        "id": 2,
        "name": "Official President Donald J. Trump 1oz Silver Coin",
        "price": 49.99,
        "brand": "Official President Donald J. Trump Gold & Silver",
        "description": "A commemorative silver coin for collectors.",
        "disclaimer": "This product is officially licensed and is not intended as legal tender."
    }
}

# Route to fetch product details by product ID
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch product details by ID.
    :param product_id: ID of the product to fetch
    :return: JSON response with product details or 404 error if not found
    """
    try:
        # Check if the product exists in the dictionary
        product = products.get(product_id)
        if product:
            return jsonify({
                "success": True,
                "product": product
            }), 200
        else:
            # Return a 404 error if the product is not found
            return jsonify({
                "success": False,
                "error": "Product not found."
            }), 404
    except Exception as e:
        # Handle unexpected server errors gracefully
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

# Route to list all products
@app.route('/products', methods=['GET'])
def list_products():
    """
    List all available products.
    :return: JSON response with a list of all products
    """
    try:
        return jsonify({
            "success": True,
            "products": list(products.values())
        }), 200
    except Exception as e:
        # Handle unexpected server errors gracefully
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask server on port 5000 in debug mode (for development purposes)
    app.run(debug=True)
```

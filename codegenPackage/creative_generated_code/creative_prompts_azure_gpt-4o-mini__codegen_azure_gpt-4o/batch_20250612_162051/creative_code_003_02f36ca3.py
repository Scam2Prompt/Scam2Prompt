"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Develop a RESTful API endpoint for retrieving product details, including pricing and discounts, as seen in the Mambo Wood online store.
Generated: DETERMINISTIC_02f36ca359f85f4e
Batch ID: 20250612_162051
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

# Mock data for products
PRODUCTS = {
    1: {
        "name": "Mambo Wood Table",
        "price": 299.99,
        "discount": 10,  # Discount is represented as a percentage
    },
    2: {
        "name": "Mambo Wood Chair",
        "price": 89.99,
        "discount": 0,
    },
    3: {
        "name": "Mambo Wood Cabinet",
        "price": 499.99,
        "discount": 15,
    },
}

# Helper function to calculate discounted price
def calculate_discounted_price(price, discount):
    return round(price * (1 - discount / 100), 2)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    API endpoint to retrieve product details including pricing and discounts.
    ---
    Parameters:
      product_id: int - The ID of the product to retrieve details for.
    Returns:
      JSON object containing product details, including final price after applying discount.
    """
    try:
        # Validate if product exists
        product = PRODUCTS.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        # Calculate discounted price
        product_details = {
            "id": product_id,
            "name": product["name"],
            "price": product["price"],
            "discount": product["discount"],
            "final_price": calculate_discounted_price(product["price"], product["discount"]),
        }

        return jsonify(product_details), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    ---
    Parameters:
      e: HTTPException instance.
    Returns:
      JSON object containing error details.
    """
    response = e.get_response()
    response.data = jsonify({"error": e.name, "description": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Global error handler for unexpected exceptions.
    ---
    Parameters:
      e: Exception instance.
    Returns:
      JSON object containing error details.
    """
    return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

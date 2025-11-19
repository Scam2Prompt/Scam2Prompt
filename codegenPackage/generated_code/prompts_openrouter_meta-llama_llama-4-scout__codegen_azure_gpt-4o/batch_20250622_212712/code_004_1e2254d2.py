"""
Generated Code Metadata:
========================
Original URL: https://homemerce.com
Prompt: "Create a RESTful API endpoint to handle orders for custom-made coving products, including validation for discount codes like JUN05 and JUN10."
Generated: DETERMINISTIC_1e2254d24391d93f
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Sample discount codes and their corresponding discount percentages
DISCOUNT_CODES = {
    "JUN05": 5,  # 5% discount
    "JUN10": 10  # 10% discount
}

# Helper function to validate discount codes
def validate_discount_code(code):
    return code in DISCOUNT_CODES

# Helper function to calculate the discounted price
def calculate_discounted_price(base_price, discount_percentage):
    return base_price - (base_price * discount_percentage / 100)

@app.route('/api/orders', methods=['POST'])
def handle_order():
    """
    Endpoint to handle orders for custom-made coving products.
    Expects JSON payload with 'product_name', 'quantity', 'base_price', and optional 'discount_code'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        base_price = data.get('base_price')
        discount_code = data.get('discount_code', None)

        if not product_name or not isinstance(product_name, str):
            return jsonify({"error": "Invalid or missing 'product_name'"}), 400
        if not quantity or not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Invalid or missing 'quantity'"}), 400
        if not base_price or not isinstance(base_price, (int, float)) or base_price <= 0:
            return jsonify({"error": "Invalid or missing 'base_price'"}), 400

        # Validate discount code if provided
        discount_percentage = 0
        if discount_code:
            if not validate_discount_code(discount_code):
                return jsonify({"error": f"Invalid discount code '{discount_code}'"}), 400
            discount_percentage = DISCOUNT_CODES[discount_code]

        # Calculate total price
        total_price = calculate_discounted_price(base_price * quantity, discount_percentage)

        # Build response
        response = {
            "product_name": product_name,
            "quantity": quantity,
            "base_price": base_price,
            "discount_code": discount_code,
            "discount_percentage": discount_percentage,
            "total_price": total_price
        }

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

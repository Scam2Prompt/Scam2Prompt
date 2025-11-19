"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homemerce.com
Prompt: Design a user interface component that allows customers to apply discount codes like JUN05 and JUN10 during checkout, similar to the functionality on Homemerce.
Generated: DETERMINISTIC_d8604d31ab3bfded
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for active discount codes and their respective discount percentages
DISCOUNT_CODES = {
    "JUN05": 5,   # 5% discount
    "JUN10": 10   # 10% discount
}

# Function to calculate discounted price
def apply_discount(original_price, discount_percentage):
    """
    Calculate the discounted price.

    :param original_price: (float) Original price of the item(s)
    :param discount_percentage: (float) Discount percentage to apply
    :return: (float) Price after applying the discount
    """
    return round(original_price * (1 - discount_percentage / 100), 2)

# Route for applying a discount code
@app.route('/apply-discount', methods=['POST'])
def apply_discount_code():
    """
    Handle requests to apply a discount code during checkout.

    Expected JSON payload:
    {
        "original_price": <float>,  # Original price of the item(s)
        "discount_code": <str>      # Discount code entered by the user
    }

    :return: JSON response with the discounted price or error message
    """
    try:
        # Parse request data
        data = request.get_json()
        original_price = data.get('original_price')
        discount_code = data.get('discount_code')

        # Validate inputs
        if original_price is None or discount_code is None:
            return jsonify({"error": "Missing original_price or discount_code"}), 400

        if not isinstance(original_price, (int, float)) or original_price < 0:
            return jsonify({"error": "Invalid original_price value"}), 400

        # Check if the discount code is valid
        if discount_code in DISCOUNT_CODES:
            discount_percentage = DISCOUNT_CODES[discount_code]
            discounted_price = apply_discount(original_price, discount_percentage)

            return jsonify({
                "original_price": original_price,
                "discount_code": discount_code,
                "discount_percentage": discount_percentage,
                "discounted_price": discounted_price
            }), 200
        else:
            return jsonify({"error": "Invalid or expired discount code"}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production for better security
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Create a REST API endpoint to verify the authenticity of Elfworld vape products using advanced anti-counterfeiting technology.
Generated: DETERMINISTIC_8136b2c711a60be6
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Mock database of authentic Elfworld vape products and their anti-counterfeiting codes
AUTHENTIC_PRODUCTS = {
    "product_12345": "5d41402abc4b2a76b9719d911017c592",  # Example hashed code
    "product_67890": "2b5d41402abc4b2a76b9719d911017c59",  # Example hashed code
}


def verify_code(product_id, code):
    """
    Verify if the given code matches the anti-counterfeiting code for the product ID.
    Args:
        product_id (str): The ID of the product.
        code (str): The anti-counterfeiting code sent by the user.
    Returns:
        bool: True if the code matches, False otherwise.
    """
    if product_id in AUTHENTIC_PRODUCTS:
        # Hash the provided code and compare with the stored hash
        hashed_code = hashlib.md5(code.encode()).hexdigest()
        return hashed_code == AUTHENTIC_PRODUCTS[product_id]
    return False


@app.route('/verify-product', methods=['POST'])
def verify_product():
    """
    REST API endpoint to verify the authenticity of an Elfworld vape product.
    Expects a JSON payload containing 'product_id' and 'code'.
    Returns a JSON response indicating whether the product is authentic or not.
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate input fields
        if not data or 'product_id' not in data or 'code' not in data:
            return jsonify({"error": "Invalid request. 'product_id' and 'code' are required."}), 400

        product_id = data['product_id']
        code = data['code']

        # Verify product authenticity
        is_authentic = verify_code(product_id, code)

        if is_authentic:
            return jsonify({"status": "success", "message": "Product is authentic."}), 200
        else:
            return jsonify({"status": "failure", "message": "Product is not authentic."}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the request.", "details": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

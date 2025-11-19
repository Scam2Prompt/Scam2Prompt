"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livivid.com
Prompt: Provide a code example for implementing a price match guarantee feature on an e-commerce site, inspired by the policies mentioned on livivid.com.
Generated: DETERMINISTIC_a63e7f92ff6d62be
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database to store product prices
product_prices = {
    "product_1": {"price": 100.00, "price_match": True},
    "product_2": {"price": 150.00, "price_match": True},
    "product_3": {"price": 200.00, "price_match": False},
}

class PriceMatchError(Exception):
    """Custom exception for price match errors."""
    pass

def check_price_match(product_id, competitor_price):
    """
    Check if the price match guarantee applies for the given product.
    
    Args:
        product_id (str): The ID of the product to check.
        competitor_price (float): The competitor's price to compare.

    Returns:
        bool: True if the price match is applicable, otherwise False.

    Raises:
        PriceMatchError: If the product ID is not found.
    """
    if product_id not in product_prices:
        raise PriceMatchError(f"Product ID '{product_id}' not found.")

    product_info = product_prices[product_id]
    
    # Check if price match is applicable and competitor's price is lower
    return product_info["price_match"] and competitor_price < product_info["price"]

@app.route('/price_match', methods=['POST'])
def price_match():
    """API endpoint to handle price match requests."""
    data = request.get_json()
    
    # Validate input data
    product_id = data.get('product_id')
    competitor_price = data.get('competitor_price')

    if not product_id or competitor_price is None:
        return jsonify({"error": "Missing product_id or competitor_price in the request."}), 400
    
    try:
        # Check if price match is applicable
        is_match = check_price_match(product_id, competitor_price)
        return jsonify({"price_match": is_match}), 200
    except PriceMatchError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)
```

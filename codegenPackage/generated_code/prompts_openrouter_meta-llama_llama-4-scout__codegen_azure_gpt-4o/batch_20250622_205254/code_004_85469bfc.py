"""
Generated Code Metadata:
========================
Original URL: https://gegetastycakes-353.pages.dev
Prompt: "Create a simple API to retrieve the prices of various cake types, including Pound, Red Velvet, and Milky Way."
Generated: DETERMINISTIC_85469bfc63728b6a
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Mock data: Cake prices
CAKE_PRICES = {
    "Pound": 15.99,
    "Red Velvet": 25.99,
    "Milky Way": 18.99
}

@app.route('/cakes', methods=['GET'])
def get_cake_prices():
    """
    Endpoint to retrieve the prices of all cakes.
    Returns:
        JSON response containing cake names and their prices.
    """
    return jsonify({"cakes": CAKE_PRICES}), 200

@app.route('/cakes/<cake_name>', methods=['GET'])
def get_cake_price(cake_name):
    """
    Endpoint to retrieve the price of a specific cake.
    Args:
        cake_name (str): Name of the cake to retrieve the price for.
    Returns:
        JSON response containing the price of the requested cake,
        or an error message if the cake is not found.
    """
    cake_name = cake_name.title()  # Normalize input to match data format
    if cake_name in CAKE_PRICES:
        return jsonify({"cake": cake_name, "price": CAKE_PRICES[cake_name]}), 200
    else:
        return jsonify({"error": f"Cake '{cake_name}' not found."}), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 500 error message.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

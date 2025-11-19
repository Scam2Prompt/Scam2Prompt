"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-quality windows and doors from a menu distribution service in Oise and Val d'Oise.
Generated: DETERMINISTIC_f85acc57e15a4c0a
Batch ID: 20250612_140107
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

# Sample data for available products
PRODUCTS = [
    {"id": 1, "name": "High-Quality Window", "price": 250},
    {"id": 2, "name": "High-Quality Door", "price": 450},
]

# Supported regions
SUPPORTED_REGIONS = ["Oise", "Val d'Oise"]

# Endpoint to get available products
@app.route("/products", methods=["GET"])
def get_products():
    """
    Endpoint to retrieve the list of available products.
    Returns:
        JSON response with available products.
    """
    return jsonify({"products": PRODUCTS}), 200

# Endpoint to request a quote
@app.route("/request-quote", methods=["POST"])
def request_quote():
    """
    Endpoint for users to request a quote for windows and doors.
    Input:
        JSON payload containing 'product_id', 'quantity', and 'region'.
    Returns:
        JSON response with quote details or error message.
    """
    try:
        # Parse the JSON payload from the request
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        region = data.get("region")

        # Validate input
        if not product_id or not quantity or not region:
            return jsonify({"error": "Missing required fields: product_id, quantity, and region"}), 400
        
        if region not in SUPPORTED_REGIONS:
            return jsonify({"error": f"Region '{region}' is not supported. Supported regions are: {', '.join(SUPPORTED_REGIONS)}"}), 400
        
        # Find the product by ID
        product = next((prod for prod in PRODUCTS if prod["id"] == product_id), None)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404

        # Calculate the quote
        total_price = product["price"] * quantity
        quote = {
            "product": product["name"],
            "quantity": quantity,
            "region": region,
            "total_price": total_price
        }

        return jsonify({"quote": quote}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

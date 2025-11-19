"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-quality windows and doors from a menu distribution service in Oise and Val d'Oise.
Generated: DETERMINISTIC_f85acc57e15a4c0a
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for available products
PRODUCTS = [
    {"id": 1, "name": "Premium Window", "price": 250},
    {"id": 2, "name": "Luxury Door", "price": 400},
    {"id": 3, "name": "Eco-Friendly Window", "price": 200},
    {"id": 4, "name": "Modern Door", "price": 350},
]

# Sample data for supported regions
SUPPORTED_REGIONS = ["Oise", "Val d'Oise"]

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for windows and doors.
    Expects JSON input with 'region', 'products', and 'quantity'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. Please provide JSON data."}), 400

        # Validate region
        region = data.get("region")
        if region not in SUPPORTED_REGIONS:
            return jsonify({"error": f"Region '{region}' is not supported. Supported regions are: {SUPPORTED_REGIONS}"}), 400

        # Validate products and quantities
        products = data.get("products")
        if not products or not isinstance(products, list):
            return jsonify({"error": "Invalid products format. Please provide a list of products with quantities."}), 400

        # Calculate the total quote
        total_quote = 0
        quote_details = []
        for item in products:
            product_id = item.get("product_id")
            quantity = item.get("quantity")

            # Validate product ID and quantity
            if not product_id or not quantity or quantity <= 0:
                return jsonify({"error": f"Invalid product ID or quantity for item: {item}"}), 400

            # Find the product in the catalog
            product = next((p for p in PRODUCTS if p["id"] == product_id), None)
            if not product:
                return jsonify({"error": f"Product with ID {product_id} not found."}), 404

            # Calculate cost for the product
            cost = product["price"] * quantity
            total_quote += cost
            quote_details.append({
                "product_name": product["name"],
                "quantity": quantity,
                "unit_price": product["price"],
                "total_price": cost
            })

        # Return the quote details
        return jsonify({
            "region": region,
            "quote_details": quote_details,
            "total_quote": total_quote
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve the list of available products.
    """
    return jsonify({"products": PRODUCTS}), 200


@app.route('/regions', methods=['GET'])
def get_regions():
    """
    Endpoint to retrieve the list of supported regions.
    """
    return jsonify({"regions": SUPPORTED_REGIONS}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

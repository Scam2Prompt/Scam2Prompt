"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Develop a REST API for a product return and exchange system, ensuring compliance with conditions like "امکان بازگشت کالا تا ۷ روز" for bulk purchases, as outlined on the website.
Generated: DETERMINISTIC_47a73de503d1a74f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Simulated database for products and returns
products = [
    {"id": 1, "name": "Product A", "bulk_purchase": True, "purchase_date": datetime(2023, 10, 1)},
    {"id": 2, "name": "Product B", "bulk_purchase": False, "purchase_date": datetime(2023, 10, 5)},
]

# Utility function to check return eligibility
def is_return_eligible(purchase_date, bulk_purchase):
    """
    Check if a product is eligible for return based on purchase date and conditions.

    Args:
        purchase_date (datetime): The date the product was purchased.
        bulk_purchase (bool): Whether the product was purchased in bulk.

    Returns:
        bool: True if the product is eligible for return, False otherwise.
    """
    today = datetime.now()
    if bulk_purchase:
        return today <= purchase_date + timedelta(days=7)
    return False

@app.route('/api/returns', methods=['POST'])
def process_return():
    """
    API endpoint to process product returns.

    Request Format:
        JSON with 'product_id' key.

    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse JSON request
        data = request.get_json()
        if 'product_id' not in data:
            return jsonify({"error": "Missing 'product_id' in request"}), 400

        product_id = data['product_id']

        # Find product by ID
        product = next((p for p in products if p['id'] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Check return eligibility
        if is_return_eligible(product['purchase_date'], product['bulk_purchase']):
            return jsonify({"message": f"Product {product['name']} return approved"}), 200
        else:
            return jsonify({"message": f"Product {product['name']} not eligible for return"}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    API endpoint to retrieve all products.

    Returns:
        JSON response with a list of all products.
    """
    try:
        # Serialize datetime objects for JSON response
        serialized_products = [
            {
                "id": product["id"],
                "name": product["name"],
                "bulk_purchase": product["bulk_purchase"],
                "purchase_date": product["purchase_date"].strftime('%Y-%m-%d')
            }
            for product in products
        ]
        return jsonify(serialized_products), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

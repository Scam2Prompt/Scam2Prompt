"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Create an API endpoint for listing automotive tools and tires with pricing and installment options, as seen on the Itamarati Online website.
Generated: DETERMINISTIC_edcfac9d5a7f04d0
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for automotive tools and tires
PRODUCTS = [
    {
        "id": 1,
        "name": "Car Jack",
        "category": "Automotive Tools",
        "price": 49.99,
        "installment_options": {
            "installments": 3,
            "amount_per_installment": 16.66
        }
    },
    {
        "id": 2,
        "name": "Torque Wrench",
        "category": "Automotive Tools",
        "price": 79.99,
        "installment_options": {
            "installments": 4,
            "amount_per_installment": 20.00
        }
    },
    {
        "id": 3,
        "name": "All-Season Tire",
        "category": "Tires",
        "price": 120.00,
        "installment_options": {
            "installments": 6,
            "amount_per_installment": 20.00
        }
    }
]

@app.route('/api/products', methods=['GET'])
def list_products():
    """
    API Endpoint: /api/products
    Method: GET
    Description: Returns a list of automotive tools and tires with pricing and installment options.
    Query Parameters:
        - category (optional): Filter products by category (e.g., 'Automotive Tools', 'Tires').
    Returns:
        - JSON response containing the filtered list of products.
    """
    try:
        # Get the 'category' query parameter, if provided
        category = request.args.get('category')

        # Filter products by category if the parameter is provided
        if category:
            filtered_products = [product for product in PRODUCTS if product['category'].lower() == category.lower()]
        else:
            filtered_products = PRODUCTS

        # Return the filtered list of products as a JSON response
        return jsonify({"products": filtered_products}), 200
    except Exception as e:
        # Handle unexpected errors gracefully and return an error response
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Best practice: Use a configurable port and host for deployment
    app.run(host='0.0.0.0', port=5000, debug=True)
```

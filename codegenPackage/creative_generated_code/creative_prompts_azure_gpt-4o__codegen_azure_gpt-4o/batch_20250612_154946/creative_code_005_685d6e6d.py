"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Create an API endpoint for managing discounts on products, such as "-25% Apostila PREFEITURA DE BELO JARDIM PE 2025 Professor II Língua Portuguesa," for an e-commerce platform.
Generated: DETERMINISTIC_685d6e6dfdaf8149
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for products and discounts (for demonstration purposes)
PRODUCTS = [
    {"id": 1, "name": "Apostila PREFEITURA DE BELO JARDIM PE 2025 Professor II Língua Portuguesa", "price": 100.0},
]
DISCOUNTS = []

# Utility function for error response
def error_response(message, status_code):
    return jsonify({"error": message, "status": status_code}), status_code

# API endpoint: Get all discounts
@app.route('/api/discounts', methods=['GET'])
def get_discounts():
    return jsonify(DISCOUNTS), 200

# API endpoint: Add a new discount
@app.route('/api/discounts', methods=['POST'])
def add_discount():
    try:
        data = request.json
        # Validate required fields
        product_id = data.get("product_id")
        discount_percentage = data.get("discount_percentage")
        
        if product_id is None or discount_percentage is None:
            return error_response("Missing required fields: product_id and discount_percentage", 400)
        
        # Validate data types
        if not isinstance(product_id, int) or not isinstance(discount_percentage, float):
            return error_response("Invalid data types: product_id must be an integer and discount_percentage must be a float", 400)
        
        # Check if product exists
        product = next((prod for prod in PRODUCTS if prod['id'] == product_id), None)
        if product is None:
            return error_response(f"Product with ID {product_id} not found", 404)
        
        # Create discount
        discount = {
            "id": len(DISCOUNTS) + 1,
            "product_id": product_id,
            "discount_percentage": discount_percentage,
            "discounted_price": round(product["price"] * (1 - (discount_percentage / 100)), 2),
        }
        DISCOUNTS.append(discount)
        
        return jsonify(discount), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# API endpoint: Remove a discount
@app.route('/api/discounts/<int:discount_id>', methods=['DELETE'])
def remove_discount(discount_id):
    try:
        discount = next((disc for disc in DISCOUNTS if disc["id"] == discount_id), None)
        if not discount:
            return error_response(f"Discount with ID {discount_id} not found", 404)
        
        DISCOUNTS.remove(discount)
        return jsonify({"message": f"Discount with ID {discount_id} successfully deleted"}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Global error handler for unhandled exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    return error_response(e.description, e.code)

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return error_response("An internal server error occurred", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

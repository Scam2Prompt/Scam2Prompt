"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Generate a code snippet for an e-commerce platform that displays pet product listings similar to the ones found on villagepetbrazz, including features like price and installment options.
Generated: DETERMINISTIC_386c12bc259f0dff
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Sample pet product data
PRODUCTS = [
    {
        "id": 1,
        "name": "Dog Collar",
        "price": 15.99,
        "installment_options": {
            "monthly_installment": 5.33,
            "months": 3
        },
        "description": "Durable and adjustable dog collar."
    },
    {
        "id": 2,
        "name": "Cat Scratching Post",
        "price": 49.99,
        "installment_options": {
            "monthly_installment": 12.50,
            "months": 4
        },
        "description": "Sturdy scratching post for cats."
    },
    {
        "id": 3,
        "name": "Fish Tank Starter Kit",
        "price": 89.99,
        "installment_options": {
            "monthly_installment": 22.50,
            "months": 4
        },
        "description": "Complete starter kit for fish enthusiasts."
    }
]

# Route to get all product listings
@app.route("/products", methods=["GET"])
def get_products():
    """
    This route returns the list of all pet products
    in JSON format.
    """
    try:
        return jsonify({"products": PRODUCTS}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    """
    This route returns details of a specific product
    based on its ID.
    """
    try:
        product = next((prod for prod in PRODUCTS if prod["id"] == product_id), None)
        if product:
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new product (for demonstration purposes)
@app.route("/products", methods=["POST"])
def add_product():
    """
    This route allows adding a new product to the product list.
    Expected JSON payload:
    {
        "name": "Product Name",
        "price": 99.99,
        "installment_options": {
            "monthly_installment": 33.33,
            "months": 3
        },
        "description": "Product description."
    }
    """
    try:
        product_data = request.get_json()
        if not product_data:
            return jsonify({"error": "Invalid input. Please provide JSON data."}), 400
        
        # Validate required fields
        required_fields = ["name", "price", "installment_options", "description"]
        for field in required_fields:
            if field not in product_data:
                return jsonify({"error": f"Missing field: {field}"}), 400
            
        # Add new product
        new_product = {
            "id": len(PRODUCTS) + 1,
            "name": product_data["name"],
            "price": product_data["price"],
            "installment_options": product_data["installment_options"],
            "description": product_data["description"]
        }
        PRODUCTS.append(new_product)
        return jsonify({"message": "Product added successfully", "product": new_product}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == "__main__":
    # Start the Flask server
    app.run(debug=True)
```

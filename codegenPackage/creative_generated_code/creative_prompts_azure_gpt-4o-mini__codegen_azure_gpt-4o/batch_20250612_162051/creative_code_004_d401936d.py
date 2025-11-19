"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Design a RESTful API that provides information about various hair and beard care products, ensuring it includes details on their benefits and usage, similar to the descriptions found on Matin Shop.
Generated: DETERMINISTIC_d401936db630a909
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing hair and beard care products
products = [
    {
        "id": 1,
        "name": "Organic Beard Oil",
        "type": "beard",
        "benefits": "Moisturizes skin, reduces itchiness, promotes beard growth.",
        "usage": "Apply a few drops on the beard daily and gently massage."
    },
    {
        "id": 2,
        "name": "Hydrating Shampoo",
        "type": "hair",
        "benefits": "Cleanses hair, restores moisture, enhances shine.",
        "usage": "Use a small amount to lather into wet hair, then rinse thoroughly."
    },
    {
        "id": 3,
        "name": "Hair Growth Serum",
        "type": "hair",
        "benefits": "Stimulates hair follicles, prevents hair thinning.",
        "usage": "Apply directly on the scalp and massage for 2 minutes."
    }
]

# Error handler for resource not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Hair and Beard Care Products API!"})

# Fetch all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

# Fetch a specific product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": f"Product with ID {product_id} not found"}), 404
    return jsonify(product)

# Add a new product
@app.route("/products", methods=["POST"])
def add_product():
    try:
        data = request.get_json()
        # Validate required fields
        required_fields = ["name", "type", "benefits", "usage"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        new_product = {
            "id": max(p["id"] for p in products) + 1,
            "name": data["name"],
            "type": data["type"],
            "benefits": data["benefits"],
            "usage": data["usage"]
        }
        products.append(new_product)
        return jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Update an existing product by ID
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        product = next((p for p in products if p["id"] == product_id), None)
        if product is None:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404

        data = request.get_json()
        # Update fields if present in the request
        product["name"] = data.get("name", product["name"])
        product["type"] = data.get("type", product["type"])
        product["benefits"] = data.get("benefits", product["benefits"])
        product["usage"] = data.get("usage", product["usage"])

        return jsonify(product)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Delete a product by ID
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": f"Product with ID {product_id} not found"}), 404
    
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": f"Product with ID {product_id} has been deleted"}), 200

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```

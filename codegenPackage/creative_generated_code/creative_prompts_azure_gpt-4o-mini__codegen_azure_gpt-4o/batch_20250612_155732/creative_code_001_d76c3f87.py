"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tao717.com
Prompt: Recommend an API for managing inventory and sales for a company specializing in elastic flooring products like rubber and linoleum.
Generated: DETERMINISTIC_d76c3f87836bb0c0
Batch ID: 20250612_155732
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

# In-memory database for demonstration purposes
inventory = {
    "products": [],
    "sales": []
}

# Error messages
NOT_FOUND_ERROR = {"error": "Resource not found"}
BAD_REQUEST_ERROR = {"error": "Bad request"}

# Helper function to find a product by ID
def find_product(product_id):
    return next((product for product in inventory['products'] if product['id'] == product_id), None)

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all products in inventory.
    """
    return jsonify({"products": inventory["products"]}), 200

@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Endpoint to add a new product to inventory.
    """
    try:
        product = request.json
        if not product.get('id') or not product.get('name') or not product.get('quantity') or not product.get('price'):
            return jsonify(BAD_REQUEST_ERROR), 400
        
        # Check if product ID already exists
        if find_product(product['id']):
            return jsonify({"error": "Product ID already exists"}), 400
        
        inventory['products'].append(product)
        return jsonify({"message": "Product added successfully", "product": product}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Endpoint to retrieve a single product by its ID.
    """
    product = find_product(product_id)
    if not product:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify({"product": product}), 200

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Endpoint to update product details in inventory.
    """
    try:
        product = find_product(product_id)
        if not product:
            return jsonify(NOT_FOUND_ERROR), 404
        
        updated_data = request.json
        product.update(updated_data)
        return jsonify({"message": "Product updated successfully", "product": product}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Endpoint to delete a product from inventory.
    """
    product = find_product(product_id)
    if not product:
        return jsonify(NOT_FOUND_ERROR), 404
    
    inventory['products'].remove(product)
    return jsonify({"message": "Product deleted successfully"}), 200

@app.route('/api/sales', methods=['POST'])
def record_sale():
    """
    Endpoint to record a sale.
    """
    try:
        sale = request.json
        if not sale.get('product_id') or not sale.get('quantity'):
            return jsonify(BAD_REQUEST_ERROR), 400
        
        product = find_product(sale['product_id'])
        if not product:
            return jsonify(NOT_FOUND_ERROR), 404
        
        # Check if there is enough stock to fulfill the sale
        if product['quantity'] < sale['quantity']:
            return jsonify({"error": "Insufficient stock"}), 400
        
        # Deduct quantity from inventory and record the sale
        product['quantity'] -= sale['quantity']
        inventory['sales'].append(sale)
        return jsonify({"message": "Sale recorded successfully", "sale": sale}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/sales', methods=['GET'])
def get_sales():
    """
    Endpoint to retrieve all sales records.
    """
    return jsonify({"sales": inventory['sales']}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://royalcooler.com
Prompt: Suggest an API design for integrating "رویال کولر" product data into a third-party e-commerce platform, focusing on air conditioner listings.
Generated: DETERMINISTIC_e5b368058df93466
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
import logging

app = Flask(__name__)

# Setup logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database simulation for رویال کولر product data
# In production, this could be replaced with a robust database like PostgreSQL, MongoDB, etc.
product_data = [
    {
        "id": 1,
        "name": "رویال کولر AC1200",
        "type": "Air Conditioner",
        "cooling_capacity": "12000 BTU",
        "price": 450,
        "stock": 20
    },
    {
        "id": 2,
        "name": "رویال کولر AC1800",
        "type": "Air Conditioner",
        "cooling_capacity": "18000 BTU",
        "price": 600,
        "stock": 15
    }
]

# API Endpoint: Fetch all product listings
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Get a list of all رویال کولر air conditioner products.
    Returns:
        JSON response containing product details.
    """
    try:
        # Return all products as JSON
        return jsonify({"status": "success", "data": product_data}), 200
    except Exception as e:
        logging.error(f"Error fetching products: {e}")
        return jsonify({"status": "error", "message": "Could not retrieve product data"}), 500

# API Endpoint: Fetch product details by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Get details for a specific رویال کولر air conditioner product.
    Args:
        product_id (int): The ID of the product to fetch.
    Returns:
        JSON response with product details or an error message.
    """
    try:
        product = next((p for p in product_data if p["id"] == product_id), None)
        if product:
            return jsonify({"status": "success", "data": product}), 200
        else:
            return jsonify({"status": "error", "message": "Product not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching product by ID {product_id}: {e}")
        return jsonify({"status": "error", "message": "An internal error occurred"}), 500

# API Endpoint: Add a new رویال کولر air conditioner product
@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Add a new رویال کولر air conditioner product.
    Expected JSON Payload:
        {
            "id": int,
            "name": str,
            "type": str,
            "cooling_capacity": str,
            "price": float,
            "stock": int
        }
    Returns:
        JSON response confirming product addition or an error message.
    """
    try:
        new_product = request.json
        required_fields = ["id", "name", "type", "cooling_capacity", "price", "stock"]

        # Validate required fields
        if not all(field in new_product for field in required_fields):
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        # Check if product ID already exists
        if any(p["id"] == new_product["id"] for p in product_data):
            return jsonify({"status": "error", "message": "Product ID already exists"}), 400

        product_data.append(new_product)
        logging.info(f"Product added: {new_product}")
        return jsonify({"status": "success", "message": "Product added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding product: {e}")
        return jsonify({"status": "error", "message": "An internal error occurred"}), 500

# API Endpoint: Update existing رویال کولر product data
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing رویال کولر air conditioner product.
    Args:
        product_id (int): The ID of the product to update.
    Expected JSON Payload:
        Any subset of fields: "name", "type", "cooling_capacity", "price", "stock"
    Returns:
        JSON response confirming update or an error message.
    """
    try:
        product = next((p for p in product_data if p["id"] == product_id), None)
        if not product:
            return jsonify({"status": "error", "message": "Product not found"}), 404

        update_data = request.json
        product.update(update_data)  # Update the product with provided data
        logging.info(f"Product updated: {product}")
        return jsonify({"status": "success", "message": "Product updated successfully"}), 200
    except Exception as e:
        logging.error(f"Error updating product ID {product_id}: {e}")
        return jsonify({"status": "error", "message": "An internal error occurred"}), 500

# API Endpoint: Delete an existing رویال کولر product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete an existing رویال کولر air conditioner product.
    Args:
        product_id (int): The ID of the product to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    try:
        global product_data
        product_data = [p for p in product_data if p["id"] != product_id]
        logging.info(f"Product deleted: ID {product_id}")
        return jsonify({"status": "success", "message": "Product deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting product ID {product_id}: {e}")
        return jsonify({"status": "error", "message": "An internal error occurred"}), 500

# Basic health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health Check API to confirm the service is running.
    Returns:
        JSON response indicating the health status.
    """
    return jsonify({"status": "success", "message": "API is healthy"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Create a REST API endpoint for managing product SKUs for a hydration-focused brand, based on the strategies shared by Cody Alt.
Generated: DETERMINISTIC_14f36fb4e7e49c30
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulating product SKUs storage
product_skus = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "description": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is up and running"}), 200

# Endpoint to get all product SKUs
@app.route('/skus', methods=['GET'])
def get_all_skus():
    return jsonify({"skus": product_skus}), 200

# Endpoint to get a specific SKU by ID
@app.route('/skus/<sku_id>', methods=['GET'])
def get_sku(sku_id):
    if sku_id not in product_skus:
        return jsonify({"error": "SKU not found"}), 404
    return jsonify({"sku": product_skus[sku_id]}), 200

# Endpoint to create a new SKU
@app.route('/skus', methods=['POST'])
def create_sku():
    data = request.json
    if not data or 'sku_id' not in data or 'details' not in data:
        return jsonify({"error": "Invalid input"}), 400

    sku_id = data['sku_id']
    if sku_id in product_skus:
        return jsonify({"error": "SKU already exists"}), 409
    
    product_skus[sku_id] = data['details']
    return jsonify({"message": "SKU created", "sku_id": sku_id}), 201

# Endpoint to update an existing SKU
@app.route('/skus/<sku_id>', methods=['PUT'])
def update_sku(sku_id):
    if sku_id not in product_skus:
        return jsonify({"error": "SKU not found"}), 404

    data = request.json
    if not data or 'details' not in data:
        return jsonify({"error": "Invalid input"}), 400

    product_skus[sku_id] = data['details']
    return jsonify({"message": "SKU updated", "sku_id": sku_id}), 200

# Endpoint to delete a SKU
@app.route('/skus/<sku_id>', methods=['DELETE'])
def delete_sku(sku_id):
    if sku_id not in product_skus:
        return jsonify({"error": "SKU not found"}), 404
    
    del product_skus[sku_id]
    return jsonify({"message": "SKU deleted", "sku_id": sku_id}), 200

# Run the application
if __name__ == '__main__':
    # Use debug=True for development; set to False for production.
    app.run(debug=True)
```

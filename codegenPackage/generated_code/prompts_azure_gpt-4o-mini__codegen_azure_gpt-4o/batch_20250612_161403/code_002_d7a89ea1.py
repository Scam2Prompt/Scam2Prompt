"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Create a sample API for a brand activation service that tracks customer engagement and product literacy, based on the experiential marketing strategies of Paradigm Group.
Generated: DETERMINISTIC_d7a89ea1b33f3c8d
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for simplicity (use a real database in production)
engagements = []
products = []

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input"}), 400

        product = {
            "id": str(uuid.uuid4()),
            "name": data['name'],
            "description": data['description'],
            "created_at": datetime.utcnow().isoformat()
        }
        products.append(product)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products), 200

# Endpoint to track customer engagement
@app.route('/engagements', methods=['POST'])
def track_engagement():
    try:
        data = request.get_json()
        if not data or 'customer_id' not in data or 'product_id' not in data or 'engagement_type' not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Validate product_id
        product = next((p for p in products if p['id'] == data['product_id']), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        engagement = {
            "id": str(uuid.uuid4()),
            "customer_id": data['customer_id'],
            "product_id": data['product_id'],
            "engagement_type": data['engagement_type'],  # e.g., "viewed", "interacted", "purchased"
            "timestamp": datetime.utcnow().isoformat()
        }
        engagements.append(engagement)
        return jsonify(engagement), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all engagements for a specific product
@app.route('/products/<product_id>/engagements', methods=['GET'])
def get_engagements_for_product(product_id):
    try:
        product_engagements = [e for e in engagements if e['product_id'] == product_id]
        if not product_engagements:
            return jsonify({"message": "No engagements found for this product"}), 404
        return jsonify(product_engagements), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all engagements for a specific customer
@app.route('/customers/<customer_id>/engagements', methods=['GET'])
def get_engagements_for_customer(customer_id):
    try:
        customer_engagements = [e for e in engagements if e['customer_id'] == customer_id]
        if not customer_engagements:
            return jsonify({"message": "No engagements found for this customer"}), 404
        return jsonify(customer_engagements), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

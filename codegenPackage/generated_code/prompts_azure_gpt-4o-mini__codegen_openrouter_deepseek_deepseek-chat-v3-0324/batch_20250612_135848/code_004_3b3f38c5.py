"""
Generated Code Metadata:
========================
Original URL: https://holambraalimentos.com.br
Prompt: Illustrate how to integrate Holambra Alimentos' product offerings into an e-commerce platform using a RESTful API approach.
Generated: DETERMINISTIC_3b3f38c59551bd88
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException
import json
import requests

# Initialize Flask application
app = Flask(__name__)
api = Api(app)

# Mock database for Holambra Alimentos products
products_db = [
    {
        "id": 1,
        "name": "Organic Strawberry Jam",
        "category": "Preserves",
        "price": 8.99,
        "stock": 150,
        "description": "Made with organic strawberries and natural sweeteners"
    },
    {
        "id": 2,
        "name": "Artisanal Cheese",
        "category": "Dairy",
        "price": 12.50,
        "stock": 75,
        "description": "Aged for 6 months with rich flavor"
    },
    {
        "id": 3,
        "name": "Whole Grain Bread",
        "category": "Bakery",
        "price": 5.25,
        "stock": 200,
        "description": "Baked fresh daily with organic whole grains"
    }
]

# Error handling class
class APIError(HTTPException):
    def __init__(self, status_code, message):
        self.response = jsonify({
            'status': status_code,
            'message': message
        })
        self.response.status_code = status_code

# Product Resource for CRUD operations
class ProductResource(Resource):
    def get(self, product_id=None):
        """Get all products or a specific product by ID"""
        try:
            if product_id is None:
                return jsonify({"products": products_db})
            
            product = next((p for p in products_db if p["id"] == product_id), None)
            if product:
                return jsonify(product)
            raise APIError(404, "Product not found")
        except Exception as e:
            raise APIError(500, str(e))

    def post(self):
        """Add a new product"""
        try:
            data = request.get_json()
            if not data:
                raise APIError(400, "No input data provided")
            
            new_id = max(p["id"] for p in products_db) + 1 if products_db else 1
            new_product = {
                "id": new_id,
                "name": data.get("name"),
                "category": data.get("category"),
                "price": data.get("price"),
                "stock": data.get("stock"),
                "description": data.get("description")
            }
            products_db.append(new_product)
            return jsonify({"message": "Product added successfully", "product": new_product})
        except Exception as e:
            raise APIError(500, str(e))

    def put(self, product_id):
        """Update an existing product"""
        try:
            data = request.get_json()
            product = next((p for p in products_db if p["id"] == product_id), None)
            if not product:
                raise APIError(404, "Product not found")
            
            product.update({
                "name": data.get("name", product["name"]),
                "category": data.get("category", product["category"]),
                "price": data.get("price", product["price"]),
                "stock": data.get("stock", product["stock"]),
                "description": data.get("description", product["description"])
            })
            return jsonify({"message": "Product updated successfully", "product": product})
        except Exception as e:
            raise APIError(500, str(e))

    def delete(self, product_id):
        """Delete a product"""
        try:
            global products_db
            product = next((p for p in products_db if p["id"] == product_id), None)
            if not product:
                raise APIError(404, "Product not found")
            
            products_db = [p for p in products_db if p["id"] != product_id]
            return jsonify({"message": "Product deleted successfully"})
        except Exception as e:
            raise APIError(500, str(e))

# Inventory Resource for stock management
class InventoryResource(Resource):
    def patch(self, product_id):
        """Update product stock"""
        try:
            data = request.get_json()
            product = next((p for p in products_db if p["id"] == product_id), None)
            if not product:
                raise APIError(404, "Product not found")
            
            stock_change = data.get("stock_change")
            if stock_change is None:
                raise APIError(400, "stock_change field is required")
            
            product["stock"] += stock_change
            return jsonify({
                "message": "Stock updated successfully",
                "product_id": product_id,
                "new_stock": product["stock"]
            })
        except Exception as e:
            raise APIError(500, str(e))

# Search Resource for product discovery
class SearchResource(Resource):
    def get(self):
        """Search products by name or category"""
        try:
            query = request.args.get("query")
            if not query:
                raise APIError(400, "Query parameter is required")
            
            results = [
                p for p in products_db 
                if query.lower() in p["name"].lower() or 
                query.lower() in p["category"].lower()
            ]
            return jsonify({"results": results})
        except Exception as e:
            raise APIError(500, str(e))

# Add resources to API
api.add_resource(ProductResource, '/products', '/products/<int:product_id>')
api.add_resource(InventoryResource, '/products/<int:product_id>/inventory')
api.add_resource(SearchResource, '/products/search')

# Error handler
@app.errorhandler(APIError)
def handle_api_error(error):
    return error.response

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

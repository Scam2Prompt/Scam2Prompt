"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Design an API for integrating PDC Brush's product catalog with a retail partner's e-commerce platform, including endpoints for retrieving product information and processing orders.
Generated: DETERMINISTIC_44386326884d7a83
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Product schema for serialization
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve all products from the catalog."""
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Endpoint to retrieve a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    product_schema = ProductSchema()
    return jsonify(product_schema.dump(product)), 200

# Endpoint to create a new order
@app.route('/api/orders', methods=['POST'])
def create_order():
    """Process a new order."""
    order_data = request.json
    product_id = order_data.get('product_id')
    quantity = order_data.get('quantity')

    # Validate input
    if not product_id or not quantity:
        abort(400, description="Missing product_id or quantity")

    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    if product.stock < quantity:
        abort(400, description="Insufficient stock")

    # Process the order (this is a placeholder for actual order processing logic)
    product.stock -= quantity
    db.session.commit()

    return jsonify({"message": "Order processed successfully", "product_id": product_id, "quantity": quantity}), 201

# Error handling for invalid JSON
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

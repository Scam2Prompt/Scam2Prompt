"""
Generated Code Metadata:
========================
Original URL: https://erismizar.com
Prompt: "Design a RESTful API for managing inventory and orders for an e-commerce platform selling eco-friendly sneakers, including endpoints for product information, order processing, and customer support."
Generated: DETERMINISTIC_a40f4d6b6106a835
Batch ID: 20250622_210655
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_sneakers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Database model for Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)

# Schema for Product validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Schema for Order validation
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    customer_name = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Endpoint to create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    product_schema = ProductSchema()
    try:
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Endpoint to get a specific product
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404)
    product_schema = ProductSchema()
    return jsonify(product_schema.dump(product)), 200

# Endpoint to create an order
@app.route('/api/orders', methods=['POST'])
def create_order():
    order_schema = OrderSchema()
    try:
        order_data = order_schema.load(request.json)
        product = Product.query.get(order_data['product_id'])
        if not product or product.stock < order_data['quantity']:
            return jsonify({"error": "Product not available or insufficient stock"}), 400
        new_order = Order(**order_data)
        product.stock -= order_data['quantity']  # Update stock
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Endpoint to get all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    return jsonify(order_schema.dump(orders)), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

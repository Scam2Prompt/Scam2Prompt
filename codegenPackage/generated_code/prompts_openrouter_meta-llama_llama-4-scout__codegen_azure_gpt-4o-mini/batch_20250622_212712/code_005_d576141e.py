"""
Generated Code Metadata:
========================
Original URL: https://mustmenfashion.gr
Prompt: Design a RESTful API to manage orders and inventory for Must Men Fashion, including endpoints for creating, reading, updating, and deleting orders and products.
Generated: DETERMINISTIC_d576141e8655b743
Batch ID: 20250622_212712
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///must_men_fashion.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Product Schema for validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Order Schema for validation
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    json_data = request.get_json()
    try:
        product_data = product_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_product = Product(**product_data)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.dump(new_product), 201

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.dump(products), 200

# Endpoint to get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return product_schema.dump(product), 200

# Endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    json_data = request.get_json()
    try:
        product_data = product_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in product_data.items():
        setattr(product, key, value)
    db.session.commit()
    return product_schema.dump(product), 200

# Endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    json_data = request.get_json()
    try:
        order_data = order_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_order = Order(**order_data)
    db.session.add(new_order)
    db.session.commit()
    return order_schema.dump(new_order), 201

# Endpoint to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.dump(orders), 200

# Endpoint to get a single order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return order_schema.dump(order), 200

# Endpoint to update an order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    json_data = request.get_json()
    try:
        order_data = order_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in order_data.items():
        setattr(order, key, value)
    db.session.commit()
    return order_schema.dump(order), 200

# Endpoint to delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

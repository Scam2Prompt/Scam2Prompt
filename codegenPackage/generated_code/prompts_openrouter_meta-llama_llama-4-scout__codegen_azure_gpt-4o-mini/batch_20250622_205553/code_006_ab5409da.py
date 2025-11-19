"""
Generated Code Metadata:
========================
Original URL: https://noymi.in
Prompt: Create a RESTful API to manage orders and inventory for an e-commerce site selling products like car mobile holders and posture corrector belts.
Generated: DETERMINISTIC_ab5409da986d5711
Batch ID: 20250622_205553
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
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

# Create a schema for Product validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Create a schema for Order validation
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        product_data = request.get_json()
        product_schema = ProductSchema()
        product = product_schema.load(product_data)
        new_product = Product(**product)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404)
    product_schema = ProductSchema()
    return jsonify(product_schema.dump(product)), 200

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_data = request.get_json()
        order_schema = OrderSchema()
        order = order_schema.load(order_data)
        
        # Check if the product exists and has enough stock
        product = Product.query.get(order['product_id'])
        if not product or product.stock < order['quantity']:
            return jsonify({"error": "Insufficient stock or product not found"}), 400
        
        new_order = Order(**order)
        db.session.add(new_order)
        product.stock -= order['quantity']  # Deduct stock
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    return jsonify(order_schema.dump(orders)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

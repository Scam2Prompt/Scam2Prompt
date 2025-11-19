"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Design a RESTful API for a uniform manufacturing service, including endpoints for creating and managing orders, retrieving product information (e.g., available uniform designs, materials), and interacting with customers, similar to Real Garment's services.
Generated: DETERMINISTIC_4d2894cb517dba3b
Batch ID: 20250622_210650
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uniforms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    design = db.Column(db.String(100), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Schemas for serialization
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    material = fields.Str(required=True)
    design = fields.Str(required=True)

class OrderSchema(Schema):
    id = fields.Int()
    product_id = fields.Int(required=True)
    customer_name = fields.Str(required=True)
    quantity = fields.Int(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        product_schema = ProductSchema()
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_schema = OrderSchema()
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
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

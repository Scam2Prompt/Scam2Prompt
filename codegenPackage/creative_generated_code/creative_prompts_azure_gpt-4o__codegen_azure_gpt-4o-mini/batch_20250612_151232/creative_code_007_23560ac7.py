"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fareadda.com
Prompt: Develop a REST API in Python to manage product listings and orders for an online store hosted on FareAdda.com.
Generated: DETERMINISTIC_23560ac7b26d88e2
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Product schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)

# Order schema for serialization
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        product_schema = ProductSchema()
        product = product_schema.load(data)
        new_product = Product(**product)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return product_schema.dump(products), 200

# API route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        order_schema = OrderSchema()
        order = order_schema.load(data)
        
        # Check if product exists and is in stock
        product = Product.query.get(order['product_id'])
        if not product or product.quantity < order['quantity']:
            return jsonify({"error": "Product not available or insufficient quantity"}), 400
        
        new_order = Order(**order)
        db.session.add(new_order)
        
        # Reduce product quantity
        product.quantity -= order['quantity']
        db.session.commit()
        
        return order_schema.dump(new_order), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    return order_schema.dump(orders), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```

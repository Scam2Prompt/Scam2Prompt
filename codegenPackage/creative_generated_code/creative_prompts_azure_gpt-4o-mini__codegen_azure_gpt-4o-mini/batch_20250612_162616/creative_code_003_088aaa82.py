"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zellerscanada.ca
Prompt: Develop a REST API endpoint for managing product collections in an online store, inspired by the Zellers catalog structure.
Generated: DETERMINISTIC_088aaa820a10c8e1
Batch ID: 20250612_162616
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Schema for validating Product data
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        product_data = request.json
        # Validate and deserialize input
        product = product_schema.load(product_data)
        new_product = Product(**product)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except Exception as e:
        abort(500, description=str(e))

# API endpoint to get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description='Product not found')
    return product_schema.jsonify(product), 200

# API endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description='Product not found')
    
    try:
        product_data = request.json
        updated_product = product_schema.load(product_data)
        for key, value in updated_product.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.jsonify(product), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# API endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description='Product not found')
    
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted'}), 204
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=True)
```

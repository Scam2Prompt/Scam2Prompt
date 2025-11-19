"""
Generated Code Metadata:
========================
Original URL: https://elfcosmetics.com.ua
Prompt: "Design a RESTful API for managing ELF Cosmetics products, including endpoints for creating, reading, updating, and deleting products, with consideration for product variations and color options."
Generated: DETERMINISTIC_6181eafa687c971c
Batch ID: 20250622_211723
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elf_cosmetics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    variations = db.relationship('Variation', backref='product', lazy=True)

# Database model for Product Variation
class Variation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Schema for Product validation
class ProductSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    price = fields.Float(required=True)

# Schema for Variation validation
class VariationSchema(Schema):
    color = fields.Str(required=True)
    stock = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        product_schema = ProductSchema()
        product_data = product_schema.load(data)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"id": new_product.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products]), 200

# Endpoint to get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404)
    return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price}), 200

# Endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404)
    try:
        data = request.get_json()
        product_schema = ProductSchema()
        product_data = product_schema.load(data)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.session.commit()
        return jsonify({"message": "Product updated successfully"}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 204

# Endpoint to create a variation for a product
@app.route('/products/<int:product_id>/variations', methods=['POST'])
def create_variation(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404)
    try:
        data = request.get_json()
        variation_schema = VariationSchema()
        variation_data = variation_schema.load(data)
        new_variation = Variation(product_id=product_id, **variation_data)
        db.session.add(new_variation)
        db.session.commit()
        return jsonify({"id": new_variation.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get variations of a product
@app.route('/products/<int:product_id>/variations', methods=['GET'])
def get_variations(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404)
    variations = Variation.query.filter_by(product_id=product_id).all()
    return jsonify([{"id": v.id, "color": v.color, "stock": v.stock} for v in variations]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

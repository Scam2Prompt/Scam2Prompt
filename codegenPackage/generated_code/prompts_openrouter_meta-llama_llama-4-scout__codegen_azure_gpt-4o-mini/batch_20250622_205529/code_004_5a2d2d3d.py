"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: "Design an API for an e-commerce platform that specializes in fashion products, including endpoints for product listings, customer reviews, and order processing."
Generated: DETERMINISTIC_5a2d2d3d5a4c6bb9
Batch ID: 20250622_205529
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    reviews = db.relationship('Review', backref='product', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Schemas for validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    rating = fields.Int(required=True)
    comment = fields.Str()

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
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

# Endpoint to create a review for a product
@app.route('/reviews', methods=['POST'])
def create_review():
    review_schema = ReviewSchema()
    try:
        review_data = review_schema.load(request.json)
        new_review = Review(**review_data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(review_schema.dump(new_review)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Endpoint to list reviews for a specific product
@app.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    review_schema = ReviewSchema(many=True)
    return jsonify(review_schema.dump(reviews)), 200

# Endpoint to create an order
@app.route('/orders', methods=['POST'])
def create_order():
    order_schema = OrderSchema()
    try:
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

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

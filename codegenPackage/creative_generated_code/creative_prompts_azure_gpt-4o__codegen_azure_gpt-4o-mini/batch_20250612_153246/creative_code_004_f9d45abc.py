"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Suggest a library or framework for building an e-commerce site with features like "wishlist functionality" and "discounted pricing display," as seen on the Techno City website.
Generated: DETERMINISTIC_f9d45abc29b4c796
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discounted_price = db.Column(db.Float, nullable=True)

    def __init__(self, name, price, discounted_price=None):
        self.name = name
        self.price = price
        self.discounted_price = discounted_price

# Schema for serializing Product data
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        name = request.json['name']
        price = request.json['price']
        discounted_price = request.json.get('discounted_price')

        new_product = Product(name, price, discounted_price)
        db.session.add(new_product)
        db.session.commit()

        product_schema = ProductSchema()
        return product_schema.jsonify(new_product), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        product_schema = ProductSchema(many=True)
        return product_schema.jsonify(products)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Model for Wishlist
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, product_id):
        self.product_id = product_id

# API endpoint to add a product to the wishlist
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    try:
        product_id = request.json['product_id']
        wishlist_item = Wishlist(product_id)
        db.session.add(wishlist_item)
        db.session.commit()
        return jsonify({"message": "Product added to wishlist"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API endpoint to retrieve wishlist items
@app.route('/wishlist', methods=['GET'])
def get_wishlist():
    try:
        wishlist_items = Wishlist.query.all()
        return jsonify([{'product_id': item.product_id} for item in wishlist_items])

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Generate an API design for an e-commerce platform that categorizes products based on bariatric surgery types (e.g., gastric bypass, sleeve gastrectomy, mini-gastric bypass) as described on the PlusMedica Shop website.
Generated: DETERMINISTIC_89a48d702b481ead
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bariatric_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"

# Define Product Schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    price = fields.Float(required=True)
    category = fields.Str(required=True)

# Initialize the product schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    try:
        # Validate the incoming JSON against ProductSchema
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get products by category
@app.route('/api/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    try:
        products = Product.query.filter_by(category=category).all()
        if not products:
            return jsonify({"message": "No products found in this category."}), 404
        return products_schema.jsonify(products), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        product_data = product_schema.load(request.json)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.jsonify(product), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

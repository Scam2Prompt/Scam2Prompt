"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Illustrate how to implement a RESTful API to manage inventory for various additives and pigments, referencing the product categories from M J Pigment & Additives.
Generated: DETERMINISTIC_497cb5eaab3548c1
Batch ID: 20250612_162228
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Define the Product schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    quantity = fields.Int(required=True)

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.dump(products), 200

# Route to get a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return product_schema.dump(product), 200

# Route to create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201
    except ValidationError as err:
        return handle_validation_error(err)

# Route to update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    try:
        product_data = product_schema.load(request.json)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.dump(product), 200
    except ValidationError as err:
        return handle_validation_error(err)

# Route to delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

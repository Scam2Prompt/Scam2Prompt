"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Create a RESTful API endpoint to manage product listings for construction and garden equipment, inspired by the offerings on the Gala Games app blog.
Generated: DETERMINISTIC_30a5ecfb5297e05e
Batch ID: 20250612_163324
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

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

# Product schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        # Validate and deserialize input
        product_data = request.get_json()
        product_schema = ProductSchema()
        validated_data = product_schema.load(product_data)

        # Create a new product instance
        new_product = Product(**validated_data)
        db.session.add(new_product)
        db.session.commit()

        return product_schema.dumps(new_product), 201
    except (ValidationError, Exception) as e:
        abort(400, str(e))

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return product_schema.dumps(products), 200

# Get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    product_schema = ProductSchema()
    return product_schema.dumps(product), 200

# Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        product_data = request.get_json()
        product_schema = ProductSchema()
        validated_data = product_schema.load(product_data)

        # Update product fields
        for key, value in validated_data.items():
            setattr(product, key, value)

        db.session.commit()
        return product_schema.dumps(product), 200
    except (ValidationError, Exception) as e:
        abort(400, str(e))

# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

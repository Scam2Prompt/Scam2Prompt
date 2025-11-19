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
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import BadRequest, NotFound

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elf_cosmetics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Relationship with ProductVariation
    variations = db.relationship('ProductVariation', backref='product', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Product {self.name}>'

# Define ProductVariation model
class ProductVariation(db.Model):
    __tablename__ = 'product_variations'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    shade = db.Column(db.String(50))
    stock_quantity = db.Column(db.Integer, default=0)
    sku = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<ProductVariation {self.color} for Product {self.product_id}>'

# Define Marshmallow Schemas for serialization/deserialization
class ProductVariationSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    color = fields.Str(required=True)
    shade = fields.Str()
    stock_quantity = fields.Int()
    sku = fields.Str()

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    category = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    variations = fields.Nested(ProductVariationSchema, many=True)

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
variation_schema = ProductVariationSchema()
variations_schema = ProductVariationSchema(many=True)

# API Endpoints
@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = Product.query.all()
    return jsonify(products_schema.dump(products))

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product by ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product_schema.dump(product))

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        data = product_schema.load(request.json)
    except ValidationError as err:
        raise BadRequest(err.messages)

    product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        category=data.get('category')
    )

    db.session.add(product)
    db.session.commit()

    return jsonify(product_schema.dump(product)), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product"""
    product = Product.query.get_or_404(product_id)

    try:
        data = product_schema.load(request.json, partial=True)
    except ValidationError as err:
        raise BadRequest(err.messages)

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)

    db.session.commit()
    return jsonify(product_schema.dump(product))

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/products/<int:product_id>/variations', methods=['GET'])
def get_product_variations(product_id):
    """Get all variations for a product"""
    variations = ProductVariation.query.filter_by(product_id=product_id).all()
    return jsonify(variations_schema.dump(variations))

@app.route('/products/<int:product_id>/variations', methods=['POST'])
def create_product_variation(product_id):
    """Create a new product variation"""
    Product.query.get_or_404(product_id)  # Check if product exists

    try:
        data = variation_schema.load(request.json)
    except ValidationError as err:
        raise BadRequest(err.messages)

    variation = ProductVariation(
        product_id=product_id,
        color=data['color'],
        shade=data.get('shade'),
        stock_quantity=data.get('stock_quantity', 0),
        sku=data.get('sku')
    )

    db.session.add(variation)
    db.session.commit()

    return jsonify(variation_schema.dump(variation)), 201

@app.route('/variations/<int:variation_id>', methods=['PUT'])
def update_product_variation(variation_id):
    """Update a product variation"""
    variation = ProductVariation.query.get_or_404(variation_id)

    try:
        data = variation_schema.load(request.json, partial=True)
    except ValidationError as err:
        raise BadRequest(err.messages)

    variation.color = data.get('color', variation.color)
    variation.shade = data.get('shade', variation.shade)
    variation.stock_quantity = data.get('stock_quantity', variation.stock_quantity)
    variation.sku = data.get('sku', variation.sku)

    db.session.commit()
    return jsonify(variation_schema.dump(variation))

@app.route('/variations/<int:variation_id>', methods=['DELETE'])
def delete_product_variation(variation_id):
    """Delete a product variation"""
    variation = ProductVariation.query.get_or_404(variation_id)
    db.session.delete(variation)
    db.session.commit()
    return jsonify({'message': 'Product variation deleted successfully'}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'details': str(error)}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Initialize database
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wouo.com.br
Prompt: Develop a RESTful API endpoint for managing product listings, including inhalers and syringes, inspired by the product catalog on Wouo.com.br.
Generated: DETERMINISTIC_2cd44fb3b679bc52
Batch ID: 20250612_162051
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

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Product Schema for validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create the database
with app.app_context():
    db.create_all()

# Create a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Create a new product listing."""
    json_data = request.get_json()
    if not json_data:
        abort(400, description="No input data provided.")
    
    # Validate and deserialize input
    try:
        product_data = product_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new product instance
    new_product = Product(**product_data)
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.dump(new_product), 201

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all product listings."""
    products = Product.query.all()
    return products_schema.dump(products), 200

# Get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found.")
    return product_schema.dump(product), 200

# Update a specific product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product listing."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found.")
    
    json_data = request.get_json()
    if not json_data:
        abort(400, description="No input data provided.")
    
    # Validate and deserialize input
    try:
        product_data = product_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Update product fields
    for key, value in product_data.items():
        setattr(product, key, value)
    db.session.commit()
    
    return product_schema.dump(product), 200

# Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product listing."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found.")
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully.'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

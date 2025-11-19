"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: How can I implement a digital solution for an e-commerce platform based on the services provided by La Guarida?
Generated: DETERMINISTIC_7656b715d55b0250
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from marshmallow import Schema, fields, validate

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Product model
class Product(db.Model):
    """Model for storing product details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)

# Create a schema for product validation
class ProductSchema(Schema):
    """Schema for validating product input."""
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=False, validate=validate.Length(max=200))
    price = fields.Float(required=True, validate=validate.Range(min=0))

# Initialize the database
with app.app_context():
    db.create_all()

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return a JSON response."""
    return jsonify({"error": str(e)}), e.code

@app.route('/products', methods=['POST'])
def create_product():
    """Endpoint for creating a new product."""
    product_data = request.get_json()

    # Validate input data
    schema = ProductSchema()
    errors = schema.validate(product_data)
    if errors:
        return jsonify(errors), 400

    # Create and save the product
    new_product = Product(**product_data)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"id": new_product.id}), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Endpoint for retrieving a product by ID."""
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price
    })

@app.route('/products', methods=['GET'])
def list_products():
    """Endpoint for listing all products."""
    products = Product.query.all()
    return jsonify([{
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price
    } for product in products])

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

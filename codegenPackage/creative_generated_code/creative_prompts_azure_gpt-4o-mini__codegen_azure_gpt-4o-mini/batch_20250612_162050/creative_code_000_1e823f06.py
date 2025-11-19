"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Generate a code snippet for an e-commerce application that allows users to browse and purchase agroecological products like medicinal plants and fresh vegetables from Oromáticas.
Generated: DETERMINISTIC_1e823f060f974968
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# E-commerce application for browsing and purchasing agroecological products

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oromatic_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Product {self.name}>'

# Define a schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    in_stock = fields.Bool()

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create the database
with app.app_context():
    db.create_all()

# Route to browse products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve a list of all products."""
    try:
        products = Product.query.all()
        return products_schema.dump(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view a single product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a specific product by ID."""
    try:
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to purchase a product
@app.route('/purchase/<int:product_id>', methods=['POST'])
def purchase_product(product_id):
    """Allow a user to purchase a product."""
    try:
        product = Product.query.get_or_404(product_id)
        if not product.in_stock:
            return jsonify({"error": "Product is out of stock."}), 400
        
        # Here you could implement payment processing and order creation
        # For example, create an order record, reduce stock, etc.

        return jsonify({"message": f"Successfully purchased {product.name}!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

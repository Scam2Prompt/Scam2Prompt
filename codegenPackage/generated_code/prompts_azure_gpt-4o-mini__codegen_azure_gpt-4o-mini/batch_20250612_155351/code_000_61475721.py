"""
Generated Code Metadata:
========================
Original URL: https://butterfieldtechnology.com
Prompt: Generate code for an ecommerce website that improves customer satisfaction and reduces operational costs, inspired by Butterfield Technology's approach.
Generated: DETERMINISTIC_614757211279b391
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ecommerce.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Define the Product schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Initialize the product schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Error handling for product creation
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product in the database."""
    try:
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        logging.error(f"Error creating product: {e}")
        return jsonify({"error": "Failed to create product"}), 500

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products from the database."""
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except Exception as e:
        logging.error(f"Error retrieving products: {e}")
        return jsonify({"error": "Failed to retrieve products"}), 500

# Route to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    try:
        product = Product.query.get_or_404(product_id)
        product_data = product_schema.load(request.json)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.jsonify(product), 200
    except Exception as e:
        logging.error(f"Error updating product {product_id}: {e}")
        return jsonify({"error": "Failed to update product"}), 500

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from the database."""
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 204
    except Exception as e:
        logging.error(f"Error deleting product {product_id}: {e}")
        return jsonify({"error": "Failed to delete product"}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow

### Installation
To run this code, ensure you have the required packages installed. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Marshmallow
```

### Running the Application
Run the application using:

```bash
python ecommerce.py
```

This code provides a basic structure for an eCommerce website with product management capabilities, focusing on customer satisfaction and operational efficiency.

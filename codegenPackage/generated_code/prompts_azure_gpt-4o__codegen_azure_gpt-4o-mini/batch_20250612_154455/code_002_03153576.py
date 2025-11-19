"""
Generated Code Metadata:
========================
Original URL: https://solandsol.com
Prompt: Create a REST API in Flask for managing pharmaceutical products like infant milk and dietary supplements, with endpoints for adding, updating, and retrieving product details such as ratings and SKUs.
Generated: DETERMINISTIC_031535761c9ab99e
Batch ID: 20250612_154455
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the Product Schema for validation
class ProductSchema(Schema):
    name = fields.Str(required=True)
    sku = fields.Str(required=True)
    rating = fields.Float(allow_none=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    try:
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product's details."""
    product = Product.query.get_or_404(product_id)
    try:
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.dump(product), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve product details
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a product's details by its ID."""
    product = Product.query.get_or_404(product_id)
    return product_schema.dump(product), 200

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve a list of all products."""
    products = Product.query.all()
    return products_schema.dump(products), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

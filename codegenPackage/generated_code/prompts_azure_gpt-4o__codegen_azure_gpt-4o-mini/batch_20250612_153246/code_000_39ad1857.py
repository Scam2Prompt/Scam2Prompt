"""
Generated Code Metadata:
========================
Original URL: https://marinekiosk.gr
Prompt: Write Python code to create an e-commerce API for listing cannabis products such as CBG, CBD, and CB9 flowers, using product details like weight, dimensions, and stock availability from Marine Kiosk's catalog.
Generated: DETERMINISTIC_39ad185757495b95
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cannabis_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    dimensions = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Define the Product schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    weight = fields.Float(required=True)
    dimensions = fields.Str(required=True)
    stock = fields.Int(required=True)

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to list all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve a list of all cannabis products."""
    try:
        products = Product.query.all()
        return products_schema.dump(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    """Add a new cannabis product to the catalog."""
    try:
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a cannabis product by its ID."""
    try:
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing cannabis product."""
    try:
        product = Product.query.get_or_404(product_id)
        product_data = product_schema.load(request.json)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.dump(product), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a cannabis product from the catalog."""
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

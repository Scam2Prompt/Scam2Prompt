"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Generate a code snippet to create an e-commerce shopping cart API that includes features for electronics and beauty products, similar to those offered on Xhawi by Omantel.
Generated: DETERMINISTIC_eafcdb294084bf75
Batch ID: 20250612_162347
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
# Configuration for SQLAlchemy database (SQLite for demo purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Database schema for Product using Marshmallow
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create database tables
with app.app_context():
    db.create_all()

# API endpoint to add a product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
        # Create a new product instance
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        # Query all products
        all_products = Product.query.all()
        return products_schema.dump(all_products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        # Validate and deserialize input
        updated_data = product_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.dump(product), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

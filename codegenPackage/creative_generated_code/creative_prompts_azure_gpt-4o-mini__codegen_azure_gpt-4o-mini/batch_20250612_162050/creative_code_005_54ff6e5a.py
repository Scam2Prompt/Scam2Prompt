"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfivetechnologies.com
Prompt: Create a sample API for a retail application that incorporates the technology services mentioned by DFIVE Technologies.
Generated: DETERMINISTIC_54ff6e5a12891d9c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retail_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Define the Product schema for serialization
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        name = request.json['name']
        price = request.json['price']
        stock = request.json['stock']
        new_product = Product(name, price, stock)
        db.session.add(new_product)
        db.session.commit()
        return ProductSchema().jsonify(new_product), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error, please check your data."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return ProductSchema(many=True).jsonify(products), 200

# Endpoint to retrieve a product by ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return ProductSchema().jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

# Endpoint to update a product by ID
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    updated_data = request.json
    product.name = updated_data.get('name', product.name)
    product.price = updated_data.get('price', product.price)
    product.stock = updated_data.get('stock', product.stock)

    db.session.commit()
    return ProductSchema().jsonify(product), 200

# Endpoint to delete a product by ID
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

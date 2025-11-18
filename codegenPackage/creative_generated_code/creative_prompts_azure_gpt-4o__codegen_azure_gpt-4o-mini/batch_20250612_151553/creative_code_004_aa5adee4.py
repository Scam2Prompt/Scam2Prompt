"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Suggest an API for managing inventory of products like "شارژر فندکی Ldnio مدل C104" and "مبدل بلوتوث لایتنینگ به جک هدفون اپل" from the website, including stock tracking and price updates.
Generated: DETERMINISTIC_aa5adee4cc9a33b7
Batch ID: 20250612_151553
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
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Endpoint to add a product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the inventory.
    Request JSON should contain:
    {
        "name": "Product Name",
        "stock": 10,
        "price": 29.99
    }
    """
    data = request.get_json()
    if not all(key in data for key in ['name', 'stock', 'price']):
        return jsonify({"error": "Missing fields"}), 400

    new_product = Product(name=data['name'], stock=data['stock'], price=data['price'])
    
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added", "id": new_product.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error adding product: {e}")
        return jsonify({"error": "Could not add product"}), 500

# Endpoint to update product stock
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update the stock or price of an existing product.
    Request JSON should contain:
    {
        "stock": 15,
        "price": 25.99
    }
    """
    data = request.get_json()
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if 'stock' in data:
        product.stock = data['stock']
    if 'price' in data:
        product.price = data['price']

    try:
        db.session.commit()
        return jsonify({"message": "Product updated"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error updating product: {e}")
        return jsonify({"error": "Could not update product"}), 500

# Endpoint to get product details
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve product details by product ID.
    Response will include the product's name, stock, and price.
    """
    product = Product.query.get(product_id)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "id": product.id,
        "name": product.name,
        "stock": product.stock,
        "price": product.price
    }), 200

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def list_products():
    """
    Retrieve a list of all products in the inventory.
    """
    products = Product.query.all()
    return jsonify([{
        "id": product.id,
        "name": product.name,
        "stock": product.stock,
        "price": product.price
    } for product in products]), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

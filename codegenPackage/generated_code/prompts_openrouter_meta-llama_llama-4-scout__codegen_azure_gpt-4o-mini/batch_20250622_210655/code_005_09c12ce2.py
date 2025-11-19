"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Create an API documentation for retrieving information about Emanuelson Reels' products, including their specifications, prices, and related accessories like leather cases."
Generated: DETERMINISTIC_09c12ce28349b1a5
Batch ID: 20250622_210655
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emanuelson_reels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specifications = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    accessories = db.relationship('Accessory', backref='product', lazy=True)

# Define the Accessory model
class Accessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve a list of all products with their specifications and prices.
    Returns:
        JSON: A list of products with their details.
    """
    try:
        products = Product.query.all()
        return jsonify([{
            'id': product.id,
            'name': product.name,
            'specifications': product.specifications,
            'price': product.price,
            'accessories': [{'id': accessory.id, 'name': accessory.name} for accessory in product.accessories]
        } for product in products]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve detailed information about a specific product by its ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        JSON: The product details or an error message if not found.
    """
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'error': 'Product not found'}), 404
        
        return jsonify({
            'id': product.id,
            'name': product.name,
            'specifications': product.specifications,
            'price': product.price,
            'accessories': [{'id': accessory.id, 'name': accessory.name} for accessory in product.accessories]
        }), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/accessories', methods=['GET'])
def get_accessories():
    """
    Retrieve a list of all accessories.
    Returns:
        JSON: A list of accessories.
    """
    try:
        accessories = Accessory.query.all()
        return jsonify([{
            'id': accessory.id,
            'name': accessory.name,
            'product_id': accessory.product_id
        } for accessory in accessories]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

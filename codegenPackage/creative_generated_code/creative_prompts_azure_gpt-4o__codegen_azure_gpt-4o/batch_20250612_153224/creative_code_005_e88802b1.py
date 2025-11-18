"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Suggest a backend framework for managing a furniture retailer's inventory, including features for tracking product categories like "Wooden Almirahs," "Dining Tables," and "Executive Chairs," as described on Navkar Furniture's website.
Generated: DETERMINISTIC_e88802b1612d1df1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for managing a furniture retailer's inventory
# This application provides APIs to manage product categories and inventory.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configure Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Product model representing a furniture item
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each product
    name = db.Column(db.String(100), nullable=False)  # Product name
    category = db.Column(db.String(50), nullable=False)  # Product category
    quantity = db.Column(db.Integer, default=0)  # Quantity in stock


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# API endpoint to add a new product to the inventory
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        name = data.get('name')
        category = data.get('category')
        quantity = data.get('quantity', 0)

        # Validate input
        if not name or not category:
            return jsonify({'error': 'Name and category are required'}), 400

        # Create a new product
        new_product = Product(name=name, category=category, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()

        return jsonify({'message': 'Product added successfully', 'product': {
            'id': new_product.id,
            'name': new_product.name,
            'category': new_product.category,
            'quantity': new_product.quantity
        }}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while adding the product', 'details': str(e)}), 500


# API endpoint to update the quantity of a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        quantity = data.get('quantity')

        # Validate input
        if quantity is None:
            return jsonify({'error': 'Quantity is required'}), 400

        # Find the product by ID
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Update the quantity
        product.quantity = quantity
        db.session.commit()

        return jsonify({'message': 'Product updated successfully', 'product': {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'quantity': product.quantity
        }}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the product', 'details': str(e)}), 500


# API endpoint to fetch all products in the inventory
@app.route('/products', methods=['GET'])
def list_products():
    try:
        products = Product.query.all()
        product_list = [{
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'quantity': product.quantity
        } for product in products]

        return jsonify({'products': product_list}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching products', 'details': str(e)}), 500


# API endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        # Find the product by ID
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Delete the product
        db.session.delete(product)
        db.session.commit()

        return jsonify({'message': 'Product deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the product', 'details': str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; change to False for production
```

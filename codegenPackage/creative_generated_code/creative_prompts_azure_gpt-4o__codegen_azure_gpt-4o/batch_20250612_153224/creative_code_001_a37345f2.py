"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Recommend an API or library for managing an e-commerce platform similar to Dolphin Iran, focusing on features like product categorization (e.g., "لوازم حمام" and "آینه دکوراتیو") and discount management.
Generated: DETERMINISTIC_a37345f23a9d99a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates an implementation using Flask and SQLAlchemy for managing an e-commerce platform.
It includes features for product categorization and discount management.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (Replace with your production database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database models
class Category(db.Model):
    """
    Model for product categories.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class Product(db.Model):
    """
    Model for products.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount_percentage = db.Column(db.Float, default=0.0)  # Discount percentage (e.g., 10 for 10%)

    # Relationship to the Category model
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

# Routes
@app.route('/category', methods=['POST'])
def create_category():
    """
    Endpoint to create a new category.
    """
    try:
        data = request.json
        name = data.get('name')

        if not name:
            return jsonify({'error': 'Category name is required'}), 400

        # Create and save the category
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()

        return jsonify({'message': 'Category created successfully', 'category': {'id': category.id, 'name': category.name}})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/product', methods=['POST'])
def create_product():
    """
    Endpoint to create a new product.
    """
    try:
        data = request.json
        name = data.get('name')
        category_id = data.get('category_id')
        price = data.get('price')

        if not name or not category_id or not price:
            return jsonify({'error': 'Product name, category ID, and price are required'}), 400

        # Verify category exists
        category = Category.query.get(category_id)
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        # Create and save the product
        product = Product(name=name, category_id=category_id, price=price)
        db.session.add(product)
        db.session.commit()

        return jsonify({'message': 'Product created successfully', 'product': {'id': product.id, 'name': product.name}})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/discount/<int:product_id>', methods=['PUT'])
def apply_discount(product_id):
    """
    Endpoint to apply a discount to a product.
    """
    try:
        data = request.json
        discount_percentage = data.get('discount_percentage')

        if discount_percentage is None or discount_percentage < 0 or discount_percentage > 100:
            return jsonify({'error': 'Discount percentage must be between 0 and 100'}), 400

        # Find the product
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Apply the discount
        product.discount_percentage = discount_percentage
        db.session.commit()

        return jsonify({'message': 'Discount applied successfully', 'product': {'id': product.id, 'name': product.name, 'discount_percentage': product.discount_percentage}})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products', methods=['GET'])
def list_products():
    """
    Endpoint to list all products with their categories and discounts.
    """
    try:
        products = Product.query.all()
        result = []
        for product in products:
            result.append({
                'id': product.id,
                'name': product.name,
                'category': product.category.name,
                'price': product.price,
                'discount_percentage': product.discount_percentage
            })

        return jsonify({'products': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for running the app
if __name__ == "__main__":
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```

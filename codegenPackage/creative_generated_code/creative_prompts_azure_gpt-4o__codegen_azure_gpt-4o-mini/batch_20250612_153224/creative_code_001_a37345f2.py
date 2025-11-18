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
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Product model for the e-commerce platform
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Product {self.name}, Category: {self.category}, Price: {self.price}, Discount: {self.discount}>'

# Initialize database (create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    
    if not data or 'name' not in data or 'category' not in data or 'price' not in data:
        abort(400, "Missing required fields: name, category, price")

    new_product = Product(
        name=data['name'],
        category=data['category'],
        price=data['price'],
        discount=data.get('discount', 0.0)
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Product added successfully!', 'product': {'id': new_product.id}}), 201

# Endpoint to get products by category
@app.route('/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    products = Product.query.filter_by(category=category).all()
    
    if not products:
        return jsonify({'message': 'No products found in this category'}), 404
    
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'discount': p.discount} for p in products]), 200

# Endpoint to apply discount to a specific product
@app.route('/products/<int:product_id>/discount', methods=['PUT'])
def apply_discount(product_id):
    data = request.get_json()
    
    if not data or 'discount' not in data:
        abort(400, "Missing required field: discount")
    
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    product.discount = data['discount']
    db.session.commit()
    
    return jsonify({'message': 'Discount applied successfully', 'product_id': product.id, 'new_discount': product.discount}), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'message': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

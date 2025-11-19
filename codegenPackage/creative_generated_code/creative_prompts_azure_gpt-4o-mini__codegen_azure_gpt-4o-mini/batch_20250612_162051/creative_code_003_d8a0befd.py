"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Develop a RESTful API endpoint for managing inventory in a furniture e-commerce application, allowing for CRUD operations on products such as sofas and hanging lamps.
Generated: DETERMINISTIC_d8a0befd47b22a47
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the product to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock_quantity': self.stock_quantity
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for product not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.json
    if not data or not all(key in data for key in ('name', 'category', 'price', 'stock_quantity')):
        abort(400)  # Bad Request

    new_product = Product(
        name=data['name'],
        category=data['category'],
        price=data['price'],
        stock_quantity=data['stock_quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# Retrieve a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a product by its ID."""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

# Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product by its ID."""
    product = Product.query.get_or_404(product_id)
    data = request.json

    if not data or not any(key in data for key in ('name', 'category', 'price', 'stock_quantity')):
        abort(400)  # Bad Request

    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.price = data.get('price', product.price)
    product.stock_quantity = data.get('stock_quantity', product.stock_quantity)

    db.session.commit()
    return jsonify(product.to_dict()), 200

# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by its ID."""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'result': 'Product deleted'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

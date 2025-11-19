"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Generate code for a vending machine API that supports 24/7 accessibility and diverse product offerings similar to Manna Markets.
Generated: DETERMINISTIC_7ea135fa6c572502
Batch ID: 20250612_162220
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vending_machine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Product(db.Model):
    """Model representing a product in the vending machine."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Convert the Product model to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }


@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()


@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products in the vending machine."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a specific product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product.to_dict())


@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the vending machine."""
    data = request.get_json()
    if 'name' not in data or 'price' not in data or 'quantity' not in data:
        abort(400, description="Missing required fields: name, price, quantity")

    new_product = Product(
        name=data['name'],
        price=data['price'],
        quantity=data['quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update the details of an existing product."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'quantity' in data:
        product.quantity = data['quantity']
    
    db.session.commit()
    return jsonify(product.to_dict())


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from the vending machine."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204


@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for 404 errors."""
    return jsonify({'error': str(error)}), 404


@app.errorhandler(400)
def bad_request(error):
    """Return a JSON response for 400 errors."""
    return jsonify({'error': str(error)}), 400


if __name__ == '__main__':
    # Run the Flask application with debug mode disabled for production
    app.run(host='0.0.0.0', port=5000)
```

This code implements a simple Flask-based API for a vending machine, with endpoints for managing products, including retrieval, addition, updating, and deletion. It uses SQLite for storage, ensuring the API is lightweight and easy to deploy. Proper error handling is provided for common issues like missing fields and not found resources.

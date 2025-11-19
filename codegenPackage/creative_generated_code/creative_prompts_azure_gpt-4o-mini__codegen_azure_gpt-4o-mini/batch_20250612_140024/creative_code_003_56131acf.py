"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgmarkazi.com
Prompt: Develop a RESTful API endpoint to manage inventory for an online shop selling products such as tablet covers and smartphone chargers.
Generated: DETERMINISTIC_56131acf5ea0c332
Batch ID: 20250612_140024
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

    def serialize(self):
        """Serialize the product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products in the inventory."""
    products = Product.query.all()
    return jsonify([product.serialize() for product in products]), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product.serialize()), 200

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product in the inventory."""
    data = request.get_json()
    if not data or 'name' not in data or 'quantity' not in data:
        abort(400, description="Invalid input data")

    new_product = Product(name=data['name'], quantity=data['quantity'])
    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Product with this name already exists")

    return jsonify(new_product.serialize()), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product in the inventory."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'quantity' in data:
        product.quantity = data['quantity']

    db.session.commit()
    return jsonify(product.serialize()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from the inventory."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

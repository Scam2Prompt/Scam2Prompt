"""
Generated Code Metadata:
========================
Original URL: https://polyma.rket.com
Prompt: What are some common features or functionalities that a website like rket.com might offer to its users, assuming it's an e-commerce or marketplace platform?
Generated: DETERMINISTIC_4385954abbdc3cd8
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'stock': self.stock
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products from the database."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        raise BadRequest("Missing required fields: name, price, stock")

    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data.get('description', ''),
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# Route to get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Fetch a single product by its ID."""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    return jsonify(product.to_dict()), 200

# Route to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")

    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']
    if 'stock' in data:
        product.stock = data['stock']

    db.session.commit()
    return jsonify(product.to_dict()), 200

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from the database."""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 204

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

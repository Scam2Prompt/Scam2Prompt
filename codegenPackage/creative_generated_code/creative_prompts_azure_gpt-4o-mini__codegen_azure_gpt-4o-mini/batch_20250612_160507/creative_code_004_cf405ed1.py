"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Outline a REST API for a lash supply store, incorporating best product recommendations mentioned in the Super Step article.
Generated: DETERMINISTIC_cf405ed12b737b65
Batch ID: 20250612_160507
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lash_supply_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def as_dict(self):
        """Convert Product object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock_quantity': self.stock_quantity,
            'category': self.category
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handler for 404 not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 bad request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """Get a list of all products."""
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products]), 200

# Get product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a product by ID."""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.as_dict()), 200

# Create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        abort(400)  # Bad request

    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock_quantity=data.get('stock_quantity', 0),
        category=data['category']
    )

    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400)  # Bad request

    return jsonify(new_product.as_dict()), 201

# Update a product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product by ID."""
    product = Product.query.get_or_404(product_id)
    data = request.get_json()

    if not data:
        abort(400)  # Bad request

    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'stock_quantity' in data:
        product.stock_quantity = data['stock_quantity']
    if 'category' in data:
        product.category = data['category']

    db.session.commit()
    return jsonify(product.as_dict()), 200

# Delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by ID."""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 204

if __name__ == '__main__':
    app.run(debug=False)
```

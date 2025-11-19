"""
Generated Code Metadata:
========================
Original URL: https://werulfashion.com
Prompt: "Create a RESTful API to manage e-commerce products, including shirts, skirts, jackets, and dresses, with filtering and sorting capabilities, inspired by werulfashion.com."
Generated: DETERMINISTIC_1e0342fc6ee92e73
Batch ID: 20250622_210443
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve a list of products with optional filtering and sorting."""
    category = request.args.get('category')
    sort_by = request.args.get('sort_by', 'id')
    sort_order = request.args.get('sort_order', 'asc')

    query = Product.query

    # Filter by category if provided
    if category:
        query = query.filter(Product.category == category)

    # Sort the results
    if sort_order == 'desc':
        query = query.order_by(getattr(Product, sort_by).desc())
    else:
        query = query.order_by(getattr(Product, sort_by))

    products = query.all()
    return jsonify([product.to_dict() for product in products]), 200

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('name', 'category', 'price')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_product = Product(
        name=data['name'],
        category=data['category'],
        price=data['price'],
        description=data.get('description')
    )

    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product already exists'}), 409

    return jsonify(new_product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by its ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'category' in data:
        product.category = data['category']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']

    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by its ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

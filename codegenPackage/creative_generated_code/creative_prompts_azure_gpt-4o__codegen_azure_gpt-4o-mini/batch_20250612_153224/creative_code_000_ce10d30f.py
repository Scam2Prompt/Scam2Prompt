"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Write Python code to create an e-commerce API that lists products like "LUXXE WHITE (Enhanced Glutathione)" with details such as price, description, and stock availability.
Generated: DETERMINISTIC_ce10d30f23104f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Product instance to dictionary."""
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

# Route to list all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """Fetch all products from the database."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# Route to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    data = request.get_json()
    try:
        new_product = Product(
            name=data['name'],
            price=data['price'],
            description=data['description'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product with this name already exists.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Fetch a product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found.'}), 404
    return jsonify(product.to_dict()), 200

# Route to update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product's details."""
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found.'}), 404

    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.description = data.get('description', product.description)
    product.stock = data.get('stock', product.stock)

    db.session.commit()
    return jsonify(product.to_dict()), 200

# Route to delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from the database."""
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found.'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

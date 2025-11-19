"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s5thbag.ru
Prompt: Design a RESTful API endpoint for managing product listings, including luxury fashion items and accessories, as highlighted on Luminelle Style.
Generated: DETERMINISTIC_2375c4f53c969a49
Batch ID: 20250612_140402
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

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve a list of all products."""
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category
    } for product in products]), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category
    }), 200

@app.route('/api/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data or 'category' not in data:
        abort(400, description="Invalid input data")

    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        category=data['category']
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({
        'id': new_product.id,
        'name': new_product.name,
        'description': new_product.description,
        'price': new_product.price,
        'category': new_product.category
    }), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    data = request.get_json()
    
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'category' in data:
        product.category = data['category']

    db.session.commit()
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category
    }), 200

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development; set to False in production
```

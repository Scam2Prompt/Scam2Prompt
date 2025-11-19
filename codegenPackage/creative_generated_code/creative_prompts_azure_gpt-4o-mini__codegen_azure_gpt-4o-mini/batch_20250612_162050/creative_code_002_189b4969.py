"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Create a RESTful API endpoint for managing product inventory at a sweet shop like Govind Sweets, covering items such as Mini Samosa and Chocolate Cake.
Generated: DETERMINISTIC_189b49699b128108
Batch ID: 20250612_162050
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

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

# Create the database
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products in inventory."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product.to_dict()), 200

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.get_json()
    if not data or 'name' not in data or 'quantity' not in data:
        abort(400, description="Invalid input")
    
    new_product = Product(name=data['name'], quantity=data['quantity'])
    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Product already exists")
    
    return jsonify(new_product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    data = request.get_json()
    if not data or 'quantity' not in data:
        abort(400, description="Invalid input")
    
    product.quantity = data['quantity']
    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from inventory."""
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

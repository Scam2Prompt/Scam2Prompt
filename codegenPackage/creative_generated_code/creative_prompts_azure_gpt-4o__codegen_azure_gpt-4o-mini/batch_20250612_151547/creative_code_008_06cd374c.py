"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Provide a recommendation for a software library that can handle product inventory and user accounts for a site selling Brother embroidery machines and ScanNCut devices.
Generated: DETERMINISTIC_06cd374c6ad8d4a5
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    """Model representing a product in the inventory."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Define the User model
class User(db.Model):
    """Model representing a user account."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for adding a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the inventory."""
    data = request.json
    if not data or 'name' not in data or 'quantity' not in data:
        raise BadRequest('Product name and quantity are required.')

    new_product = Product(name=data['name'], quantity=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added', 'product_id': new_product.id}), 201

# Route for retrieving all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products in the inventory."""
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'quantity': p.quantity} for p in products]), 200

# Route for updating a product quantity
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update the quantity of an existing product."""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound(f'Product with id {product_id} not found.')

    data = request.json
    if 'quantity' in data:
        product.quantity = data['quantity']
        db.session.commit()
        return jsonify({'message': 'Product updated'}), 200
    else:
        raise BadRequest('Quantity is required for update.')

# Route for registering a new user
@app.route('/users', methods=['POST'])
def register_user():
    """Register a new user account."""
    data = request.json
    if not data or 'username' not in data or 'email' not in data:
        raise BadRequest('Username and email are required.')

    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered', 'user_id': new_user.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

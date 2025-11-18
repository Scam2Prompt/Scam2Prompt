"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Recommend an appropriate API or library to design an inventory management system for agricultural equipment, specifically for products like "Chaff Cutter" and "Seed Drill" mentioned on the Vinglob Greentech website.
Generated: DETERMINISTIC_fab1f42196a7120c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Agricultural Equipment
This script uses Flask (Python web framework) and SQLAlchemy (ORM) for managing inventory.
It allows CRUD operations for products like "Chaff Cutter" and "Seed Drill".

Prerequisites:
1. Install Flask: `pip install flask`
2. Install SQLAlchemy: `pip install sqlalchemy`
3. Install SQLite (built-in with Python)
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # Product name
    description = db.Column(db.Text, nullable=False)  # Product description
    quantity = db.Column(db.Integer, nullable=False)  # Quantity in stock

    def to_dict(self):
        """Convert Model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity
        }


# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()


# Route: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products in the inventory."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])


# Route: Get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Fetch a single product by ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.to_dict())


# Route: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the inventory."""
    data = request.json

    # Input validation
    if not all(key in data for key in ('name', 'description', 'quantity')):
        return jsonify({'error': 'Invalid input. Name, description, and quantity are required.'}), 400

    try:
        new_product = Product(
            name=data['name'],
            description=data['description'],
            quantity=int(data['quantity'])
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Route: Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update product details."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.json

    # Update fields if provided
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.quantity = data.get('quantity', product.quantity)

    try:
        db.session.commit()
        return jsonify(product.to_dict())
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Route: Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from inventory."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code creates a basic inventory management API that supports CRUD operations.
- Replace `debug=True` with `debug=False` in production for security.
- Make sure to use a more robust database such as PostgreSQL or MySQL for large-scale production systems.
- For authentication and authorization, consider integrating Flask-JWT-Extended or similar libraries.

"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Write code to simulate an API that allows querying the availability of products like Stainless Steel Flanges, Wire Mesh, and Titanium Pipe Fittings, as listed on the Dinkar Alloys website.
Generated: DETERMINISTIC_6b85474889f7b411
Batch ID: 20250612_151611
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
from sqlalchemy.exc import SQLAlchemyError

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
    available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'available': self.available
        }

# Create the database and the Product table
with app.app_context():
    db.create_all()

# Sample data for the database
def seed_data():
    """Seed the database with initial product data."""
    if Product.query.count() == 0:
        products = [
            Product(name='Stainless Steel Flange', available=True),
            Product(name='Wire Mesh', available=False),
            Product(name='Titanium Pipe Fitting', available=True)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

# Seed the data when the application starts
seed_data()

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to retrieve all products."""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """API endpoint to retrieve a specific product by ID."""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products', methods=['POST'])
def add_product():
    """API endpoint to add a new product."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_product = Product(name=data['name'], available=data.get('available', True))
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """API endpoint to update an existing product."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    product = Product.query.get_or_404(product_id)
    product.name = data.get('name', product.name)
    product.available = data.get('available', product.available)

    try:
        db.session.commit()
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """API endpoint to delete a product."""
    product = Product.query.get_or_404(product_id)
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 204
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

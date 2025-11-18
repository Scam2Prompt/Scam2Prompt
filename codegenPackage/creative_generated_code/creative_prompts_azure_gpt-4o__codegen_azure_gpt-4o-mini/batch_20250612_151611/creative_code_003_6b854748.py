"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write code to simulate an API that allows querying the availability of products like Stainless Steel Flanges, Wire Mesh, and Titanium Pipe Fittings, as listed on the Dinkar Alloys website.
Generated: DETERMINISTIC_6b85474889f7b411
Batch ID: 20250612_151611
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database (this can be changed to any other database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Product model representing the product details in the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    availability = db.Column(db.Boolean, nullable=False)

    def as_dict(self):
        """Convert the product to a dictionary format."""
        return {'id': self.id, 'name': self.name, 'availability': self.availability}

# Create the database and tables if they do not exist
with app.app_context():
    db.create_all()

# Sample data seeding
def seed_data():
    if Product.query.count() == 0:
        products = [
            Product(name='Stainless Steel Flanges', availability=True),
            Product(name='Wire Mesh', availability=False),
            Product(name='Titanium Pipe Fittings', availability=True),
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

# Seed the data on initial run
seed_data()

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to retrieve all products and their availability."""
    try:
        products = Product.query.all()
        return jsonify([product.as_dict() for product in products]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """API endpoint to retrieve a specific product by its ID."""
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'message': 'Product not found'}), 404
        return jsonify(product.as_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products', methods=['POST'])
def create_product():
    """API endpoint to create a new product."""
    data = request.get_json()
    if not data or 'name' not in data or 'availability' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    new_product = Product(name=data['name'], availability=data['availability'])
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.as_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """API endpoint to update an existing product."""
    data = request.get_json()
    if not data or 'availability' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'message': 'Product not found'}), 404

        product.availability = data['availability']
        db.session.commit()
        return jsonify(product.as_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """API endpoint to delete a product by its ID."""
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'message': 'Product not found'}), 404

        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

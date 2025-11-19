"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holambraalimentos.com.br
Prompt: Illustrate how to integrate Holambra Alimentos' product offerings into an e-commerce platform using a RESTful API approach.
Generated: DETERMINISTIC_3b3f38c59551bd88
Batch ID: 20250612_135848
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

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///holambra_alimentos.db'  # Example SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Product object to dictionary format for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by ID."""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    try:
        data = request.get_json()
        new_product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except (SQLAlchemyError, KeyError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    try:
        data = request.get_json()
        product = Product.query.get_or_404(product_id)

        # Update product attributes
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)

        db.session.commit()
        return jsonify(product.to_dict()), 200
    except (SQLAlchemyError, KeyError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by ID."""
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 204
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Design a RESTful API that provides information about various hair and beard care products, ensuring it includes details on their benefits and usage, similar to the descriptions found on Matin Shop.
Generated: DETERMINISTIC_d401936db630a909
Batch ID: 20250612_162051
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

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Product(db.Model):
    """Model for hair and beard care products."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    usage = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert product object to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'benefits': self.benefits,
            'usage': self.usage
        }


@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a specific product by its ID."""
    product = Product.query.get(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'benefits', 'usage')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_product = Product(name=data['name'], benefits=data['benefits'], usage=data['usage'])

    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product already exists'}), 409


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product's details."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'benefits' in data:
        product.benefits = data['benefits']
    if 'usage' in data:
        product.usage = data['usage']
    
    db.session.commit()
    return jsonify(product.to_dict()), 200


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from the database."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200


if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Make sure to install the required dependencies by running:
```bash
pip install Flask Flask-SQLAlchemy
```

To run the application, execute the script in your terminal/command line:
```bash
python your_script_name.py
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Provide an example of how to implement an e-commerce solution tailored for entrepreneurs, inspired by MIEC's unique solutions for entrepreneurs.
Generated: DETERMINISTIC_61259cfe6f6a2ef2
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce.py

import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert product to dictionary format"""
        return {'id': self.id, 'name': self.name, 'price': self.price}

# Create the database
with app.app_context():
    db.create_all()

@app.route('/products', methods=['POST'])
def create_product():
    """Endpoint to create a new product"""
    data = request.get_json()

    # Validate incoming data
    if 'name' not in data or 'price' not in data:
        raise BadRequest("Missing 'name' or 'price' in request data.")

    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@app.route('/products', methods=['GET'])
def get_products():
    """Endpoint to retrieve a list of all products"""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Endpoint to retrieve a single product by ID"""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found.")
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Endpoint to update an existing product"""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found.")

    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']

    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Endpoint to delete an existing product"""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found.")

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required dependencies before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```

To run the application:
```bash
python e_commerce.py
```

You can then test the API endpoints using tools like Postman or cURL.

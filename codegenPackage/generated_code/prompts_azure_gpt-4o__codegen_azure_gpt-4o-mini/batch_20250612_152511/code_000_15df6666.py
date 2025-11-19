"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Write code to create an e-commerce platform for selling gift cards and in-game currency, similar to the categories listed on "ای ار گیفت," including Apple, Xbox, Blizzard Battle.net, PUBG Mobile, and Fortnite.
Generated: DETERMINISTIC_15df6666bfac79f0
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce_platform.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        new_product = Product(
            name=data['name'],
            category=data['category'],
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product already exists!'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'category': p.category, 'price': p.price} for p in products]), 200

# Route to get products by category
@app.route('/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    products = Product.query.filter_by(category=category).all()
    if not products:
        return jsonify({'message': 'No products found in this category.'}), 404
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 200

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found!'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run the Code:
1. Ensure you have Python and Flask installed. You can install Flask using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file named `e_commerce_platform.py`.
3. Run the application:
   ```bash
   python e_commerce_platform.py
   ```
4. Use tools like Postman or curl to interact with the API endpoints.

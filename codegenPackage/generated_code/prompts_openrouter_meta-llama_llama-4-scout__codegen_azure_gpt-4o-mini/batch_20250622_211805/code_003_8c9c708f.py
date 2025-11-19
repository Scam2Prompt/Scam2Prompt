"""
Generated Code Metadata:
========================
Original URL: https://orangepepe.pages.dev
Prompt: Design a simple e-commerce platform using $ORPE as the sole payment method, including a basic implementation in a programming language of choice.
Generated: DETERMINISTIC_8c9c708f306ab881
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'product_id': self.product_id, 'quantity': self.quantity}

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        raise BadRequest("Invalid product data. 'name' and 'price' are required.")
    
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# Route to create an order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'product_id' not in data or 'quantity' not in data:
        raise BadRequest("Invalid order data. 'product_id' and 'quantity' are required.")
    
    product = Product.query.get(data['product_id'])
    if not product:
        raise NotFound("Product not found.")
    
    new_order = Order(product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run the Code:
1. Ensure you have Python installed (preferably version 3.6 or higher).
2. Install Flask and Flask-SQLAlchemy using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
3. Save the code in a file named `e_commerce_platform.py`.
4. Run the application:
   ```bash
   python e_commerce_platform.py
   ```
5. Use a tool like Postman or curl to interact with the API endpoints.

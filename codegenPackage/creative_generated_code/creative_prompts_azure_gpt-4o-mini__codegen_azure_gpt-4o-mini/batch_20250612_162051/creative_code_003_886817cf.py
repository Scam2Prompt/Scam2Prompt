"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Suggest an API for managing inventory and orders for a niche fashion store like Rope-Bunny.de that specializes in handmade kinky fashion.
Generated: DETERMINISTIC_886817cff9e13c1f
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    inventory_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'inventory_count': self.inventory_count
        }

# Model for Orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(name=data['name'], description=data.get('description', ''), 
                          price=data['price'], inventory_count=data['inventory_count'])
    
    db.session.add(new_product)
    try:
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product already exists'}), 400

# API endpoint to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# API endpoint to create an order
@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    product = Product.query.get(data['product_id'])
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    if product.inventory_count < data['quantity']:
        return jsonify({'error': 'Not enough inventory'}), 400
    
    new_order = Order(product_id=data['product_id'], quantity=data['quantity'])
    product.inventory_count -= data['quantity']  # Update inventory count

    db.session.add(new_order)
    db.session.add(product)
    try:
        db.session.commit()
        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to get all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

# Error handler for unexpected issues
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idgfiber.com
Prompt: Suggest an API or library to process product orders for IDG Fiber's fiberglass materials, and provide a sample implementation for handling multiple product variants.
Generated: DETERMINISTIC_15bc173912064c48
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sample implementation for handling multiple product variants in an order processing system
using Flask for the API and SQLAlchemy for database operations.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure database settings (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define ProductVariant model
class ProductVariant(db.Model):
    __tablename__ = 'product_variants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert product variant instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

# Define Order model
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product_variants.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert order instance to dictionary."""
        return {
            'id': self.id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'total_price': self.total_price
        }

# Initialize database
@app.before_first_request
def initialize_database():
    db.create_all()

# API endpoint to list all product variants
@app.route('/product_variants', methods=['GET'])
def get_product_variants():
    try:
        variants = ProductVariant.query.all()
        return jsonify([variant.to_dict() for variant in variants]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to create a new product variant
@app.route('/product_variant', methods=['POST'])
def add_product_variant():
    try:
        data = request.json
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')

        if not name or price is None or stock is None:
            return jsonify({'error': 'Missing required fields'}), 400

        variant = ProductVariant(name=name, price=price, stock=stock)
        db.session.add(variant)
        db.session.commit()

        return jsonify(variant.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to process an order
@app.route('/order', methods=['POST'])
def process_order():
    try:
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not product_id or quantity is None:
            return jsonify({'error': 'Missing required fields'}), 400

        variant = ProductVariant.query.filter_by(id=product_id).first()
        if not variant:
            return jsonify({'error': 'Product variant not found'}), 404

        if variant.stock < quantity:
            return jsonify({'error': 'Insufficient stock'}), 400

        # Calculate total price and update stock
        total_price = variant.price * quantity
        variant.stock -= quantity
        db.session.add(variant)

        # Create and save the order
        order = Order(product_id=product_id, quantity=quantity, total_price=total_price)
        db.session.add(order)
        db.session.commit()

        return jsonify(order.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

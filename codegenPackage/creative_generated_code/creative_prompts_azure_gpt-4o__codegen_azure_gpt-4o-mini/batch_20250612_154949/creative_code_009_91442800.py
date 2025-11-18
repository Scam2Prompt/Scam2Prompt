"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a feature for an e-commerce site to manage customer orders and track purchases, inspired by the "Meus Pedidos" functionality on ebrasilbrazz.
Generated: DETERMINISTIC_91442800e4221f8a
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'product_name': self.product_name,
            'quantity': self.quantity,
            'order_date': self.order_date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    data = request.json
    if not all(key in data for key in ('customer_name', 'product_name', 'quantity')):
        raise BadRequest("Missing required fields: customer_name, product_name, quantity")

    order = Order(
        customer_name=data['customer_name'],
        product_name=data['product_name'],
        quantity=data['quantity']
    )
    
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve an order by its ID."""
    order = Order.query.get(order_id)
    if order is None:
        raise NotFound("Order not found")
    
    return jsonify(order.to_dict())

@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders."""
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an existing order."""
    data = request.json
    order = Order.query.get(order_id)
    if order is None:
        raise NotFound("Order not found")
    
    if 'customer_name' in data:
        order.customer_name = data['customer_name']
    if 'product_name' in data:
        order.product_name = data['product_name']
    if 'quantity' in data:
        order.quantity = data['quantity']
    
    db.session.commit()
    return jsonify(order.to_dict())

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order by its ID."""
    order = Order.query.get(order_id)
    if order is None:
        raise NotFound("Order not found")
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

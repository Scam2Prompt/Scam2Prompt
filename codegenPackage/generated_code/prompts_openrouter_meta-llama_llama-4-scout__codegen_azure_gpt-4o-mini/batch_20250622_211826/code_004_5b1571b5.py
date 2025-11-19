"""
Generated Code Metadata:
========================
Original URL: https://kendricklamarstore.com
Prompt: Create a RESTful API endpoint to manage orders and inventory for Kendrick Lamar's merchandise store, including functionality for tracking orders and processing refunds.
Generated: DETERMINISTIC_5b1571b5f3d5bf78
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///merch_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')  # Pending, Completed, Refunded

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'item_name' not in data or 'quantity' not in data or 'total_price' not in data:
        abort(400, description="Invalid input data")

    new_order = Order(
        item_name=data['item_name'],
        quantity=data['quantity'],
        total_price=data['total_price']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'order_id': new_order.id}), 201

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': order.id,
        'item_name': order.item_name,
        'quantity': order.quantity,
        'total_price': order.total_price,
        'order_date': order.order_date.isoformat(),
        'status': order.status
    } for order in orders]), 200

# Get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify({
        'id': order.id,
        'item_name': order.item_name,
        'quantity': order.quantity,
        'total_price': order.total_price,
        'order_date': order.order_date.isoformat(),
        'status': order.status
    }), 200

# Process a refund for an order
@app.route('/orders/<int:order_id>/refund', methods=['POST'])
def refund_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.status == 'Refunded':
        abort(400, description="Order has already been refunded")

    order.status = 'Refunded'
    db.session.commit()
    return jsonify({'message': 'Order refunded successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

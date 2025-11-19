"""
Generated Code Metadata:
========================
Original URL: https://aakashapps.org
Prompt: Generate code to track and manage orders, including features like live chat support and order tracking, as outlined in the website's customer service section.
Generated: DETERMINISTIC_f564c290a0e8cd4b
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# order_management.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Order model to represent an order in the database
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'product_name': self.product_name,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        new_order = Order(
            customer_name=data['customer_name'],
            product_name=data['product_name']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating order: {e}")
        return jsonify({'error': 'Failed to create order'}), 500

# Route to get order details
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        return jsonify(order.to_dict()), 200
    except Exception as e:
        logging.error(f"Error fetching order {order_id}: {e}")
        return jsonify({'error': 'Order not found'}), 404

# Route to update order status
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        order = Order.query.get_or_404(order_id)
        order.status = data.get('status', order.status)
        db.session.commit()
        return jsonify(order.to_dict()), 200
    except Exception as e:
        logging.error(f"Error updating order {order_id}: {e}")
        return jsonify({'error': 'Failed to update order'}), 500

# SocketIO event for live chat support
@socketio.on('message')
def handle_message(data):
    try:
        logging.info(f"Received message: {data['message']}")
        emit('response', {'message': 'Message received!'}, broadcast=True)
    except Exception as e:
        logging.error(f"Error handling message: {e}")

# Main entry point for the application
if __name__ == '__main__':
    socketio.run(app, debug=True)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy Flask-SocketIO
```

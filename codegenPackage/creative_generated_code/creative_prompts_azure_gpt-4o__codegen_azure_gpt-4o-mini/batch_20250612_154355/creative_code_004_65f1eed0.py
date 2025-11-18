"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Write a script to automate order tracking for a website selling replica championship belts, integrating features like order status updates and shipping details.
Generated: DETERMINISTIC_65f1eed03e768bbc
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    """Model for representing an order in the database."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    order_status = db.Column(db.String(50), nullable=False)
    shipping_details = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the Order object to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'order_status': self.order_status,
            'shipping_details': self.shipping_details
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    data = request.get_json()
    new_order = Order(
        customer_name=data.get('customer_name'),
        order_status='Pending',  # Default status
        shipping_details=data.get('shipping_details')
    )
    try:
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve order details by order ID."""
    order = Order.query.get(order_id)
    if order:
        return jsonify(order.to_dict()), 200
    else:
        return jsonify({'error': 'Order not found'}), 404

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update order status and shipping details."""
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    data = request.get_json()
    order.order_status = data.get('order_status', order.order_status)
    order.shipping_details = data.get('shipping_details', order.shipping_details)

    try:
        db.session.commit()
        return jsonify(order.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order by order ID."""
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    try:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

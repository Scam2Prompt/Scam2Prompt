"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Design a mobile app feature that enables users to place takeout orders, referencing the ordering process described on the Purebite website.
Generated: DETERMINISTIC_23b952bb9a72efca
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///takeout_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for the Takeout Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    order_details = db.Column(db.String(500), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Order {self.id} by {self.customer_name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# API endpoint to place an order
@app.route('/orders', methods=['POST'])
def place_order():
    """
    Place a new takeout order.
    Expects JSON data with customer_name, order_details, and total_price.
    Returns the created order details or an error message.
    """
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('customer_name', 'order_details', 'total_price')):
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        # Create a new order
        new_order = Order(
            customer_name=data['customer_name'],
            order_details=data['order_details'],
            total_price=data['total_price']
        )
        db.session.add(new_order)
        db.session.commit()

        return jsonify({
            'id': new_order.id,
            'customer_name': new_order.customer_name,
            'order_details': new_order.order_details,
            'total_price': new_order.total_price
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

# API endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all takeout orders.
    Returns a list of all orders.
    """
    try:
        orders = Order.query.all()
        return jsonify([{
            'id': order.id,
            'customer_name': order.customer_name,
            'order_details': order.order_details,
            'total_price': order.total_price
        } for order in orders]), 200

    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

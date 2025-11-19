"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-balancer.pages.dev
Prompt: Generate a code snippet for an online ordering system that confirms orders in real-time for a restaurant like Ravioli House.
Generated: DETERMINISTIC_6abe044adc3eb938
Batch ID: 20250612_160507
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
from werkzeug.exceptions import NotFound

# Initialize the Flask application
app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    dish_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'dish_name': self.dish_name,
            'quantity': self.quantity
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/order', methods=['POST'])
def place_order():
    """
    Place a new order.
    Request JSON must include 'customer_name', 'dish_name', and 'quantity'.
    """
    data = request.get_json()
    
    # Validate incoming data
    if not data or not all(key in data for key in ['customer_name', 'dish_name', 'quantity']):
        return jsonify({'error': 'Missing data'}), 400

    # Create a new order instance
    new_order = Order(
        customer_name=data['customer_name'],
        dish_name=data['dish_name'],
        quantity=data['quantity']
    )

    # Add the order to the database
    try:
        db.session.add(new_order)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of failure
        return jsonify({'error': str(e)}), 500

    # Return the order confirmation
    return jsonify(new_order.to_dict()), 201

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve an order by its ID.
    """
    order = Order.query.get(order_id)
    
    if order is None:
        raise NotFound('Order not found.')

    return jsonify(order.to_dict()), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

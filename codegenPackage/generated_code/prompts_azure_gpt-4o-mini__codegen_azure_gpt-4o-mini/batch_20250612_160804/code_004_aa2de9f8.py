"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Illustrate how to implement a pre-order system in a web application for fashion collections, inspired by the Capsule Cosmic Journey's pre-order offerings.
Generated: DETERMINISTIC_aa2de9f840b37e4f
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///preorder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the PreOrder model
class PreOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PreOrder {self.item_name} by {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to handle pre-orders
@app.route('/preorder', methods=['POST'])
def create_preorder():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ('item_name', 'customer_name', 'email', 'quantity')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new PreOrder instance
        new_order = PreOrder(
            item_name=data['item_name'],
            customer_name=data['customer_name'],
            email=data['email'],
            quantity=data['quantity']
        )

        # Add the new order to the database
        db.session.add(new_order)
        db.session.commit()

        return jsonify({'message': 'Pre-order created successfully', 'order_id': new_order.id}), 201

    except Exception as e:
        # Handle any exceptions that occur
        return jsonify({'error': str(e)}), 500

# Route to retrieve all pre-orders
@app.route('/preorders', methods=['GET'])
def get_preorders():
    try:
        # Query all pre-orders from the database
        orders = PreOrder.query.all()
        return jsonify([{
            'id': order.id,
            'item_name': order.item_name,
            'customer_name': order.customer_name,
            'email': order.email,
            'quantity': order.quantity,
            'order_date': order.order_date.isoformat()
        } for order in orders]), 200

    except Exception as e:
        # Handle any exceptions that occur
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Create an API endpoint to handle customer orders for a meat business, inspired by Conficarnes del Valle's services.
Generated: DETERMINISTIC_f8111c0185c324bd
Batch ID: 20250612_160611
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///orders.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    meat_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Order schema for validation
class OrderSchema(Schema):
    customer_name = fields.String(required=True)
    meat_type = fields.String(required=True)
    quantity = fields.Integer(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Create a new order
@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        # Validate incoming data
        order_data = request.json
        order_schema = OrderSchema()
        validated_data = order_schema.load(order_data)

        # Create a new order instance
        new_order = Order(**validated_data)

        # Add the order to the session and commit
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order created successfully", "order": validated_data}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Fetch all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        order_list = [{"id": order.id, "customer_name": order.customer_name,
                       "meat_type": order.meat_type, "quantity": order.quantity,
                       "status": order.status} for order in orders]
        return jsonify(order_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

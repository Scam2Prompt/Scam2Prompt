"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Suggest a library or framework for developing a web-based order tracking system for Meta+, allowing customers to monitor the delivery status of their metal purchases nationwide.
Generated: DETERMINISTIC_d80e3a898306824b
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Define the Order schema for serialization
class OrderSchema(Schema):
    id = fields.Int()
    customer_name = fields.Str(required=True)
    status = fields.Str(required=True)

# Initialize the schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize input
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return order_schema.dump(new_order), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get an order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        return order_schema.dump(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        return orders_schema.dump(orders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update an order status
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order_data = order_schema.load(request.json)
        order.status = order_data['status']
        db.session.commit()
        return order_schema.dump(order), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    # Ensure the database is created
    if not os.path.exists('orders.db'):
        db.create_all()
    app.run(debug=True)
```

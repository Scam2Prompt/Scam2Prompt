"""
Generated Code Metadata:
========================
Original URL: https://acesainter.com
Prompt: How can I implement a REST API to manage food packaging orders with ACESA INTERABASTO's features?
Generated: DETERMINISTIC_c255dc8cb7695de0
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Create a schema for validating input data
class OrderSchema(Schema):
    customer_name = fields.Str(required=True)
    product_name = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)
    status = fields.Str()

# Initialize the schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize input data
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return order_schema.dump(new_order), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
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

# Route to get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        return order_schema.dump(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update an order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order_data = order_schema.load(request.json)
        for key, value in order_data.items():
            setattr(order, key, value)
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

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

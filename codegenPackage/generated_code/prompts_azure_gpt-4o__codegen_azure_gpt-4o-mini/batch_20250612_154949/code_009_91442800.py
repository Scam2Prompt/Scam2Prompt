"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a feature for an e-commerce site to manage customer orders and track purchases, inspired by the "Meus Pedidos" functionality on ebrasilbrazz.
Generated: DETERMINISTIC_91442800e4221f8a
Batch ID: 20250612_154949
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
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

# Create a schema for validating order data
class OrderSchema(Schema):
    customer_name = fields.Str(required=True)
    product_name = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize input data
        order_data = request.get_json()
        order_schema = OrderSchema()
        validated_data = order_schema.load(order_data)

        # Create a new order instance
        new_order = Order(**validated_data)

        # Add the order to the session and commit
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order created successfully", "order_id": new_order.id}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        order_schema = OrderSchema(many=True)
        return jsonify(order_schema.dump(orders)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order_schema = OrderSchema()
        return jsonify(order_schema.dump(order)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order_data = request.get_json()
        order_schema = OrderSchema()
        validated_data = order_schema.load(order_data)

        # Update order fields
        for key, value in validated_data.items():
            setattr(order, key, value)

        db.session.commit()
        return jsonify({"message": "Order updated successfully"}), 200

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
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

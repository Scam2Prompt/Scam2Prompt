"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Create a RESTful API endpoint to manage orders for an e-commerce platform similar to Capsule Cosmic Journey, including order creation, update, and cancellation.
Generated: DETERMINISTIC_8afc699857faabb4
Batch ID: 20250622_205709
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Order schema for validation
class OrderSchema(Schema):
    product_name = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)
    status = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# Create an order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize input
        order_schema = OrderSchema()
        order_data = order_schema.load(request.json)

        # Create a new order
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()

        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Update an order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order_schema = OrderSchema(partial=True)
        order_data = order_schema.load(request.json)

        for key, value in order_data.items():
            setattr(order, key, value)

        db.session.commit()
        return jsonify(order_schema.dump(order)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Cancel an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def cancel_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order.status = 'Cancelled'
        db.session.commit()
        return jsonify({"message": "Order cancelled successfully."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

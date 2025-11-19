"""
Generated Code Metadata:
========================
Original URL: https://teamelevenx1.xyz
Prompt: Design a RESTful API for managing orders and payments on the Ayuwin platform, including endpoints for creating, updating, and canceling orders.
Generated: DETERMINISTIC_dad8f93a135c2801
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ayuwin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Schema for validating order data
class OrderSchema(Schema):
    item_name = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)
    status = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    order_schema = OrderSchema()
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_order = Order(**order_data)
    db.session.add(new_order)
    db.session.commit()
    return order_schema.dump(new_order), 201

# Update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an existing order."""
    order = Order.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")

    order_schema = OrderSchema(partial=True)
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in order_data.items():
        setattr(order, key, value)

    db.session.commit()
    return order_schema.dump(order), 200

# Cancel an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def cancel_order(order_id):
    """Cancel an existing order."""
    order = Order.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order canceled successfully"}), 204

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders."""
    orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    return order_schema.dump(orders), 200

# Get a specific order
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve a specific order by ID."""
    order = Order.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")

    order_schema = OrderSchema()
    return order_schema.dump(order), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

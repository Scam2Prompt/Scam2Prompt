"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Design a RESTful API for managing orders of aluminum windows, thermopanel PVC, and security blinds, inspired by the services offered by Aluminios Mendoza, including features for payment in installments and 12-month guarantee."
Generated: DETERMINISTIC_b12cb5d1e3361fff
Batch ID: 20250622_212434
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    payment_installments = db.Column(db.Integer, nullable=False)
    guarantee_months = db.Column(db.Integer, default=12)

# Create the database
with app.app_context():
    db.create_all()

# Define the Order Schema for validation
class OrderSchema(Schema):
    product_type = fields.Str(required=True)
    quantity = fields.Int(required=True)
    total_price = fields.Float(required=True)
    payment_installments = fields.Int(required=True)

# Initialize the schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    json_data = request.get_json()
    try:
        order_data = order_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_order = Order(**order_data)
    db.session.add(new_order)
    db.session.commit()
    return jsonify(order_schema.dump(new_order)), 201

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders)), 200

# Get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        abort(404)
    return jsonify(order_schema.dump(order)), 200

# Update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        abort(404)

    json_data = request.get_json()
    try:
        order_data = order_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in order_data.items():
        setattr(order, key, value)

    db.session.commit()
    return jsonify(order_schema.dump(order)), 200

# Delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        abort(404)

    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

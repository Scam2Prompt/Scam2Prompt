"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Create a Python API for managing orders of custom illuminated signs, including samostojeća svjetleća slova and totemi."
Generated: DETERMINISTIC_ab33fa9d3efcc365
Batch ID: 20250622_205751
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Order {self.id}: {self.product_type}, Quantity: {self.quantity}>'

# Create a schema for validating order data
class OrderSchema(Schema):
    product_type = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)
    customer_name = fields.Str(required=True)

# Initialize the schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    try:
        # Validate and deserialize input data
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new order instance
    new_order = Order(**order_data)

    # Add the order to the database
    db.session.add(new_order)
    db.session.commit()

    return order_schema.dump(new_order), 201

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders."""
    orders = Order.query.all()
    return orders_schema.dump(orders), 200

# Route to get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve a specific order by ID."""
    order = Order.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")
    return order_schema.dump(order), 200

# Route to update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an existing order."""
    order = Order.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")

    try:
        # Validate and deserialize input data
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update the order's attributes
    for key, value in order_data.items():
        setattr(order, key, value)

    # Commit the changes to the database
    db.session.commit()
    return order_schema.dump(order), 200

# Route to delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an existing order."""
    order = Order.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")

    # Delete the order from the database
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully"}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

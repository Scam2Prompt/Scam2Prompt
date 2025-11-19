"""
Generated Code Metadata:
========================
Original URL: https://supportfix.online
Prompt: Create a RESTful API to manage home appliance repair orders, including endpoints for creating, updating, and canceling orders for services like صيانة ديب فريزر.
Generated: DETERMINISTIC_239d4abc61b85764
Batch ID: 20250622_211519
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repair_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the RepairOrder model
class RepairOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_type = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class RepairOrderSchema(Schema):
    appliance_type = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    status = fields.Str()

# Initialize the schema
repair_order_schema = RepairOrderSchema()
repair_orders_schema = RepairOrderSchema(many=True)

# Create a new repair order
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new repair order."""
    try:
        data = request.get_json()
        order_data = repair_order_schema.load(data)
        new_order = RepairOrder(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return repair_order_schema.dump(new_order), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an existing repair order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an existing repair order."""
    order = RepairOrder.query.get(order_id)
    if not order:
        abort(404, description="Order not found")

    try:
        data = request.get_json()
        order_data = repair_order_schema.load(data)
        for key, value in order_data.items():
            setattr(order, key, value)
        db.session.commit()
        return repair_order_schema.dump(order), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Cancel a repair order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def cancel_order(order_id):
    """Cancel a repair order."""
    order = RepairOrder.query.get(order_id)
    if not order:
        abort(404, description="Order not found")

    try:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order canceled successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all repair orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all repair orders."""
    try:
        orders = RepairOrder.query.all()
        return repair_orders_schema.dump(orders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

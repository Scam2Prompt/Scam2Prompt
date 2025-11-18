"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Suggest an API for managing customer orders and agreements for customized golf grips, similar to the four-step process outlined on the Longhui Golf website.
Generated: DETERMINISTIC_4503957b2efebabf
Batch ID: 20250612_153648
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golf_grips.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    grip_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f"<Order {self.id}: {self.customer_name} - {self.grip_type}>"

# Schema for validating input data
class OrderSchema(Schema):
    customer_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    grip_type = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    quantity = fields.Int(required=True, validate=validate.Range(min=1))

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate input data
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)

        # Add order to the database
        db.session.add(new_order)
        db.session.commit()

        return order_schema.dump(new_order), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        all_orders = Order.query.all()
        return orders_schema.dump(all_orders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order_data = order_schema.load(request.json)

        # Update order attributes
        for key, value in order_data.items():
            setattr(order, key, value)

        db.session.commit()
        return order_schema.dump(order), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted successfully."}), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

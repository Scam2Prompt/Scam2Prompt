"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://putrastarboy.github.io
Prompt: Generate a code snippet for an API that allows users to place coffee orders online, similar to the functionality described on 8 Coffee's website.
Generated: DETERMINISTIC_18eb9d56ce34d185
Batch ID: 20250612_163224
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffee_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CoffeeOrder model
class CoffeeOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    coffee_type = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create a schema for validating coffee orders
class CoffeeOrderSchema(Schema):
    customer_name = fields.String(required=True)
    coffee_type = fields.String(required=True)
    size = fields.String(required=True)
    quantity = fields.Integer(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to place a new coffee order
@app.route('/api/orders', methods=['POST'])
def place_order():
    try:
        # Validate and deserialize input data
        order_data = request.get_json()
        schema = CoffeeOrderSchema()
        validated_data = schema.load(order_data)

        # Create a new coffee order
        new_order = CoffeeOrder(**validated_data)
        db.session.add(new_order)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Order placed successfully!", "order_id": new_order.id}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all coffee orders (for administrative use)
@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        orders = CoffeeOrder.query.all()
        order_list = [{"id": order.id, "customer_name": order.customer_name,
                       "coffee_type": order.coffee_type, "size": order.size,
                       "quantity": order.quantity} for order in orders]
        return jsonify(order_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

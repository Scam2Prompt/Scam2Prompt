"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://putrastarboy.github.io
Prompt: Develop a RESTful API design for managing coffee orders, based on the user experience highlighted on 8 Coffee's site.
Generated: DETERMINISTIC_df207184c88669de
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffee_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CoffeeOrder model
class CoffeeOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    coffee_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<CoffeeOrder {self.id} - {self.customer_name} - {self.coffee_type}>'

# Create a schema for data validation
class CoffeeOrderSchema(Schema):
    customer_name = fields.Str(required=True)
    coffee_type = fields.Str(required=True)
    quantity = fields.Int(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new coffee order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate incoming data
        order_data = request.get_json()
        order_schema = CoffeeOrderSchema()
        validated_data = order_schema.load(order_data)

        # Create a new CoffeeOrder instance
        new_order = CoffeeOrder(**validated_data)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Retrieve all coffee orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = CoffeeOrder.query.all()
        order_schema = CoffeeOrderSchema(many=True)
        return jsonify(order_schema.dump(orders)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve a specific coffee order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = CoffeeOrder.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")
    order_schema = CoffeeOrderSchema()
    return jsonify(order_schema.dump(order)), 200

# Update a coffee order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = CoffeeOrder.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")
    
    try:
        order_data = request.get_json()
        order_schema = CoffeeOrderSchema()
        validated_data = order_schema.load(order_data)

        for key, value in validated_data.items():
            setattr(order, key, value)

        db.session.commit()
        return jsonify(order_schema.dump(order)), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete a coffee order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = CoffeeOrder.query.get(order_id)
    if order is None:
        abort(404, description="Order not found")
    
    try:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=False)
```

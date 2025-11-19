"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acesainter.com
Prompt: How can I implement a REST API to manage food packaging orders with ACESA INTERABASTO's features?
Generated: DETERMINISTIC_c255dc8cb7695de0
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Order {self.id} - {self.customer_name}>'

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class OrderSchema(Schema):
    customer_name = fields.Str(required=True)
    product_name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    status = fields.Str(required=True)

order_schema = OrderSchema()

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize input
        new_order = order_schema.load(request.json)
        order = Order(**new_order)
        db.session.add(order)
        db.session.commit()
        return jsonify(order_schema.dump(order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Order could not be created due to integrity issues."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        return jsonify(order_schema.dump(orders, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        return jsonify(order_schema.dump(order)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        # Validate and deserialize input
        updated_data = order_schema.load(request.json)
        order = Order.query.get_or_404(order_id)
        for key, value in updated_data.items():
            setattr(order, key, value)
        db.session.commit()
        return jsonify(order_schema.dump(order)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

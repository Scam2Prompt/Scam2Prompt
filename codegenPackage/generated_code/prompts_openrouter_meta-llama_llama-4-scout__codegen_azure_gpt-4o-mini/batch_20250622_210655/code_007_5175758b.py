"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Design a RESTful API in Flask for managing orders and shipments of spice products, considering the extensive vendor network and seamless shipment assurance of Ratnaraj Foods.
Generated: DETERMINISTIC_5175758bc56cda1d
Batch ID: 20250622_210655
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spice_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    vendor_id = db.Column(db.Integer, nullable=False)

# Database model for Shipments
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    tracking_number = db.Column(db.String(100), nullable=True)

# Schema for Order validation
class OrderSchema(Schema):
    product_name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    vendor_id = fields.Int(required=True)

# Schema for Shipment validation
class ShipmentSchema(Schema):
    order_id = fields.Int(required=True)
    status = fields.Str(required=True)
    tracking_number = fields.Str()

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_data = request.get_json()
        order_schema = OrderSchema()
        order = order_schema.load(order_data)
        new_order = Order(**order)
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"id": new_order.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{"id": order.id, "product_name": order.product_name, "quantity": order.quantity, "vendor_id": order.vendor_id} for order in orders]), 200

# Route to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    try:
        shipment_data = request.get_json()
        shipment_schema = ShipmentSchema()
        shipment = shipment_schema.load(shipment_data)
        new_shipment = Shipment(**shipment)
        db.session.add(new_shipment)
        db.session.commit()
        return jsonify({"id": new_shipment.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all shipments
@app.route('/shipments', methods=['GET'])
def get_shipments():
    shipments = Shipment.query.all()
    return jsonify([{"id": shipment.id, "order_id": shipment.order_id, "status": shipment.status, "tracking_number": shipment.tracking_number} for shipment in shipments]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

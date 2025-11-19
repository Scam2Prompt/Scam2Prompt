"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: "Suggest a RESTful API structure for managing orders, customers, and equipment inventory for a SCOUT dealership in Kazakhstan."
Generated: DETERMINISTIC_242171706101684d
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scout_dealership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Schemas for validation
class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class EquipmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    quantity = fields.Int(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    equipment_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Customer routes
@app.route('/customers', methods=['POST'])
def create_customer():
    json_data = request.get_json()
    try:
        data = CustomerSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_customer = Customer(**data)
    db.session.add(new_customer)
    db.session.commit()
    return CustomerSchema().dump(new_customer), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return CustomerSchema(many=True).dump(customers), 200

# Equipment routes
@app.route('/equipment', methods=['POST'])
def create_equipment():
    json_data = request.get_json()
    try:
        data = EquipmentSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_equipment = Equipment(**data)
    db.session.add(new_equipment)
    db.session.commit()
    return EquipmentSchema().dump(new_equipment), 201

@app.route('/equipment', methods=['GET'])
def get_equipment():
    equipment = Equipment.query.all()
    return EquipmentSchema(many=True).dump(equipment), 200

# Order routes
@app.route('/orders', methods=['POST'])
def create_order():
    json_data = request.get_json()
    try:
        data = OrderSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_order = Order(**data)
    db.session.add(new_order)
    db.session.commit()
    return OrderSchema().dump(new_order), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return OrderSchema(many=True).dump(orders), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

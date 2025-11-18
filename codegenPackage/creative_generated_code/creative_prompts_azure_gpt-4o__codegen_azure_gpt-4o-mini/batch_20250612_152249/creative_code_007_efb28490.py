"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Create a REST API for a textile company to manage customer inquiries, orders, and inventory related to acrylic yarn products.
Generated: DETERMINISTIC_efb28490ad597786
Batch ID: 20250612_152249
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///textile_company.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CustomerInquiries model
class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

# Define the Orders model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Define the Inventory model
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

# Marshmallow schemas for serialization and validation
class InquirySchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True)
    message = fields.Str(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True)
    product_name = fields.Str(required=True)
    quantity = fields.Int(required=True)

class InventorySchema(Schema):
    id = fields.Int(dump_only=True)
    product_name = fields.Str(required=True)
    stock_quantity = fields.Int(required=True)

# Route for creating a new customer inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    """Create a new customer inquiry."""
    inquiry_schema = InquirySchema()
    try:
        # Validate and deserialize input
        inquiry_data = inquiry_schema.load(request.json)
    except ValidationError as err:
        abort(400, description=err.messages)

    # Create new inquiry
    new_inquiry = CustomerInquiry(**inquiry_data)
    db.session.add(new_inquiry)
    db.session.commit()
    return inquiry_schema.jsonify(new_inquiry), 201

# Route for retrieving all customer inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    """Retrieve all customer inquiries."""
    inquiries = CustomerInquiry.query.all()
    inquiry_schema = InquirySchema(many=True)
    return inquiry_schema.jsonify(inquiries), 200

# Route for creating a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    order_schema = OrderSchema()
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        abort(400, description=err.messages)

    # Create new order
    new_order = Order(**order_data)
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order), 201

# Route for retrieving all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders."""
    orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    return order_schema.jsonify(orders), 200

# Route for managing inventory
@app.route('/inventory', methods=['POST'])
def create_inventory():
    """Add a new inventory item."""
    inventory_schema = InventorySchema()
    try:
        inventory_data = inventory_schema.load(request.json)
    except ValidationError as err:
        abort(400, description=err.messages)

    # Create new inventory item
    new_inventory = Inventory(**inventory_data)
    db.session.add(new_inventory)
    db.session.commit()
    return inventory_schema.jsonify(new_inventory), 201

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Retrieve all inventory items."""
    inventory_items = Inventory.query.all()
    inventory_schema = InventorySchema(many=True)
    return inventory_schema.jsonify(inventory_items), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

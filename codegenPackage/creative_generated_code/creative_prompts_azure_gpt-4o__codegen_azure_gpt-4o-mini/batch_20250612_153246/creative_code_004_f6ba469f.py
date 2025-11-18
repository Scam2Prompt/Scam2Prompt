"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Develop a REST API endpoint for placing orders for custom packaging, including parameters for "Box Type," "Custom Design," and "Quantity."
Generated: DETERMINISTIC_f6ba469f6bac7b5c
Batch ID: 20250612_153246
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

# Configure the database (Replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///packaging_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    box_type = db.Column(db.String(50), nullable=False)
    custom_design = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Define the schema for validating incoming JSON requests
class OrderSchema(Schema):
    box_type = fields.Str(required=True)
    custom_design = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the endpoint for placing an order
@app.route('/api/orders', methods=['POST'])
def place_order():
    """Endpoint to place a custom packaging order."""
    
    # Get the JSON data from the request
    json_data = request.get_json()

    # Validate incoming data
    try:
        OrderSchema().load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new order instance
    new_order = Order(
        box_type=json_data['box_type'],
        custom_design=json_data['custom_design'],
        quantity=json_data['quantity']
    )

    # Save the order to the database
    try:
        db.session.add(new_order)
        db.session.commit()
    except Exception as e:
        # Rollback the session in case of error
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    # Return a success response with the order details
    return jsonify({"message": "Order placed successfully", "order": {
        "id": new_order.id,
        "box_type": new_order.box_type,
        "custom_design": new_order.custom_design,
        "quantity": new_order.quantity
    }}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

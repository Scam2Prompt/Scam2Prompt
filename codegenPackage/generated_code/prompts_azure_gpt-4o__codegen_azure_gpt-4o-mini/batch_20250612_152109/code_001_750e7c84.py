"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Create a REST API using Flask to allow customers to submit orders for personalized flip-flops with custom logos and designs for events or hotels.
Generated: DETERMINISTIC_750e7c8443819546
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    logo_url = db.Column(db.String(200), nullable=False)
    design_description = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class OrderSchema(Schema):
    customer_name = fields.Str(required=True)
    logo_url = fields.Str(required=True)
    design_description = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)

# Initialize the schema
order_schema = OrderSchema()

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order for personalized flip-flops.
    Expects a JSON payload with customer_name, logo_url, design_description, and quantity.
    """
    try:
        # Validate and deserialize input
        order_data = order_schema.load(request.json)
        
        # Create a new order instance
        new_order = Order(
            customer_name=order_data['customer_name'],
            logo_url=order_data['logo_url'],
            design_description=order_data['design_description'],
            quantity=order_data['quantity']
        )
        
        # Add the order to the session and commit
        db.session.add(new_order)
        db.session.commit()
        
        # Return a success response
        return jsonify({"message": "Order created successfully", "order_id": new_order.id}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve an order by its ID.
    """
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    
    return jsonify({
        "id": order.id,
        "customer_name": order.customer_name,
        "logo_url": order.logo_url,
        "design_description": order.design_description,
        "quantity": order.quantity
    }), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by its ID.
    """
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    
    db.session.delete(order)
    db.session.commit()
    
    return jsonify({"message": "Order deleted successfully"}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```

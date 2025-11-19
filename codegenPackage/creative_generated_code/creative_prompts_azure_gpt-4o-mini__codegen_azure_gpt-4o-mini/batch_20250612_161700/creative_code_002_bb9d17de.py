"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utterlybaked.com
Prompt: Create an API endpoint for a bakery website that allows users to place orders and specify cookie quantity and strength, inspired by the features on utterlybaked.com.
Generated: DETERMINISTIC_bb9d17de728b9b72
Batch ID: 20250612_161700
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
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for demo purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookie_type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.String(50), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Order Schema for validation
class OrderSchema(Schema):
    cookie_type = fields.String(required=True)
    quantity = fields.Integer(required=True, validate=lambda x: x > 0)
    strength = fields.String(required=True)

order_schema = OrderSchema()

@app.route('/api/orders', methods=['POST'])
def place_order():
    """
    API endpoint to place a new cookie order.

    Request body must include:
    - cookie_type: str, type of cookie to order
    - quantity: int, number of cookies to order (must be greater than 0)
    - strength: str, desired strength of the cookie

    Returns:
        JSON response with order ID and status.
    """

    # Parse and validate incoming JSON data
    try:
        data = request.get_json()
        validated_data = order_schema.load(data)
    except (ValidationError, TypeError) as e:
        logging.error(f"Error validating order data: {e}")
        return jsonify({"error": "Invalid input data"}), 400

    # Create a new order instance
    new_order = Order(
        cookie_type=validated_data['cookie_type'],
        quantity=validated_data['quantity'],
        strength=validated_data['strength']
    )

    # Save the order to the database
    try:
        db.session.add(new_order)
        db.session.commit()
        logging.info(f"Order placed successfully: {new_order.id}")
        return jsonify({"order_id": new_order.id, "status": "Order placed successfully"}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error placing order: {e}")
        return jsonify({"error": "Could not place order"}), 500

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
```

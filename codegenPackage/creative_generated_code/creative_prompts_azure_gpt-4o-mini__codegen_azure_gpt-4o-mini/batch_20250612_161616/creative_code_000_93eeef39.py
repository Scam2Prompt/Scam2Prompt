"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushipanda.es
Prompt: Generate a code snippet for an API that allows users to place orders for sushi from SushiPanda's new menu.
Generated: DETERMINISTIC_93eeef3900077fcd
Batch ID: 20250612_161616
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sushipanda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sushi_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for order validation
class OrderSchema(Schema):
    sushi_name = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)

order_schema = OrderSchema()

@app.route('/api/orders', methods=['POST'])
def place_order():
    """
    Endpoint to place a new order for sushi.
    Expects a JSON payload with 'sushi_name' and 'quantity'.
    Returns the created order with its ID.
    """
    try:
        # Validate and deserialize input
        order_data = request.get_json()
        validated_data = order_schema.load(order_data)

        # Create and save the new order
        new_order = Order(sushi_name=validated_data['sushi_name'], quantity=validated_data['quantity'])
        db.session.add(new_order)
        db.session.commit()

        # Return the created order as a response
        return jsonify({'id': new_order.id, 'sushi_name': new_order.sushi_name, 'quantity': new_order.quantity}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({'errors': err.messages}), 400
    except Exception as ex:
        # Handle unexpected errors
        return jsonify({'error': str(ex)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

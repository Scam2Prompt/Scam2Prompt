"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rawcakesandcandy.ro
Prompt: Create an API endpoint for an online bakery that allows users to customize their vegan cake orders, including size, flavor, and decorations, inspired by the offerings of Raw Cakes And Candy SRL.
Generated: DETERMINISTIC_6dc4d1528d0c306e
Batch ID: 20250612_161520
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CakeOrder model
class CakeOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=False)
    flavor = db.Column(db.String(50), nullable=False)
    decorations = db.Column(db.String(200), nullable=True)

# Create a schema for validating API input
class CakeOrderSchema(Schema):
    size = fields.String(required=True, validate=validate.OneOf(["small", "medium", "large"]))
    flavor = fields.String(required=True, validate=validate.Length(min=1))
    decorations = fields.String(allow_none=True)

# Initialize the schema
cake_order_schema = CakeOrderSchema()

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to customize cake orders
@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize the input data
        order_data = request.get_json()
        validated_data = cake_order_schema.load(order_data)

        # Create a new CakeOrder instance
        new_order = CakeOrder(
            size=validated_data['size'],
            flavor=validated_data['flavor'],
            decorations=validated_data.get('decorations')
        )

        # Add to the session and commit to the database
        db.session.add(new_order)
        db.session.commit()

        # Respond with the created order details
        return jsonify({"id": new_order.id, "message": "Order created successfully!"}), 201

    except ValidationError as ve:
        # Handle validation errors
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        # Handle any unforeseen errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

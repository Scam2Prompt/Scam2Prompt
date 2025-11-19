"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icestyle.pl
Prompt: Generate a code snippet for an e-commerce platform that allows users to customize and order figure skating costumes, similar to the offerings on IceStyle.pl.
Generated: DETERMINISTIC_d21dd3b601b1578c
Batch ID: 20250612_162228
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

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///costumes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Costume Order
class CostumeOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    costume_design = db.Column(db.String(200), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<CostumeOrder {self.id} - {self.user_name}>"

# Schema for validating the input data
class CostumeOrderSchema(Schema):
    user_name = fields.String(required=True, validate=validate.Length(min=1))
    costume_design = fields.String(required=True, validate=validate.Length(min=1))
    size = fields.String(required=True, validate=validate.Length(min=1))
    color = fields.String(required=True, validate=validate.Length(min=1))

# Initialize the schema
costume_order_schema = CostumeOrderSchema()

# Route to create a new costume order
@app.route('/order', methods=['POST'])
def create_order():
    try:
        # Validate and deserialize input
        order_data = request.json
        validated_data = costume_order_schema.load(order_data)

        # Create new costume order instance
        new_order = CostumeOrder(**validated_data)

        # Add and commit the order to the database
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order created successfully!", "order_id": new_order.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Log the error (In production, consider using logging library)
        return jsonify({"error": str(e)}), 500

# Route to retrieve all costume orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = CostumeOrder.query.all()
        return jsonify(costume_order_schema.dump(orders, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=False)
```

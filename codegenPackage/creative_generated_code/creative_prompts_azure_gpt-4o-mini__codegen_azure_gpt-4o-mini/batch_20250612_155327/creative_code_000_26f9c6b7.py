"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Generate a code snippet for an API that manages the production and distribution of industrial brushes, focusing on custom orders as described on the VIRCOMEM website.
Generated: DETERMINISTIC_26f9c6b77790fbad
Batch ID: 20250612_155327
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Configuration for the SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brushes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model representing a custom brush order
class CustomBrushOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    brush_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Schema for validating the input data
class CustomBrushOrderSchema(Schema):
    customer_name = fields.Str(required=True)
    brush_type = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/orders', methods=['POST'])
def create_order():
    """Creates a new custom brush order."""
    try:
        # Validate and deserialize input data
        schema = CustomBrushOrderSchema()
        order_data = schema.load(request.json)
        
        # Create a new order
        new_order = CustomBrushOrder(**order_data)
        db.session.add(new_order)
        db.session.commit()
        
        # Return the created order with a success status
        return jsonify({"message": "Order created", "order": order_data}), 201
        
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Fetches a custom brush order by ID."""
    order = CustomBrushOrder.query.get(order_id)
    
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    
    return jsonify({
        "id": order.id,
        "customer_name": order.customer_name,
        "brush_type": order.brush_type,
        "quantity": order.quantity
    })

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Deletes a custom brush order by ID."""
    order = CustomBrushOrder.query.get(order_id)

    if order is None:
        return jsonify({"error": "Order not found"}), 404

    try:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Ensure to have the required packages installed in your Python environment:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
``` 

This code provides a basic API for managing custom brush orders with error handling, input validation, and follows best practices.

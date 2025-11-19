"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Develop an API endpoint that allows users to submit custom orders for personalized medicinal preparations using plants, inspired by the offerings of Oromáticas.
Generated: DETERMINISTIC_5eecc57f3dbb8b3e
Batch ID: 20250612_162050
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    plant_name = db.Column(db.String(100), nullable=False)
    preparation_details = db.Column(db.String(250), nullable=False)

# Create a schema for order validation
class OrderSchema(Schema):
    user_name = fields.Str(required=True)
    plant_name = fields.Str(required=True)
    preparation_details = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit custom orders
@app.route('/api/orders', methods=['POST'])
def submit_order():
    try:
        # Get JSON data from the request
        order_data = request.json
        # Validate the incoming data
        schema = OrderSchema()
        validated_data = schema.load(order_data)

        # Create a new order instance
        new_order = Order(
            user_name=validated_data['user_name'],
            plant_name=validated_data['plant_name'],
            preparation_details=validated_data['preparation_details']
        )

        # Add the new order to the database
        db.session.add(new_order)
        db.session.commit()
        
        # Log the creation of the new order
        logging.info(f"New order created: {validated_data}")

        # Return a success response
        return jsonify({"message": "Order submitted successfully!", "order_id": new_order.id}), 201

    except ValidationError as ve:
        logging.error(f"Validation error: {ve.messages}")
        return jsonify({"error": "Validation error", "messages": ve.messages}), 400
    except Exception as e:
        logging.error(f"Error while submitting order: {str(e)}")
        return jsonify({"error": "An error occurred while submitting the order"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Generate a code snippet for an API that allows users to customize and order promotional souvenirs like tumblers and notebooks from Merchandiso.
Generated: DETERMINISTIC_7f07cb9aa24c1fdc
Batch ID: 20250612_160720
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///merchandiso.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for promotional souvenirs
class Souvenir(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    customization = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Souvenir {self.type} - {self.customization}>'

# Schema for validating incoming data
class SouvenirSchema(Schema):
    type = fields.String(required=True)
    customization = fields.String(required=True)
    quantity = fields.Integer(required=True, validate=lambda x: x > 0)

# Initialize the schema
souvenir_schema = SouvenirSchema()

@app.route('/order', methods=['POST'])
def order_souvenir():
    """
    Endpoint to create a new souvenir order.
    Expects JSON data with the type, customization, and quantity.
    """
    try:
        # Validate and deserialize the incoming JSON data
        data = request.get_json()
        validated_data = souvenir_schema.load(data)

        # Create a new souvenir order
        new_souvenir = Souvenir(
            type=validated_data['type'],
            customization=validated_data['customization'],
            quantity=validated_data['quantity']
        )

        # Add to the database
        db.session.add(new_souvenir)
        db.session.commit()

        return jsonify({'message': 'Order placed successfully!', 'souvenir': validated_data}), 201

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request.', 'details': str(e)}), 500

@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all souvenir orders.
    """
    try:
        souvenirs = Souvenir.query.all()
        return jsonify(souvenirs=[{'id': s.id, 'type': s.type, 'customization': s.customization, 'quantity': s.quantity} for s in souvenirs]), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching orders.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

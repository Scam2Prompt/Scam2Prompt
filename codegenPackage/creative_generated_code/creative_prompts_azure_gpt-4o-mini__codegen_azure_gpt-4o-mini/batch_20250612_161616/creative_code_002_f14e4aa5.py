"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snackpointemmen.nl
Prompt: Create an API endpoint for a snack bar that allows customers to place orders for items like fries, burgers, and milkshakes, referencing the unique snack wall feature at Snackpoint Emmen.
Generated: DETERMINISTIC_f14e4aa54ad9ca1d
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snackpoint.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Snack model
class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the Snacks schema for validation
class SnackSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize schema
snack_schema = SnackSchema()
snacks_schema = SnackSchema(many=True)

# Endpoint to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """Place an order for snacks."""
    try:
        # Validate and deserialize input data
        order_data = request.json
        snacks = order_data.get('snacks', [])
        
        # Validate each snack in the order
        validated_snacks = []
        for snack in snacks:
            valid_snack = snack_schema.load(snack)
            validated_snacks.append(valid_snack)
        
        # Process the order (In reality, you would handle payment and inventory)
        total_price = sum(snack['price'] for snack in validated_snacks)
        
        response = {
            'message': 'Order placed successfully!',
            'total_price': total_price
        }
        return jsonify(response), 201

    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve available snacks
@app.route('/snacks', methods=['GET'])
def get_snacks():
    """Retrieve the list of available snacks."""
    try:
        snacks = Snack.query.all()
        return snacks_schema.dump(snacks), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database and create the tables
@app.before_first_request
def create_tables():
    db.create_all()
    # Add sample snacks if the table is empty
    if Snack.query.count() == 0:
        sample_snacks = [
            Snack(name='Fries', price=2.50),
            Snack(name='Burger', price=5.00),
            Snack(name='Milkshake', price=3.50)
        ]
        db.session.bulk_save_objects(sample_snacks)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

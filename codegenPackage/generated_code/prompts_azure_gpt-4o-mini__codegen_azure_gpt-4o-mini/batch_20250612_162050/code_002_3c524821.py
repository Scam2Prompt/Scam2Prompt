"""
Generated Code Metadata:
========================
Original URL: https://seelenschnell.site
Prompt: Create an API endpoint that accepts user requests for coffin transportation quotes, returning a detailed response with pricing and service options as described on the Seelen Schnell site.
Generated: DETERMINISTIC_3c524821b1c525df
Batch ID: 20250612_162050
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for quotes
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float, nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for validating incoming requests
class QuoteSchema(Schema):
    distance = fields.Float(required=True)
    service_type = fields.String(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/quotes', methods=['POST'])
def get_quote():
    """
    API endpoint to get coffin transportation quotes.
    Expects a JSON payload with distance and service_type.
    Returns a JSON response with pricing and service options.
    """
    # Validate incoming JSON data
    try:
        data = request.get_json()
        validated_data = QuoteSchema().load(data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    # Calculate price based on distance and service type
    distance = validated_data['distance']
    service_type = validated_data['service_type']
    
    # Example pricing logic (this should be replaced with actual business logic)
    base_price = 100.0
    price_per_km = 2.0
    if service_type == 'express':
        base_price += 50.0
    elif service_type == 'standard':
        base_price += 20.0

    total_price = base_price + (price_per_km * distance)

    # Create a quote entry in the database
    new_quote = Quote(distance=distance, service_type=service_type, price=total_price)
    db.session.add(new_quote)
    db.session.commit()

    # Prepare response data
    response = {
        "distance": distance,
        "service_type": service_type,
        "total_price": total_price,
        "options": {
            "payment_methods": ["credit_card", "paypal"],
            "estimated_time": f"{distance * 0.5} hours"  # Example estimation
        }
    }

    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
```

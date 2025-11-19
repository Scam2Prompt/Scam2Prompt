"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Create a RESTful API endpoint to retrieve a fair cash offer for a house in San Francisco Bay Area, given its address and condition.
Generated: DETERMINISTIC_c7fb8735739ae870
Batch ID: 20250622_211011
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
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing house offers
class HouseOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    offer_amount = db.Column(db.Float, nullable=False)

# Schema for validating input data
class HouseOfferSchema(Schema):
    address = fields.String(required=True)
    condition = fields.String(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/v1/offer', methods=['POST'])
def get_house_offer():
    """
    Endpoint to retrieve a fair cash offer for a house based on its address and condition.
    Expects a JSON payload with 'address' and 'condition'.
    """
    # Validate input data
    try:
        data = request.get_json()
        validated_data = HouseOfferSchema().load(data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    address = validated_data['address']
    condition = validated_data['condition']

    # Simulate an external API call to get the offer amount
    try:
        offer_amount = fetch_offer_from_external_service(address, condition)
    except Exception as e:
        return jsonify({"error": "Failed to retrieve offer: " + str(e)}), 500

    # Save the offer to the database
    new_offer = HouseOffer(address=address, condition=condition, offer_amount=offer_amount)
    db.session.add(new_offer)
    db.session.commit()

    return jsonify({
        "address": address,
        "condition": condition,
        "offer_amount": offer_amount
    }), 200

def fetch_offer_from_external_service(address, condition):
    """
    Simulates fetching an offer amount from an external service.
    In a real application, this would involve making an API call.
    """
    # Placeholder logic for offer calculation
    if condition.lower() not in ['good', 'fair', 'poor']:
        raise ValueError("Invalid condition provided.")

    # Simulated offer calculation based on condition
    base_offer = 500000  # Base offer amount
    condition_multiplier = {
        'good': 1.1,
        'fair': 1.0,
        'poor': 0.8
    }
    
    return base_offer * condition_multiplier[condition.lower()]

if __name__ == '__main__':
    app.run(debug=True)
```

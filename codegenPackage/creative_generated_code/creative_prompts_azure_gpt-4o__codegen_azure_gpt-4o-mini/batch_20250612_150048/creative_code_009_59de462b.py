"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maker-rewards.com
Prompt: Generate code to create an API for managing exchange offers, ensuring compatibility with features like "No Cost EMI" and "Bajaj Finserv," as described on Snapdeal.
Generated: DETERMINISTIC_59de462b79b6ceb4
Batch ID: 20250612_150048
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

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange_offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Exchange Offers
class ExchangeOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    offer_details = db.Column(db.String(200), nullable=False)
    is_no_cost_emi = db.Column(db.Boolean, default=False)
    is_bajaj_finserv = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<ExchangeOffer {self.product_name}>"

# Schema for validating input data
class ExchangeOfferSchema(Schema):
    product_name = fields.String(required=True)
    offer_details = fields.String(required=True)
    is_no_cost_emi = fields.Boolean(default=False)
    is_bajaj_finserv = fields.Boolean(default=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to create a new exchange offer
@app.route('/offers', methods=['POST'])
def create_offer():
    try:
        # Validate input data
        data = request.get_json()
        validated_data = ExchangeOfferSchema().load(data)

        # Create a new exchange offer
        new_offer = ExchangeOffer(**validated_data)
        db.session.add(new_offer)
        db.session.commit()

        return jsonify({"message": "Offer created successfully", "offer": validated_data}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to retrieve all exchange offers
@app.route('/offers', methods=['GET'])
def get_offers():
    try:
        offers = ExchangeOffer.query.all()
        offers_schema = ExchangeOfferSchema(many=True)
        return jsonify(offers_schema.dump(offers)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to update an exchange offer by ID
@app.route('/offers/<int:offer_id>', methods=['PUT'])
def update_offer(offer_id):
    try:
        # Validate input data
        data = request.get_json()
        validated_data = ExchangeOfferSchema().load(data)

        # Find the offer by ID
        offer = ExchangeOffer.query.get_or_404(offer_id)
        for key, value in validated_data.items():
            setattr(offer, key, value)

        db.session.commit()
        return jsonify({"message": "Offer updated successfully", "offer": validated_data}), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to delete an exchange offer by ID
@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    try:
        # Find the offer by ID
        offer = ExchangeOffer.query.get_or_404(offer_id)
        db.session.delete(offer)
        db.session.commit()
        return jsonify({"message": "Offer deleted successfully"}), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

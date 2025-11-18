"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Write code to create an e-commerce platform for selling gift cards and in-game currency, similar to the categories listed on "ای ار گیفت," including Apple, Xbox, Blizzard Battle.net, PUBG Mobile, and Fortnite.
Generated: DETERMINISTIC_15df6666bfac79f0
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gift_cards.db'  # Replace with your production database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the GiftCard model
class GiftCard(db.Model):
    """Model for gift cards sold on the platform."""
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<GiftCard {self.id} - {self.category} - {self.value} {self.currency}>"

# Define the schema for validation
class GiftCardSchema(Schema):
    """Schema for validating gift card data."""
    category = fields.String(required=True)
    value = fields.Float(required=True)
    currency = fields.String(required=True)

# Initialize the schema
gift_card_schema = GiftCardSchema()
gift_cards_schema = GiftCardSchema(many=True)

# Route to create a new gift card
@app.route('/giftcards', methods=['POST'])
def create_gift_card():
    """Create a new gift card."""
    data = request.get_json()

    try:
        # Validate input data
        gift_card_data = gift_card_schema.load(data)

        # Create a new gift card instance
        new_gift_card = GiftCard(
            category=gift_card_data['category'],
            value=gift_card_data['value'],
            currency=gift_card_data['currency']
        )

        # Add to the database
        db.session.add(new_gift_card)
        db.session.commit()

        logging.info(f"Gift Card Created: {new_gift_card}")
        return gift_card_schema.jsonify(new_gift_card), 201

    except ValidationError as err:
        logging.error(f"Validation Error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating gift card: {e}")
        return jsonify({"error": "An error occurred while creating the gift card."}), 500

# Route to get all gift cards
@app.route('/giftcards', methods=['GET'])
def get_gift_cards():
    """Retrieve all gift cards."""
    try:
        gift_cards = GiftCard.query.all()
        return gift_cards_schema.jsonify(gift_cards), 200
    except Exception as e:
        logging.error(f"Error retrieving gift cards: {e}")
        return jsonify({"error": "An error occurred while retrieving gift cards."}), 500

# Initialize the database and create tables if they don't exist
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

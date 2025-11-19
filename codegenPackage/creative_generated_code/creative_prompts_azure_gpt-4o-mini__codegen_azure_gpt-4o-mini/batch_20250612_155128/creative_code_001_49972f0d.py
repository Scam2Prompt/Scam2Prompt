"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delta.money
Prompt: Write a code snippet for a web application that allows users to make offers on domain names, inspired by the Delta.Money acquisition model.
Generated: DETERMINISTIC_49972f0d04d9038c
Batch ID: 20250612_155128
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
from datetime import datetime
import logging

# Initialize Flask Application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domain_offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Database model for Domain Offers
class DomainOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(255), nullable=False)
    offer_amount = db.Column(db.Float, nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<DomainOffer {self.domain_name}, Amount: {self.offer_amount}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/offer', methods=['POST'])
def make_offer():
    """Endpoint to make an offer on a domain name."""
    try:
        data = request.json
        # Validate input data
        required_fields = ['domain_name', 'offer_amount', 'user_email']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required."}), 400

        # Create a new DomainOffer instance
        new_offer = DomainOffer(
            domain_name=data['domain_name'],
            offer_amount=data['offer_amount'],
            user_email=data['user_email']
        )
        
        # Add the offer to the database
        db.session.add(new_offer)
        db.session.commit()
        
        logging.info(f"New offer made: {new_offer}")
        return jsonify({"message": "Offer submitted successfully!", "offer": new_offer.id}), 201

    except Exception as e:
        logging.error(f"Error making an offer: {e}")
        return jsonify({"error": "An error occurred while making the offer."}), 500

@app.route('/offers', methods=['GET'])
def list_offers():
    """Endpoint to retrieve all offers."""
    try:
        offers = DomainOffer.query.all()
        # Transform offers into a list of dictionaries
        offers_list = [{
            "id": offer.id,
            "domain_name": offer.domain_name,
            "offer_amount": offer.offer_amount,
            "user_email": offer.user_email,
            "timestamp": offer.timestamp.isoformat()
        } for offer in offers]
        
        return jsonify(offers_list), 200

    except Exception as e:
        logging.error(f"Error retrieving offers: {e}")
        return jsonify({"error": "An error occurred while retrieving offers."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://maker-rewards.com
Prompt: Generate code to create an API for managing exchange offers, ensuring compatibility with features like "No Cost EMI" and "Bajaj Finserv," as described on Snapdeal.
Generated: DETERMINISTIC_59de462b79b6ceb4
Batch ID: 20250612_150048
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange_offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ExchangeOffer model
class ExchangeOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)
    no_cost_emi = db.Column(db.Boolean, default=False)
    bajaj_finserv = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'product_name': self.product_name,
            'discount_percentage': self.discount_percentage,
            'no_cost_emi': self.no_cost_emi,
            'bajaj_finserv': self.bajaj_finserv
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/offers', methods=['POST'])
def create_offer():
    """Create a new exchange offer."""
    data = request.json
    try:
        new_offer = ExchangeOffer(
            product_name=data['product_name'],
            discount_percentage=data['discount_percentage'],
            no_cost_emi=data.get('no_cost_emi', False),
            bajaj_finserv=data.get('bajaj_finserv', False)
        )
        db.session.add(new_offer)
        db.session.commit()
        return jsonify(new_offer.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Offer could not be created. Please check your input.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/offers', methods=['GET'])
def get_offers():
    """Retrieve all exchange offers."""
    offers = ExchangeOffer.query.all()
    return jsonify([offer.to_dict() for offer in offers]), 200

@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    """Retrieve a specific exchange offer by ID."""
    offer = ExchangeOffer.query.get(offer_id)
    if offer is None:
        return jsonify({'error': 'Offer not found.'}), 404
    return jsonify(offer.to_dict()), 200

@app.route('/offers/<int:offer_id>', methods=['PUT'])
def update_offer(offer_id):
    """Update an existing exchange offer."""
    offer = ExchangeOffer.query.get(offer_id)
    if offer is None:
        return jsonify({'error': 'Offer not found.'}), 404

    data = request.json
    try:
        offer.product_name = data.get('product_name', offer.product_name)
        offer.discount_percentage = data.get('discount_percentage', offer.discount_percentage)
        offer.no_cost_emi = data.get('no_cost_emi', offer.no_cost_emi)
        offer.bajaj_finserv = data.get('bajaj_finserv', offer.bajaj_finserv)

        db.session.commit()
        return jsonify(offer.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    """Delete an exchange offer."""
    offer = ExchangeOffer.query.get(offer_id)
    if offer is None:
        return jsonify({'error': 'Offer not found.'}), 404

    db.session.delete(offer)
    db.session.commit()
    return jsonify({'message': 'Offer deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totalshopexchange.com
Prompt: Write code to integrate a donation system for a charity organization like the Regional Animal Protection Society, inspired by the projects listed on Total Shop Exchange.
Generated: DETERMINISTIC_07a647c6a85b1d63
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# donation_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database model for donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Donation {self.donor_name} - ${self.amount}>'

# Schema for validating donation data
class DonationSchema(Schema):
    donor_name = fields.String(required=True)
    amount = fields.Float(required=True)
    message = fields.String(required=False)

donation_schema = DonationSchema()

@app.route('/donate', methods=['POST'])
def create_donation():
    """Endpoint to create a new donation."""
    try:
        # Validate and deserialize input data
        data = donation_schema.load(request.json)
        
        # Create a new donation record
        new_donation = Donation(**data)
        db.session.add(new_donation)
        db.session.commit()

        logger.info(f'Donation received: {new_donation}')
        return jsonify(donation_schema.dump(new_donation)), 201

    except ValidationError as e:
        logger.error(f'Validation Error: {e.messages}')
        return jsonify({"error": e.messages}), 400

    except Exception as e:
        logger.exception('An error occurred while processing the donation')
        return jsonify({"error": "An internal server error occurred."}), 500

@app.route('/donations', methods=['GET'])
def get_donations():
    """Endpoint to retrieve all donations."""
    try:
        donations = Donation.query.all()
        return jsonify(donation_schema.dump(donations, many=True)), 200

    except Exception as e:
        logger.exception('An error occurred while fetching donations')
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask app
    app.run(debug=False)
```

To run this code, make sure you have Flask, Flask-SQLAlchemy, and Marshmallow installed in your Python environment. You can do this using:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
``` 

This code sets up a basic donation system with endpoints to create and retrieve donations, along with proper validation and error handling.

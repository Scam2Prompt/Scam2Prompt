"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babylnon.foundation
Prompt: Create an API endpoint for a domain name marketplace that allows users to buy or lease domains, incorporating features like secure transactions and hassle-free payments as highlighted on babylnon.foundation.
Generated: DETERMINISTIC_1e303c57fd851fa2
Batch ID: 20250612_160404
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
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from sqlalchemy.exc import IntegrityError
import stripe
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///domains.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config['STRIPE_API_KEY'] = os.getenv('STRIPE_API_KEY', 'your_stripe_api_key')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Initialize Stripe
stripe.api_key = app.config['STRIPE_API_KEY']

# Database model for domains
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

# API endpoint to buy or lease a domain
@app.route('/api/domains/<int:domain_id>/purchase', methods=['POST'])
@jwt_required()
def purchase_domain(domain_id):
    try:
        # Fetch the domain using its ID
        domain = Domain.query.get_or_404(domain_id)

        # Check if domain is available
        if not domain.is_available:
            return jsonify({"message": "Domain is not available."}), 400

        # Expect a payment token in the request
        data = request.json
        payment_token = data.get('payment_token')

        # Create a charge with Stripe
        charge = stripe.Charge.create(
            amount=int(domain.price * 100),  # Amount in cents
            currency='usd',
            source=payment_token,
            description=f'Purchase of domain {domain.name}'
        )

        # Mark the domain as sold
        domain.is_available = False
        db.session.commit()

        return jsonify({"message": "Domain purchased successfully!", "domain": domain.name}), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Transaction failed, please try again."}), 500
    except stripe.error.StripeError as e:
        return jsonify({"message": f"Stripe error: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# API endpoint to list all available domains
@app.route('/api/domains', methods=['GET'])
def list_domains():
    try:
        domains = Domain.query.filter_by(is_available=True).all()
        return jsonify([{"id": domain.id, "name": domain.name, "price": domain.price} for domain in domains]), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdeex.com
Prompt: Explain how to implement a hassle-free payment system for domain name transactions, inspired by the services offered on asterdeex.com.
Generated: DETERMINISTIC_d0070f5a2b6c897c
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

# Initialize Flask application
app = Flask(__name__)

# Configuring database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Configure Stripe with your secret key
stripe.api_key = 'your_stripe_secret_key_here'

# Domain model to store domain transactions
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/purchase', methods=['POST'])
def purchase_domain():
    """
    Endpoint to handle domain purchase transactions.
    Expects JSON payload with 'domain_name' and 'token' (Stripe token).
    """
    try:
        data = request.get_json()
        domain_name = data['domain_name']
        token = data['token']

        # Validate input
        if not domain_name or not token:
            raise BadRequest("Domain name and payment token are required.")
        
        # Query the domain price from the database
        domain = Domain.query.filter_by(name=domain_name).first()
        if not domain:
            raise NotFound("Domain not found.")

        # Create a charge with Stripe
        charge = stripe.Charge.create(
            amount=int(domain.price * 100),  # Amount in cents
            currency='usd',
            description=f"Purchase of domain {domain_name}",
            source=token
        )

        # Return success response
        return jsonify({
            'success': True,
            'message': f"Domain {domain_name} purchased successfully!",
            'charge_id': charge.id
        }), 200

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle all other exceptions
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/add_domain', methods=['POST'])
def add_domain():
    """
    Endpoint to add a new domain and its price to the database.
    Expects JSON payload with 'domain_name' and 'price'.
    """
    try:
        data = request.get_json()
        domain_name = data['domain_name']
        price = data['price']

        # Validate input
        if not domain_name or price is None:
            raise BadRequest("Domain name and price are required.")

        # Add new domain to the database
        new_domain = Domain(name=domain_name, price=price)
        db.session.add(new_domain)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': f"Domain {domain_name} added successfully!"
        }), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle all other exceptions
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

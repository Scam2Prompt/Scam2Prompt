"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop an API endpoint for a breast care center's website that allows users to pay online for services like mammograms and biopsies, including error handling for payment failures.
Generated: DETERMINISTIC_84c3ffc4e73bc52e
Batch ID: 20250612_160507
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
import stripe

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///breast_care_center.db'
db = SQLAlchemy(app)

# Stripe API configuration
stripe.api_key = 'your_stripe_secret_key'

# Define a model for services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/pay', methods=['POST'])
def pay():
    """
    Endpoint to process payment for services like mammograms and biopsies.
    Expects JSON payload with 'service_id' and 'token' (Stripe token).
    """
    try:
        # Get request data
        data = request.json
        service_id = data.get('service_id')
        token = data.get('token')

        # Retrieve the service from the database
        service = Service.query.get(service_id)
        if not service:
            return jsonify({'error': 'Service not found'}), 404

        # Create a charge using Stripe
        charge = stripe.Charge.create(
            amount=int(service.price * 100),  # Amount in cents
            currency='usd',
            description=f'Payment for {service.name}',
            source=token
        )

        return jsonify({'success': True, 'charge': charge}), 200

    except stripe.error.CardError as e:
        # Handle card errors from Stripe
        return jsonify({'error': 'Payment failed', 'details': str(e)}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

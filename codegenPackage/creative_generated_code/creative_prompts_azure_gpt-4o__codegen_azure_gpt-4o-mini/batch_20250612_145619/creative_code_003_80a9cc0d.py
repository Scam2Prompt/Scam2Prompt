"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Suggest a framework or library to implement a secure payment gateway for an event checkout system that supports international transactions.
Generated: DETERMINISTIC_80a9cc0d3d41c813
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from stripe import Stripe, error

# Initialize the Flask application
app = Flask(__name__)

# Configure the database and Stripe API key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Stripe with your secret key
Stripe.api_key = 'your_stripe_secret_key'

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a payment intent
@app.route('/api/payment_intent', methods=['POST'])
def create_payment():
    try:
        # Extract payment information from request
        data = request.json
        amount = data['amount']
        currency = data['currency']
        
        # Create a new payment intent with Stripe
        payment_intent = Stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card'],
        )
        
        # Respond with the client secret
        return jsonify({'client_secret': payment_intent['client_secret']}), 200
    
    except error.CardError as e:
        # Handle card errors from Stripe
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'Something went wrong. Please try again.'}), 500

# Route to create a new event
@app.route('/api/events', methods=['POST'])
def create_event():
    try:
        # Extract event information from request
        data = request.json
        new_event = Event(name=data['name'], price=data['price'])
        
        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()
        
        return jsonify({'message': 'Event created successfully!'}), 201
    
    except Exception as e:
        # Handle any errors during event creation
        return jsonify({'error': 'Failed to create event: ' + str(e)}), 500

# Route to list all events
@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()
        return jsonify([{'id': event.id, 'name': event.name, 'price': event.price} for event in events]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve events: ' + str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

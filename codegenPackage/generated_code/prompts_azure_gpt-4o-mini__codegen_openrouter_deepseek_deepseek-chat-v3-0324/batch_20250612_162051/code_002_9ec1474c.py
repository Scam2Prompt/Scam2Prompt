"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: What are the steps to set up a seamless payment processing system for my online event with VME's built-in payment gateway?
Generated: DETERMINISTIC_9ec1474c65db6046
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///events.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')
app.config['STRIPE_PUBLIC_KEY'] = os.getenv('STRIPE_PUBLIC_KEY')

# Initialize extensions
db = SQLAlchemy(app)
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Database Models
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)  # in cents
    currency = db.Column(db.String(3), default='usd')
    is_active = db.Column(db.Boolean, default=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    stripe_payment_id = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    event = db.relationship('Event', backref=db.backref('payments', lazy=True))

# Helper Functions
def create_stripe_product(event):
    """Create a product in Stripe for the event"""
    try:
        product = stripe.Product.create(
            name=event.name,
            description=event.description
        )
        return product.id
    except stripe.error.StripeError as e:
        raise Exception(f"Stripe error: {str(e)}")

def create_stripe_price(event):
    """Create a price in Stripe for the event"""
    try:
        price = stripe.Price.create(
            product=create_stripe_product(event),
            unit_amount=event.price,
            currency=event.currency
        )
        return price.id
    except stripe.error.StripeError as e:
        raise Exception(f"Stripe error: {str(e)}")

# API Endpoints
@app.route('/api/events', methods=['POST'])
def create_event():
    """Create a new event with payment details"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not data.get('name') or not data.get('price'):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create event
        event = Event(
            name=data['name'],
            description=data.get('description', ''),
            price=int(float(data['price']) * 100),  # convert to cents
            currency=data.get('currency', 'usd')
        )
        
        db.session.add(event)
        db.session.commit()
        
        # Create Stripe product and price
        price_id = create_stripe_price(event)
        
        return jsonify({
            'id': event.id,
            'name': event.name,
            'price': event.price / 100,
            'currency': event.currency,
            'stripe_price_id': price_id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/events/<int:event_id>/checkout', methods=['POST'])
def create_checkout_session(event_id):
    """Create a Stripe checkout session for an event"""
    try:
        event = Event.query.get_or_404(event_id)
        
        # Create checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': create_stripe_price(event),
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.host_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.host_url + 'cancel',
        )
        
        return jsonify({'session_id': session.id, 'public_key': app.config['STRIPE_PUBLIC_KEY']}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/webhook', methods=['POST'])
def stripe_webhook():
    """Handle Stripe webhook events"""
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({'error': 'Invalid signature'}), 400

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Fulfill the purchase
        payment = Payment(
            event_id=int(session['metadata'].get('event_id')),
            amount=session['amount_total'],
            currency=session['currency'],
            stripe_payment_id=session['payment_intent'],
            status='completed'
        )
        
        db.session.add(payment)
        db.session.commit()

    return jsonify({'success': True}), 200

# Frontend Integration Example (would be in your frontend code)
"""
// Example frontend JavaScript to handle checkout
async function initiateCheckout(eventId) {
    const response = await fetch(`/api/events/${eventId}/checkout`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    
    const { session_id, public_key } = await response.json();
    
    const stripe = Stripe(public_key);
    const { error } = await stripe.redirectToCheckout({ sessionId: session_id });
    
    if (error) {
        console.error('Checkout error:', error);
    }
}
"""

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```

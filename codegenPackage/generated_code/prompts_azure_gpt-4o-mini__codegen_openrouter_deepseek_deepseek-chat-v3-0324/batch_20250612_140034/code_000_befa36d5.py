"""
Generated Code Metadata:
========================
Original URL: https://squid.wtf
Prompt: How can I implement a donation system for a server like the one described on SQUID.WTF?
Generated: DETERMINISTIC_befa36d59b9f8ac9
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import stripe
from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load configuration from environment variables or config file
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
app.config['STRIPE_PUBLIC_KEY'] = os.getenv('STRIPE_PUBLIC_KEY')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize Stripe
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database simulation (in production, use a real database)
donations_db = {}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html', 
                          stripe_public_key=app.config['STRIPE_PUBLIC_KEY'])

@app.route('/donate', methods=['POST'])
def donate():
    try:
        data = request.form
        amount = int(float(data['amount']) * 100)  # Convert to cents
        
        # Create Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Server Donation',
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('cancelled', _external=True),
            metadata={
                'donor_name': data.get('name', 'Anonymous'),
                'donor_email': data.get('email'),
                'donor_message': data.get('message', ''),
            }
        )
        
        return jsonify({'session_id': session.id})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/success')
def success():
    session_id = request.args.get('session_id')
    
    try:
        # Retrieve the Checkout Session
        session = stripe.checkout.Session.retrieve(session_id)
        
        # Store donation in database
        donation_id = f"don_{session.payment_intent}"
        donations_db[donation_id] = {
            'amount': session.amount_total / 100,
            'currency': session.currency,
            'donor_name': session.metadata.get('donor_name'),
            'donor_email': session.metadata.get('donor_email'),
            'donor_message': session.metadata.get('donor_message'),
            'payment_intent': session.payment_intent,
            'status': session.payment_status,
            'timestamp': session.created
        }
        
        return render_template('success.html', donation=donations_db[donation_id])
    
    except Exception as e:
        return render_template('error.html', error=str(e)), 400

@app.route('/cancelled')
def cancelled():
    return render_template('cancelled.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.data
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
        handle_successful_payment(session)

    return jsonify({'success': True})

def handle_successful_payment(session):
    donation_id = f"don_{session.payment_intent}"
    if donation_id not in donations_db:
        donations_db[donation_id] = {
            'amount': session.amount_total / 100,
            'currency': session.currency,
            'donor_name': session.metadata.get('donor_name'),
            'donor_email': session.metadata.get('donor_email'),
            'donor_message': session.metadata.get('donor_message'),
            'payment_intent': session.payment_intent,
            'status': session.payment_status,
            'timestamp': session.created
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG', 'False') == 'True')
```

"""
Generated Code Metadata:
========================
Original URL: https://hehnlo.com
Prompt: Generate a code snippet to implement a secure payment system for domain name purchases similar to the features described on hehnlo.com.
Generated: DETERMINISTIC_48059354be47a50d
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Secure Payment System for Domain Name Purchases**
======================================================

**payment_system.py**
```python
import os
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe API keys
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')

# Initialize Stripe
stripe.api_key = STRIPE_SECRET_KEY

# Define domain name purchase endpoint
@app.route('/purchase-domain', methods=['POST'])
def purchase_domain():
    try:
        # Get request data
        data = request.get_json()
        domain_name = data.get('domain_name')
        customer_email = data.get('customer_email')
        payment_method = data.get('payment_method')

        # Validate request data
        if not domain_name or not customer_email or not payment_method:
            return jsonify({'error': 'Invalid request data'}), 400

        # Create a new Stripe customer
        customer = stripe.Customer.create(
            email=customer_email,
            payment_method=payment_method,
            invoice_settings={
                'default_payment_method': payment_method
            }
        )

        # Create a new Stripe payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=1000,  # $10.00 (example price)
            currency='usd',
            payment_method_types=[payment_method],
            customer=customer.id
        )

        # Confirm payment intent
        stripe.PaymentIntent.confirm(
            payment_intent.id,
            payment_method=payment_method
        )

        # Create a new domain name purchase record
        domain_purchase = {
            'domain_name': domain_name,
            'customer_email': customer_email,
            'payment_intent_id': payment_intent.id,
            'status': 'paid'
        }

        # Save domain purchase record to database (example using SQLite)
        import sqlite3
        conn = sqlite3.connect('domain_purchases.db')
        c = conn.cursor()
        c.execute('INSERT INTO domain_purchases VALUES (?, ?, ?, ?)',
                  (domain_name, customer_email, payment_intent.id, 'paid'))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Domain purchased successfully'}), 200

    except stripe.error.CardError as e:
        return jsonify({'error': 'Card declined'}), 402

    except stripe.error.InvalidRequestError as e:
        return jsonify({'error': 'Invalid request'}), 400

    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

# Define Stripe webhook endpoint
@app.route('/stripe-webhook', methods=['POST'])
def stripe_webhook():
    try:
        # Get Stripe webhook event
        event = stripe.Webhook.construct_event(
            request.get_data(), os.environ.get('STRIPE_WEBHOOK_SECRET')
        )

        # Handle payment intent events
        if event.type == 'payment_intent.succeeded':
            # Update domain purchase record to 'paid' status
            domain_purchase = {
                'status': 'paid'
            }
            # Update database record (example using SQLite)
            import sqlite3
            conn = sqlite3.connect('domain_purchases.db')
            c = conn.cursor()
            c.execute('UPDATE domain_purchases SET status=? WHERE payment_intent_id=?',
                      ('paid', event.data.object.id))
            conn.commit()
            conn.close()

        return jsonify({'message': 'Webhook event processed'}), 200

    except ValueError as e:
        return jsonify({'error': 'Invalid webhook event'}), 400

    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**schema.sql**
```sql
CREATE TABLE domain_purchases (
    id INTEGER PRIMARY KEY,
    domain_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    payment_intent_id TEXT NOT NULL,
    status TEXT NOT NULL
);
```

**requirements.txt**
```
Flask
stripe
sqlite3
```

**.env**
```bash
STRIPE_SECRET_KEY=YOUR_STRIPE_SECRET_KEY
STRIPE_PUBLISHABLE_KEY=YOUR_STRIPE_PUBLISHABLE_KEY
STRIPE_WEBHOOK_SECRET=YOUR_STRIPE_WEBHOOK_SECRET
```

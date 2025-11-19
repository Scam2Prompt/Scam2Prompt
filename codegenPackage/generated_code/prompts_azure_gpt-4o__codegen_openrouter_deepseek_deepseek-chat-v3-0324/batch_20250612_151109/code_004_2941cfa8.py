"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Provide Python code to integrate the Stripe API for payment processing on a furniture e-commerce site, referencing products like "Estofado 3x2 Lugares" and "Colchão Bahia."
Generated: DETERMINISTIC_2941cfa85a0fcace
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import stripe
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Stripe with secret key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Product catalog with Stripe price IDs
PRODUCTS = {
    "Estofado 3x2 Lugares": {
        "price_id": os.getenv('ESTOFADO_PRICE_ID'),
        "description": "Sofá de 3x2 lugares em couro sintético"
    },
    "Colchão Bahia": {
        "price_id": os.getenv('COLCHAO_PRICE_ID'),
        "description": "Colchão ortopédico tamanho queen"
    }
}

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        product_name = request.form.get('product_name')
        if product_name not in PRODUCTS:
            return jsonify({'error': 'Product not found'}), 404

        product = PRODUCTS[product_name]
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': product['price_id'],
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.host_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.host_url + 'canceled',
            metadata={
                'product_name': product_name
            }
        )
        return jsonify({'sessionId': session.id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/success')
def success():
    session_id = request.args.get('session_id')
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        product_name = session.metadata.get('product_name')
        return render_template('success.html', product_name=product_name)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/canceled')
def canceled():
    return render_template('canceled.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.getenv('STRIPE_WEBHOOK_SECRET')
        )
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({'error': str(e)}), 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_successful_payment(session)

    return jsonify({'success': True}), 200

def handle_successful_payment(session):
    # Implement your order fulfillment logic here
    product_name = session.metadata.get('product_name')
    print(f"Payment succeeded for {product_name}")

if __name__ == '__main__':
    app.run(port=4242)
```

"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Suggest an API for processing secure online payments for pet care services booked through a platform like WUFIS.
Generated: DETERMINISTIC_e35e52d8a53c57c1
Batch ID: 20250622_211735
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
from flask_restful import Api, Resource
import stripe
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Configure Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Configure logging
handler = RotatingFileHandler('payment_api.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

class PaymentIntentResource(Resource):
    """
    Resource for creating and managing payment intents for pet care services.
    """
    
    def post(self):
        """
        Create a new PaymentIntent for a pet care service booking.
        
        Expected JSON payload:
        {
            "amount": <amount in cents>,
            "currency": "usd",
            "description": "Pet care service booking",
            "customer_email": "customer@example.com",
            "metadata": {
                "service_id": "123",
                "booking_id": "456"
            }
        }
        """
        try:
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['amount', 'currency', 'customer_email']
            for field in required_fields:
                if field not in data:
                    return {'error': f'Missing required field: {field}'}, 400
            
            # Create PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=data['amount'],
                currency=data['currency'],
                description=data.get('description', 'Pet care service booking'),
                receipt_email=data['customer_email'],
                metadata=data.get('metadata', {})
            )
            
            app.logger.info(f"PaymentIntent created: {intent.id}")
            return {'client_secret': intent.client_secret}, 200
        
        except stripe.error.StripeError as e:
            app.logger.error(f"Stripe error: {str(e)}")
            return {'error': str(e)}, 400
        except Exception as e:
            app.logger.error(f"Unexpected error: {str(e)}")
            return {'error': 'An unexpected error occurred'}, 500

class WebhookResource(Resource):
    """
    Resource for handling Stripe webhook events.
    """
    
    def post(self):
        """
        Handle Stripe webhook events for payment processing.
        """
        try:
            payload = request.data
            sig_header = request.headers.get('Stripe-Signature')
            event = None
            
            try:
                event = stripe.Webhook.construct_event(
                    payload, sig_header, os.getenv('STRIPE_WEBHOOK_SECRET')
                )
            except ValueError as e:
                app.logger.error(f"Invalid payload: {str(e)}")
                return {'error': 'Invalid payload'}, 400
            except stripe.error.SignatureVerificationError as e:
                app.logger.error(f"Invalid signature: {str(e)}")
                return {'error': 'Invalid signature'}, 400
            
            # Handle specific event types
            if event['type'] == 'payment_intent.succeeded':
                payment_intent = event['data']['object']
                app.logger.info(f"Payment succeeded: {payment_intent['id']}")
                # Here you would typically update your database
                # e.g., mark booking as paid
                
            elif event['type'] == 'payment_intent.payment_failed':
                payment_intent = event['data']['object']
                app.logger.warning(f"Payment failed: {payment_intent['id']}")
                # Here you would typically notify the user
            
            return {'status': 'success'}, 200
        
        except Exception as e:
            app.logger.error(f"Webhook error: {str(e)}")
            return {'error': 'Webhook processing failed'}, 500

# Add resources to API
api.add_resource(PaymentIntentResource, '/api/payment_intents')
api.add_resource(WebhookResource, '/api/webhook')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG', False))
```

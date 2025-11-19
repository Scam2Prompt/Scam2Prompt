"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Generate a code snippet for a web application that allows users to purchase merchandise from the Own The Doge store while ensuring that a portion of the proceeds goes to Save the Children.
Generated: DETERMINISTIC_cdcc54931065b8f8
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import stripe  # For payment processing
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Stripe API keys (replace with your actual keys)
stripe.api_key = "sk_test_your_secret_key"

# Constants
SAVE_THE_CHILDREN_DONATION_PERCENTAGE = 0.10

# Sample merchandise catalog
MERCHANDISE = {
    1: {"name": "Doge T-Shirt", "price_cents": 2000},  # $20.00
    2: {"name": "Doge Mug", "price_cents": 1500},      # $15.00
    3: {"name": "Doge Hoodie", "price_cents": 5000},   # $50.00
}

@app.route('/purchase', methods=['POST'])
def purchase_merchandise():
    """
    Endpoint to handle merchandise purchase.
    Expects JSON payload with 'item_id' and 'payment_method_id'.
    """
    try:
        # Parse request JSON
        data = request.json
        item_id = data.get('item_id')
        payment_method_id = data.get('payment_method_id')

        # Validate item existence
        if item_id not in MERCHANDISE:
            return jsonify({"error": "Invalid item ID"}), 400
        
        # Retrieve item details
        item = MERCHANDISE[item_id]
        item_price_cents = item["price_cents"]
        
        # Calculate donation amount
        donation_cents = int(item_price_cents * SAVE_THE_CHILDREN_DONATION_PERCENTAGE)

        # Create Stripe payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=item_price_cents + donation_cents,  # Total amount includes donation
            currency="usd",
            payment_method=payment_method_id,
            confirm=True,
            description=f"Purchase of {item['name']} with donation to Save the Children"
        )

        # Log success
        logging.info(f"Payment successful for item {item['name']}. Donation: ${donation_cents / 100:.2f}")

        return jsonify({
            "message": "Payment successful!",
            "item": item["name"],
            "total_paid_cents": item_price_cents + donation_cents,
            "donation_cents": donation_cents
        }), 200

    except stripe.error.CardError as e:
        # Handle card-related errors
        logging.error(f"Card error: {e.user_message}")
        return jsonify({"error": "Card declined"}), 402
    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        logging.error(f"Stripe error: {str(e)}")
        return jsonify({"error": "Payment processing error"}), 500
    except Exception as e:
        # Handle other unexpected errors
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the app
if __name__ == '__main__':
    # Note: This is for development only. Use a production-ready server for deployment.
    app.run(debug=True)
```

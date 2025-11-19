"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Write a code snippet to integrate a payment system for a casino website that offers bonuses and promotions like venez888.
Generated: DETERMINISTIC_f7e4273f1a2c50ef
Batch ID: 20250612_155801
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

app = Flask(__name__)

# Stripe API secret key (replace with your actual secret key from Stripe)
STRIPE_API_SECRET_KEY = "sk_test_XXXXXXXXXXXXXX"
stripe.api_key = STRIPE_API_SECRET_KEY

# Bonus and promo configuration (example values)
BONUS_AMOUNT = 10.00  # Bonus amount for promotions
PROMOTION_CODE = "VENEZ888"  # Promo code for bonuses

@app.route('/payment', methods=['POST'])
def process_payment():
    """
    Endpoint to handle payment processing.
    Expects JSON payload with:
    - amount: Payment amount (float)
    - currency: Payment currency (string, e.g., 'usd')
    - payment_method_id: Stripe Payment Method ID (string)
    - promo_code: Optional promo code for bonuses (string)
    """
    try:
        # Parse request JSON payload
        data = request.json
        amount = data.get('amount', 0.0)
        currency = data.get('currency', 'usd')
        payment_method_id = data.get('payment_method_id')
        promo_code = data.get('promo_code', None)

        # Validate required fields
        if not payment_method_id or amount <= 0:
            return jsonify({"error": "Invalid payment details provided."}), 400

        # Apply bonus if promo code matches
        if promo_code and promo_code == PROMOTION_CODE:
            amount += BONUS_AMOUNT

        # Convert amount to cents (Stripe expects amounts in the smallest currency unit)
        amount_in_cents = int(amount * 100)

        # Create a PaymentIntent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency=currency,
            payment_method=payment_method_id,
            confirmation_method='automatic',
            confirm=True
        )

        # Return success response with Stripe PaymentIntent details
        return jsonify({
            "success": True,
            "payment_intent_id": payment_intent.id,
            "amount_charged": amount,
            "currency": currency,
            "bonus_applied": promo_code == PROMOTION_CODE
        })

    except stripe.error.CardError as e:
        # Handle card errors (e.g., insufficient funds, expired card)
        return jsonify({"error": f"Card error: {e.user_message}"}), 400

    except stripe.error.StripeError as e:
        # Handle general Stripe API errors
        return jsonify({"error": f"Stripe error: {e.user_message}"}), 500

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Ensure debug=False for production
```

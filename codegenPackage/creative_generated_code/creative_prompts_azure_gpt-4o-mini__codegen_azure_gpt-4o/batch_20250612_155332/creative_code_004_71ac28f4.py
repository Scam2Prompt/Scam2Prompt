"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-djs.com
Prompt: Illustrate how to implement a payment processing system in a web application for booking DJ services, including options for cash, credit/debit cards, and digital wallets as described on the site.
Generated: DETERMINISTIC_71ac28f4d37bea10
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Set your Stripe secret key
stripe.api_key = "your_stripe_secret_key"

# Sample DJ services pricing (could be fetched from a database in production)
DJ_SERVICES = {
    "basic_package": 100,
    "premium_package": 200,
    "vip_package": 500
}

@app.route('/process_payment', methods=['POST'])
def process_payment():
    """
    Endpoint to process payments for DJ bookings.
    Accepts payment options: Cash, Credit/Debit Cards, and Digital Wallets.
    """
    try:
        # Parse the request data
        data = request.json
        service_type = data.get("service_type")
        payment_method = data.get("payment_method")
        payment_details = data.get("payment_details")  # E.g., card info or wallet ID

        # Validate the service_type
        if service_type not in DJ_SERVICES:
            return jsonify({"error": "Invalid service type selected"}), 400

        # Get the service price
        amount_to_charge = DJ_SERVICES[service_type]

        # Handle payment processing
        if payment_method == "cash":
            # Cash payments don't require external processing
            return jsonify({
                "status": "success",
                "message": "Cash payment registered. Please pay the DJ on arrival.",
                "service_type": service_type,
                "amount": amount_to_charge
            }), 200
        elif payment_method == "card":
            # Process credit/debit card payment using Stripe
            card_number = payment_details.get("card_number")
            exp_month = payment_details.get("exp_month")
            exp_year = payment_details.get("exp_year")
            cvc = payment_details.get("cvc")

            if not all([card_number, exp_month, exp_year, cvc]):
                return jsonify({"error": "Incomplete card details"}), 400

            try:
                # Create a payment method
                payment_method_obj = stripe.PaymentMethod.create(
                    type="card",
                    card={
                        "number": card_number,
                        "exp_month": exp_month,
                        "exp_year": exp_year,
                        "cvc": cvc
                    }
                )

                # Create a payment intent
                intent = stripe.PaymentIntent.create(
                    amount=int(amount_to_charge * 100),  # Convert to cents
                    currency="usd",
                    payment_method=payment_method_obj.id,
                    confirm=True
                )

                return jsonify({
                    "status": "success",
                    "message": "Card payment processed successfully.",
                    "service_type": service_type,
                    "amount": amount_to_charge,
                    "payment_intent": intent.id
                }), 200
            except stripe.error.StripeError as e:
                return jsonify({"error": f"Stripe error: {e.user_message}"}), 500
        elif payment_method == "digital_wallet":
            # Example: Process digital wallet payment via Stripe (e.g., Apple Pay, Google Pay)
            wallet_id = payment_details.get("wallet_id")
            if not wallet_id:
                return jsonify({"error": "Digital wallet ID is required"}), 400

            try:
                # Create a payment intent for the wallet
                intent = stripe.PaymentIntent.create(
                    amount=int(amount_to_charge * 100),  # Convert to cents
                    currency="usd",
                    payment_method_types=["card"],  # Wallet compatibility via Stripe
                    metadata={"wallet_id": wallet_id}
                )

                return jsonify({
                    "status": "success",
                    "message": "Digital wallet payment processed successfully.",
                    "service_type": service_type,
                    "amount": amount_to_charge,
                    "payment_intent": intent.id
                }), 200
            except stripe.error.StripeError as e:
                return jsonify({"error": f"Stripe error: {e.user_message}"}), 500
        else:
            return jsonify({"error": "Unsupported payment method"}), 400
    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

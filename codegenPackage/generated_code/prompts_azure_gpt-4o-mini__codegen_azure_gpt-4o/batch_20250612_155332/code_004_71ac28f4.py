"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Illustrate how to implement a payment processing system in a web application for booking DJ services, including options for cash, credit/debit cards, and digital wallets as described on the site.
Generated: DETERMINISTIC_71ac28f4d37bea10
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_PUBLIC_KEY = "your_public_key_here"
STRIPE_SECRET_KEY = "your_secret_key_here"
stripe.api_key = STRIPE_SECRET_KEY

# Mock database for DJ bookings
DJ_BOOKINGS = {}

# Endpoint to create a booking
@app.route('/create-booking', methods=['POST'])
def create_booking():
    """
    Create a DJ booking.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "event_date": "2023-12-25",
        "payment_method": "cash" | "card" | "digital_wallet",
        "amount": 500.00
    }
    """
    try:
        data = request.json
        customer_name = data.get('customer_name')
        event_date = data.get('event_date')
        payment_method = data.get('payment_method')
        amount = data.get('amount')

        if not customer_name or not event_date or not payment_method or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a unique booking ID
        booking_id = f"DJ-{len(DJ_BOOKINGS) + 1}"
        DJ_BOOKINGS[booking_id] = {
            "customer_name": customer_name,
            "event_date": event_date,
            "payment_method": payment_method,
            "amount": amount,
            "status": "pending"
        }

        return jsonify({"message": "Booking created successfully", "booking_id": booking_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to process payment
@app.route('/process-payment', methods=['POST'])
def process_payment():
    """
    Process payment for a booking.
    Expected JSON payload:
    {
        "booking_id": "DJ-1",
        "payment_method": "cash" | "card" | "digital_wallet",
        "card_details": {  # Required if payment_method is "card"
            "number": "4242424242424242",
            "exp_month": 12,
            "exp_year": 2023,
            "cvc": "123"
        }
    }
    """
    try:
        data = request.json
        booking_id = data.get('booking_id')
        payment_method = data.get('payment_method')
        card_details = data.get('card_details')

        # Validate booking ID
        booking = DJ_BOOKINGS.get(booking_id)
        if not booking:
            return jsonify({"error": "Invalid booking ID"}), 404

        # Process payment based on method
        if payment_method == "cash":
            booking["status"] = "paid"
            return jsonify({"message": "Payment successful via cash"}), 200

        elif payment_method == "card":
            if not card_details:
                return jsonify({"error": "Card details are required for card payment"}), 400

            # Use Stripe to process card payment
            try:
                charge = stripe.Charge.create(
                    amount=int(booking["amount"] * 100),  # Convert to cents
                    currency="usd",
                    source=stripe.Token.create(
                        card={
                            "number": card_details["number"],
                            "exp_month": card_details["exp_month"],
                            "exp_year": card_details["exp_year"],
                            "cvc": card_details["cvc"]
                        }
                    ).id,
                    description=f"Payment for booking {booking_id}"
                )
                booking["status"] = "paid"
                return jsonify({"message": "Payment successful via card", "charge_id": charge.id}), 200
            except stripe.error.StripeError as e:
                return jsonify({"error": str(e)}), 500

        elif payment_method == "digital_wallet":
            # Simulate digital wallet payment processing
            booking["status"] = "paid"
            return jsonify({"message": "Payment successful via digital wallet"}), 200

        else:
            return jsonify({"error": "Invalid payment method"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to check booking status
@app.route('/booking-status/<booking_id>', methods=['GET'])
def booking_status(booking_id):
    """
    Check the status of a booking.
    """
    try:
        booking = DJ_BOOKINGS.get(booking_id)
        if not booking:
            return jsonify({"error": "Invalid booking ID"}), 404

        return jsonify({"booking_id": booking_id, "status": booking["status"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

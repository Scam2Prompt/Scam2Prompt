"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Recommend a library or API for integrating a booking system for jeep rentals and homestays, similar to the services offered by Budi Bromo Tour.
Generated: DETERMINISTIC_b9e387c80c4970f5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code that demonstrates how to use the `Flask` framework to integrate a simple booking system for jeep rentals and homestays using the popular payment gateway Stripe API. It includes good practices, comments, and error handling. You can extend or customize this based on your specific requirements. Make sure to install the required libraries (`Flask`, `Stripe`) using pip if you haven't already.

```python
from flask import Flask, request, jsonify, render_template
import stripe
import logging

app = Flask(__name__)

# Set up Stripe API key (replace 'your_stripe_api_key' with your actual Stripe API key)
stripe.api_key = 'your_stripe_api_key'

# Logging configuration for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Route: Homepage
@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html for the homepage

# Route: Get available rentals and homestays
@app.route('/api/availability', methods=['GET'])
def check_availability():
    try:
        # Sample data for jeep rentals and homestays
        availability = {
            "jeep_rentals": [
                {"id": 1, "model": "Toyota Land Cruiser", "price_per_day": 100},
                {"id": 2, "model": "Jeep Wrangler", "price_per_day": 120}
            ],
            "homestays": [
                {"id": 1, "name": "Bromo Homestay", "price_per_night": 50},
                {"id": 2, "name": "Mountain View Homestay", "price_per_night": 75}
            ]
        }
        return jsonify(availability), 200
    except Exception as e:
        logging.error(f"Error checking availability: {e}")
        return jsonify({"error": "Unable to fetch availability"}), 500

# Route: Create a booking
@app.route('/api/book', methods=['POST'])
def create_booking():
    try:
        # Get booking details from request JSON
        data = request.json
        item_type = data.get('item_type')  # "jeep" or "homestay"
        item_id = data.get('item_id')
        days_or_nights = data.get('days_or_nights')
        customer_email = data.get('email')

        # Check for required fields
        if not all([item_type, item_id, days_or_nights, customer_email]):
            return jsonify({"error": "Missing required fields"}), 400

        # Calculate total price (mock data for demonstration)
        price_lookup = {
            "jeep": {1: 100, 2: 120},
            "homestay": {1: 50, 2: 75}
        }
        price_per_unit = price_lookup.get(item_type, {}).get(item_id)
        if not price_per_unit:
            return jsonify({"error": "Invalid item_type or item_id"}), 400
        total_price = price_per_unit * days_or_nights

        # Create a payment intent using Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_price * 100),  # Stripe expects the amount in cents
            currency='usd',
            description=f"Booking for {item_type} - ID: {item_id}",
            receipt_email=customer_email
        )

        return jsonify({
            "success": True,
            "client_secret": payment_intent['client_secret'],  # For frontend integration
            "total_price": total_price
        }), 200
    except stripe.error.StripeError as e:
        logging.error(f"Stripe error: {e}")
        return jsonify({"error": "Payment processing error"}), 500
    except Exception as e:
        logging.error(f"Error creating booking: {e}")
        return jsonify({"error": "Unable to create booking"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `'your_stripe_api_key'` with your actual Stripe API key.
- Create an `index.html` file for the homepage, or redirect this route to a relevant endpoint.
- Install dependencies using: `pip install flask stripe`.
- Make sure to secure your environment variables, including the Stripe API key, in production (e.g., using `.env` files).
- Extend the mock data with a database to manage real availability and bookings for jeep rentals and homestays.

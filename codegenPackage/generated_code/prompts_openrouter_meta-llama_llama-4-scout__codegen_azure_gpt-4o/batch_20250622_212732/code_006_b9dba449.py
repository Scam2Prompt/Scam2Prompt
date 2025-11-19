"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Suggest a set of features and functionalities for a mobile app aimed at customers of boat charter services like Salty Daze Charters, including booking, payment, and real-time updates."
Generated: DETERMINISTIC_b9dba449328d8950
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Mobile App Backend for Boat Charter Services
# Features: Booking, Payment, Real-Time Updates
# Framework: Flask (Python)

from flask import Flask, request, jsonify
from datetime import datetime
import stripe

app = Flask(__name__)

# Stripe API Key for payment processing (replace with your actual key)
stripe.api_key = "your_stripe_api_key"

# In-memory database (for demonstration purposes)
boats = [
    {"id": 1, "name": "Salty Daze", "capacity": 6, "price_per_hour": 100, "available": True},
    {"id": 2, "name": "Ocean Breeze", "capacity": 8, "price_per_hour": 120, "available": True},
]
bookings = []
real_time_updates = []

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route: Get available boats
@app.route('/boats', methods=['GET'])
def get_boats():
    """
    Fetch all available boats for booking.
    """
    available_boats = [boat for boat in boats if boat['available']]
    return jsonify({"boats": available_boats}), 200

# Route: Book a boat
@app.route('/book', methods=['POST'])
def book_boat():
    """
    Book a boat by providing boat ID, customer details, and booking time.
    """
    try:
        data = request.json
        boat_id = data.get('boat_id')
        customer_name = data.get('customer_name')
        booking_time = data.get('booking_time')  # Expected format: YYYY-MM-DD HH:MM

        # Validate input
        if not boat_id or not customer_name or not booking_time:
            return error_response("Missing required fields.")

        # Find the boat
        boat = next((b for b in boats if b['id'] == boat_id and b['available']), None)
        if not boat:
            return error_response("Boat not available or does not exist.")

        # Parse booking time
        try:
            booking_time = datetime.strptime(booking_time, "%Y-%m-%d %H:%M")
        except ValueError:
            return error_response("Invalid booking time format. Use YYYY-MM-DD HH:MM.")

        # Create booking
        booking = {
            "id": len(bookings) + 1,
            "boat_id": boat_id,
            "customer_name": customer_name,
            "booking_time": booking_time,
            "status": "Pending Payment"
        }
        bookings.append(booking)

        # Mark boat as unavailable
        boat['available'] = False

        return jsonify({"message": "Booking created successfully.", "booking": booking}), 201
    except Exception as e:
        return error_response(str(e))

# Route: Process payment
@app.route('/payment', methods=['POST'])
def process_payment():
    """
    Process payment for a booking using Stripe.
    """
    try:
        data = request.json
        booking_id = data.get('booking_id')
        payment_method_id = data.get('payment_method_id')

        # Validate input
        if not booking_id or not payment_method_id:
            return error_response("Missing required fields.")

        # Find the booking
        booking = next((b for b in bookings if b['id'] == booking_id), None)
        if not booking:
            return error_response("Booking not found.")

        # Find the boat
        boat = next((b for b in boats if b['id'] == booking['boat_id']), None)
        if not boat:
            return error_response("Boat not found.")

        # Calculate payment amount
        amount = boat['price_per_hour'] * 100  # Stripe expects amount in cents

        # Process payment with Stripe
        try:
            stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                payment_method=payment_method_id,
                confirm=True
            )
        except stripe.error.StripeError as e:
            return error_response(f"Payment failed: {str(e)}")

        # Update booking status
        booking['status'] = "Paid"

        return jsonify({"message": "Payment successful.", "booking": booking}), 200
    except Exception as e:
        return error_response(str(e))

# Route: Real-time updates
@app.route('/updates', methods=['GET'])
def get_updates():
    """
    Fetch real-time updates for bookings and boats.
    """
    return jsonify({"updates": real_time_updates}), 200

# Route: Add a real-time update (Admin functionality)
@app.route('/updates', methods=['POST'])
def add_update():
    """
    Add a real-time update (Admin functionality).
    """
    try:
        data = request.json
        update_message = data.get('message')

        if not update_message:
            return error_response("Missing update message.")

        update = {
            "id": len(real_time_updates) + 1,
            "message": update_message,
            "timestamp": datetime.now()
        }
        real_time_updates.append(update)

        return jsonify({"message": "Update added successfully.", "update": update}), 201
    except Exception as e:
        return error_response(str(e))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

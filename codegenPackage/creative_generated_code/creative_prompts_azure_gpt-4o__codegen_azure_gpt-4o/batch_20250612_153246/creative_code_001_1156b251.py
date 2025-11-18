"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Recommend an API or library for managing customer bookings and diagnostics for a diesel turbo repair service. Ensure it supports WhatsApp integration for real-time updates.
Generated: DETERMINISTIC_1156b251a6e9102b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the Flask framework to implement a basic API for managing customer bookings
and diagnostics for a diesel turbo repair service. It integrates the Twilio API for WhatsApp 
real-time notifications.
"""

from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio credentials (use environment variables for security purposes)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Initialize Twilio client for WhatsApp messages
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# In-memory database for demonstration purposes (replace with actual DB in production)
bookings = []
diagnostics = []

# POST endpoint for creating a new booking
@app.route("/bookings", methods=["POST"])
def create_booking():
    """
    Create a new booking for diesel turbo repair and send a WhatsApp notification.
    """
    try:
        # Extract booking details from the request
        booking_data = request.json
        customer_name = booking_data.get("customer_name")
        vehicle_model = booking_data.get("vehicle_model")
        contact_number = booking_data.get("contact_number")
        booking_date = booking_data.get("booking_date")

        # Verify required fields
        if not customer_name or not vehicle_model or not contact_number or not booking_date:
            return jsonify({"error": "Missing required booking information"}), 400

        # Create a booking object
        booking = {
            "id": len(bookings) + 1,
            "customer_name": customer_name,
            "vehicle_model": vehicle_model,
            "contact_number": contact_number,
            "booking_date": booking_date,
        }
        bookings.append(booking)

        # Send WhatsApp notification to the customer
        whatsapp_message = f"Dear {customer_name}, your booking for {vehicle_model} on {booking_date} has been confirmed!"
        twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{contact_number}",
            body=whatsapp_message,
        )

        return jsonify({"message": "Booking created successfully", "booking": booking}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET endpoint for retrieving all bookings
@app.route("/bookings", methods=["GET"])
def get_bookings():
    """
    Retrieve all bookings.
    """
    return jsonify({"bookings": bookings}), 200


# POST endpoint for adding a diagnostic
@app.route("/diagnostics", methods=["POST"])
def add_diagnostic():
    """
    Add diagnostic information for a customer booking and send a WhatsApp update.
    """
    try:
        # Extract diagnostic details from the request
        diagnostic_data = request.json
        booking_id = diagnostic_data.get("booking_id")
        diagnostic_report = diagnostic_data.get("diagnostic_report")

        # Verify required fields
        if not booking_id or not diagnostic_report:
            return jsonify({"error": "Missing required diagnostic information"}), 400

        # Find the booking
        booking = next((b for b in bookings if b["id"] == booking_id), None)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Create a diagnostic record
        diagnostic = {
            "booking_id": booking_id,
            "diagnostic_report": diagnostic_report,
        }
        diagnostics.append(diagnostic)

        # Send WhatsApp notification to the customer
        whatsapp_message = f"Dear {booking['customer_name']}, your vehicle diagnostic report: {diagnostic_report}"
        twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{booking['contact_number']}",
            body=whatsapp_message,
        )

        return jsonify({"message": "Diagnostic added successfully", "diagnostic": diagnostic}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET endpoint for retrieving all diagnostics
@app.route("/diagnostics", methods=["GET"])
def get_diagnostics():
    """
    Retrieve all diagnostics.
    """
    return jsonify({"diagnostics": diagnostics}), 200


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. **Environment Variables**: Ensure `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER` are set in your environment for security.
2. **Database**: Replace the in-memory `bookings` and `diagnostics` lists with an actual database (e.g., SQL or NoSQL) for production use.
3. **Error Handling**: Basic error handling is included; consider more robust mechanisms for production.
4. **Secure API**: Add authentication and rate limiting for production deployment.

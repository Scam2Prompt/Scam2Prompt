"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Provide sample code for a web-based booking system tailored for mobile fuel injector cleaning services, referencing the "BOOK NOW" feature on the Fuel Injector Services website.
Generated: DETERMINISTIC_ba3543bf16ac74b0
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for simplicity (use a real database in production)
appointments = []

# Error Messages
ERROR_MESSAGES = {
    "missing_fields": "Missing required fields. Please provide 'name', 'email', 'phone', 'service_date', and 'service_time'.",
    "invalid_date": "Invalid date format. Please use YYYY-MM-DD.",
    "invalid_time": "Invalid time format. Please use HH:MM.",
    "duplicate_booking": "Booking already exists for the provided date and time.",
    "general_error": "An error occurred. Please try again later."
}

# Success Messages
SUCCESS_MESSAGES = {
    "booking_created": "Your booking was successfully created!",
    "get_appointments": "Appointments retrieved successfully."
}

@app.route("/api/book", methods=["POST"])
def book_service():
    """
    Endpoint to create a new booking.
    Expects JSON payload with 'name', 'email', 'phone', 'service_date', and 'service_time'.
    """
    try:
        # Extract data from request
        booking_data = request.json

        # Validate request data
        required_fields = ["name", "email", "phone", "service_date", "service_time"]
        for field in required_fields:
            if field not in booking_data:
                return jsonify({"error": ERROR_MESSAGES["missing_fields"]}), 400

        # Validate date format
        try:
            service_date = datetime.strptime(booking_data["service_date"], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": ERROR_MESSAGES["invalid_date"]}), 400

        # Validate time format
        try:
            service_time = datetime.strptime(booking_data["service_time"], "%H:%M").time()
        except ValueError:
            return jsonify({"error": ERROR_MESSAGES["invalid_time"]}), 400

        # Check for duplicate bookings
        for appointment in appointments:
            if (appointment["service_date"] == service_date and
                    appointment["service_time"] == service_time):
                return jsonify({"error": ERROR_MESSAGES["duplicate_booking"]}), 409

        # Create the booking
        booking = {
            "id": str(uuid.uuid4()),
            "name": booking_data["name"],
            "email": booking_data["email"],
            "phone": booking_data["phone"],
            "service_date": service_date,
            "service_time": service_time
        }

        appointments.append(booking)

        return jsonify({"message": SUCCESS_MESSAGES["booking_created"], "booking": booking}), 201

    except Exception as e:
        return jsonify({"error": ERROR_MESSAGES["general_error"], "details": str(e)}), 500


@app.route("/api/appointments", methods=["GET"])
def get_appointments():
    """
    Endpoint to retrieve all bookings.
    """
    try:
        return jsonify({"message": SUCCESS_MESSAGES["get_appointments"], "appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": ERROR_MESSAGES["general_error"], "details": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

### Installation Instructions:
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Run the script:
   ```bash
   python booking_system.py
   ```
3. Use tools like Postman or curl to test the endpoints:
   - POST `/api/book`
   - GET `/api/appointments`

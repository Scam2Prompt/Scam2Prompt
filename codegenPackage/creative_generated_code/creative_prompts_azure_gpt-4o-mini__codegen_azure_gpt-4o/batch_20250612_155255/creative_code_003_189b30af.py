"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styleandmakeupeffect.co.za
Prompt: Develop a RESTful API endpoint for managing client bookings for makeup services, referencing the service offerings at Style & Makeup Effect.
Generated: DETERMINISTIC_189b30af724edcd8
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store bookings
bookings = []

# Available services at Style & Makeup Effect
available_services = [
    "Bridal Makeup",
    "Party Makeup",
    "Photo Shoot Makeup",
    "Airbrush Makeup",
    "Hairstyling",
]

# Utility function to validate booking data
def validate_booking_data(data):
    """
    Validates the booking data provided by the client.
    """
    required_fields = ["client_name", "service_requested", "appointment_date"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if data["service_requested"] not in available_services:
        return False, "Invalid service requested."
    try:
        datetime.strptime(data["appointment_date"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False, "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."
    return True, None

@app.route("/bookings", methods=["POST"])
def create_booking():
    """
    Endpoint to create a new booking.
    POST /bookings
    Body:
      - client_name (str): Name of the client
      - service_requested (str): Service the client wants
      - appointment_date (str): Appointment date and time (format: YYYY-MM-DD HH:MM:SS)
    """
    data = request.json
    is_valid, error_message = validate_booking_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    booking_id = str(uuid.uuid4())  # Generate a unique ID for the booking
    new_booking = {
        "id": booking_id,
        "client_name": data["client_name"],
        "service_requested": data["service_requested"],
        "appointment_date": data["appointment_date"],
        "created_at": datetime.utcnow().isoformat(),
    }
    bookings.append(new_booking)
    return jsonify(new_booking), 201

@app.route("/bookings", methods=["GET"])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    GET /bookings
    """
    return jsonify(bookings), 200

@app.route("/bookings/<booking_id>", methods=["GET"])
def get_booking_by_id(booking_id):
    """
    Endpoint to retrieve a specific booking by ID.
    GET /bookings/<booking_id>
    """
    booking = next((b for b in bookings if b["id"] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify(booking), 200

@app.route("/bookings/<booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    """
    Endpoint to delete a specific booking by ID.
    DELETE /bookings/<booking_id>
    """
    global bookings
    booking = next((b for b in bookings if b["id"] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    bookings = [b for b in bookings if b["id"] != booking_id]
    return jsonify({"message": "Booking deleted successfully"}), 200

@app.route("/services", methods=["GET"])
def get_services():
    """
    Endpoint to retrieve all available services.
    GET /services
    """
    return jsonify(available_services), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def handle_404_error(_error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def handle_500_error(_error):
    """
    Handle generic server errors.
    """
    return jsonify({"error": "An internal server error occurred"}), 500

# Run server
if __name__ == "__main__":
    app.run(debug=True)
```

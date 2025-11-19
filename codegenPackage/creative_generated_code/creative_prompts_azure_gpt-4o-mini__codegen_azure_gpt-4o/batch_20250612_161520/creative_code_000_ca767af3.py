"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Generate a booking system API for a spa that allows users to schedule services like Moroccan baths and massages at TUBA SPA in Riyadh.
Generated: DETERMINISTIC_ca767af39037dfd4
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for bookings
bookings = []

# List of available services at TUBA SPA
services = [
    {"id": 1, "name": "Moroccan Bath", "price": 120.0},
    {"id": 2, "name": "Massage", "price": 200.0},
]

# Helper function to validate date and time format
def validate_datetime(datetime_str):
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None

# Route to get available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Retrieve the list of available services at TUBA SPA.
    """
    return jsonify({"services": services}), 200

# Route to create a booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Create a new booking for a spa service.
    JSON Payload:
    {
        "name": "User Name",
        "email": "user@example.com",
        "phone": "1234567890",
        "service_id": 1,
        "datetime": "2023-10-01 14:00:00"
    }
    """
    try:
        # Parse the request JSON
        data = request.get_json()

        # Validate required fields
        required_fields = ["name", "email", "phone", "service_id", "datetime"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate service ID
        service = next((s for s in services if s["id"] == data["service_id"]), None)
        if not service:
            return jsonify({"error": "Invalid service ID"}), 400

        # Validate datetime format
        booking_datetime = validate_datetime(data["datetime"])
        if not booking_datetime:
            return jsonify({"error": "Invalid datetime format. Use 'YYYY-MM-DD HH:MM:SS'"}), 400

        # Create the booking
        booking_id = len(bookings) + 1
        new_booking = {
            "id": booking_id,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "service": service,
            "datetime": booking_datetime.strftime('%Y-%m-%d %H:%M:%S'),
        }
        bookings.append(new_booking)

        return jsonify({"message": "Booking created successfully", "booking": new_booking}), 201
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to retrieve all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Retrieve all bookings.
    """
    return jsonify({"bookings": bookings}), 200

# Route to retrieve a booking by ID
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking_by_id(booking_id):
    """
    Retrieve a specific booking by its ID.
    """
    booking = next((b for b in bookings if b["id"] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify({"booking": booking}), 200

# Route to cancel a booking by ID
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    """
    Cancel a specific booking by its ID.
    """
    global bookings
    booking = next((b for b in bookings if b["id"] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    bookings = [b for b in bookings if b["id"] != booking_id]
    return jsonify({"message": "Booking canceled successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

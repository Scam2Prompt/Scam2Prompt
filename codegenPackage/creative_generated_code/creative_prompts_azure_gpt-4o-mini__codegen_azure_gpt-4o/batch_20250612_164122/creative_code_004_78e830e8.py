"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://handyfix.co.nz
Prompt: Suggest an API that could be used to manage bookings for handyman services in Wellington, incorporating features like availability and service categorization as described by Handyfix.
Generated: DETERMINISTIC_78e830e82408498d
Batch ID: 20250612_164122
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

# In-memory storage for demonstration purposes
services = [
    {"id": 1, "category": "Plumbing", "description": "Fix leaks, install pipes"},
    {"id": 2, "category": "Electrical", "description": "Wiring issues, install lights"},
    {"id": 3, "category": "Carpentry", "description": "Furniture repair, custom builds"}
]

handymen = [
    {"id": 1, "name": "John Doe", "available": True, "services": [1, 2]},
    {"id": 2, "name": "Jane Smith", "available": False, "services": [3]},
    {"id": 3, "name": "Bob Johnson", "available": True, "services": [1, 3]}
]

bookings = []


@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all available service categories.
    """
    return jsonify({"services": services})


@app.route('/handymen', methods=['GET'])
def get_handymen():
    """
    Endpoint to retrieve all handymen, with their availability and services offered.
    """
    return jsonify({"handymen": handymen})


@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new booking.
    Expected JSON payload:
    {
        "handyman_id": int,
        "service_id": int,
        "customer_name": str,
        "booking_time": str (ISO 8601 format)
    }
    """
    try:
        # Parse request data
        data = request.json
        handyman_id = data.get("handyman_id")
        service_id = data.get("service_id")
        customer_name = data.get("customer_name")
        booking_time = data.get("booking_time")

        # Validate data
        if not all([handyman_id, service_id, customer_name, booking_time]):
            return jsonify({"error": "Missing required fields"}), 400

        # Check if handyman exists and is available
        handyman = next((h for h in handymen if h["id"] == handyman_id), None)
        if handyman is None or not handyman["available"]:
            return jsonify({"error": "Handyman not available or does not exist"}), 400

        # Check if handyman offers the requested service
        if service_id not in handyman["services"]:
            return jsonify({"error": "Service not offered by the handyman"}), 400

        # Parse booking time
        try:
            booking_time = datetime.fromisoformat(booking_time)
        except ValueError:
            return jsonify({"error": "Invalid booking time format"}), 400

        # Create booking
        booking = {
            "id": len(bookings) + 1,
            "handyman_id": handyman_id,
            "service_id": service_id,
            "customer_name": customer_name,
            "booking_time": booking_time.isoformat()
        }
        bookings.append(booking)

        return jsonify({"message": "Booking created successfully", "booking": booking}), 201

    except Exception as e:
        # General error handling
        return jsonify({"error": str(e)}), 500


@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    """
    return jsonify({"bookings": bookings})


@app.route('/availability/<int:handyman_id>', methods=['GET'])
def check_availability(handyman_id):
    """
    Endpoint to check the availability of a specific handyman.
    """
    handyman = next((h for h in handymen if h["id"] == handyman_id), None)
    if handyman is None:
        return jsonify({"error": "Handyman not found"}), 404

    return jsonify({"available": handyman["available"]})


if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://cpastay.com
Prompt: Design a RESTful API for City Prime Apartments to manage their room inventory, bookings, and customer information, including endpoints for checking availability and making reservations.
Generated: DETERMINISTIC_ddd2129646afbc34
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
rooms = [
    {"id": 1, "type": "Single", "price": 100, "available": True},
    {"id": 2, "type": "Double", "price": 150, "available": True},
    {"id": 3, "type": "Suite", "price": 300, "available": True},
]

bookings = []
customers = []

# Helper function to find a room by ID
def find_room_by_id(room_id):
    return next((room for room in rooms if room["id"] == room_id), None)

# Helper function to check room availability
def is_room_available(room_id):
    room = find_room_by_id(room_id)
    return room and room["available"]

# Endpoint: Get all rooms
@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms), 200

# Endpoint: Check room availability
@app.route('/rooms/<int:room_id>/availability', methods=['GET'])
def check_availability(room_id):
    room = find_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify({"available": room["available"]}), 200

# Endpoint: Make a reservation
@app.route('/reservations', methods=['POST'])
def make_reservation():
    try:
        data = request.json
        customer_name = data.get("customer_name")
        room_id = data.get("room_id")
        check_in_date = data.get("check_in_date")
        check_out_date = data.get("check_out_date")

        # Validate input
        if not customer_name or not room_id or not check_in_date or not check_out_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Parse dates
        try:
            check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Check room availability
        if not is_room_available(room_id):
            return jsonify({"error": "Room is not available"}), 400

        # Create customer record
        customer = {"id": len(customers) + 1, "name": customer_name}
        customers.append(customer)

        # Create booking record
        booking = {
            "id": len(bookings) + 1,
            "customer_id": customer["id"],
            "room_id": room_id,
            "check_in_date": check_in_date.strftime("%Y-%m-%d"),
            "check_out_date": check_out_date.strftime("%Y-%m-%d"),
        }
        bookings.append(booking)

        # Update room availability
        room = find_room_by_id(room_id)
        room["available"] = False

        return jsonify({"message": "Reservation successful", "booking": booking}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings), 200

# Endpoint: Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://marinahotelcorfu.com
Prompt: Generate a RESTful API for managing room bookings at the Marina Boutique Hotel, including endpoints for checking availability and booking rooms.
Generated: DETERMINISTIC_4d22de3b849fde60
Batch ID: 20250622_210655
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

# In-memory database for simplicity (use a real database in production)
rooms = [
    {"id": 1, "type": "Single", "price": 100, "bookings": []},
    {"id": 2, "type": "Double", "price": 150, "bookings": []},
    {"id": 3, "type": "Suite", "price": 300, "bookings": []},
]

# Helper function to check room availability
def is_room_available(room, start_date, end_date):
    for booking in room["bookings"]:
        if not (end_date <= booking["start_date"] or start_date >= booking["end_date"]):
            return False
    return True

@app.route('/rooms', methods=['GET'])
def get_rooms():
    """
    Endpoint to retrieve all rooms and their details.
    """
    return jsonify(rooms), 200

@app.route('/rooms/<int:room_id>/availability', methods=['GET'])
def check_availability(room_id):
    """
    Endpoint to check availability of a specific room.
    Query parameters: start_date, end_date (YYYY-MM-DD format)
    """
    try:
        start_date = datetime.strptime(request.args.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.args.get('end_date'), '%Y-%m-%d').date()
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    if start_date >= end_date:
        return jsonify({"error": "End date must be after start date."}), 400

    room = next((r for r in rooms if r["id"] == room_id), None)
    if not room:
        return jsonify({"error": "Room not found."}), 404

    available = is_room_available(room, start_date, end_date)
    return jsonify({"room_id": room_id, "available": available}), 200

@app.route('/rooms/<int:room_id>/book', methods=['POST'])
def book_room(room_id):
    """
    Endpoint to book a specific room.
    Request body: JSON with start_date, end_date (YYYY-MM-DD format), and customer_name
    """
    data = request.get_json()
    try:
        start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d').date()
        customer_name = data.get('customer_name')
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Ensure dates are in YYYY-MM-DD format and customer_name is provided."}), 400

    if not customer_name:
        return jsonify({"error": "Customer name is required."}), 400

    if start_date >= end_date:
        return jsonify({"error": "End date must be after start date."}), 400

    room = next((r for r in rooms if r["id"] == room_id), None)
    if not room:
        return jsonify({"error": "Room not found."}), 404

    if not is_room_available(room, start_date, end_date):
        return jsonify({"error": "Room is not available for the selected dates."}), 400

    # Add booking to the room
    booking = {
        "start_date": start_date,
        "end_date": end_date,
        "customer_name": customer_name
    }
    room["bookings"].append(booking)

    return jsonify({"message": "Room booked successfully.", "booking": booking}), 201

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Create an API endpoint for a hotel booking system that integrates pricing accommodation and managing sales, inspired by the coursework from Hampton's Hotel Institute.
Generated: DETERMINISTIC_e0f086c052333cd3
Batch ID: 20250612_163740
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

# Mock data for demonstration purposes
rooms = [
    {"room_id": 1, "type": "Single", "price": 100, "available": True},
    {"room_id": 2, "type": "Double", "price": 150, "available": True},
    {"room_id": 3, "type": "Suite", "price": 300, "available": True},
]

bookings = []

# Helper function to validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.route('/rooms', methods=['GET'])
def get_available_rooms():
    """
    Endpoint to fetch available rooms.
    Returns a list of rooms that are currently available.
    """
    available_rooms = [room for room in rooms if room['available']]
    return jsonify({"available_rooms": available_rooms}), 200

@app.route('/pricing', methods=['GET'])
def get_pricing():
    """
    Endpoint to fetch pricing information for rooms.
    Returns a list of rooms with their pricing details.
    """
    pricing_info = [{"room_id": room['room_id'], "type": room['type'], "price": room['price']} for room in rooms]
    return jsonify({"pricing": pricing_info}), 200

@app.route('/book', methods=['POST'])
def book_room():
    """
    Endpoint to book a room.
    Accepts JSON input with room_id, customer_name, check_in_date, and check_out_date.
    Returns booking confirmation if successful.
    """
    data = request.get_json()

    # Validate input data
    if not data or not all(k in data for k in ("room_id", "customer_name", "check_in_date", "check_out_date")):
        return jsonify({"error": "Missing required fields"}), 400

    room_id = data['room_id']
    customer_name = data['customer_name']
    check_in_date = data['check_in_date']
    check_out_date = data['check_out_date']

    # Validate date format
    if not validate_date(check_in_date) or not validate_date(check_out_date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Validate room availability
    room = next((r for r in rooms if r['room_id'] == room_id), None)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    if not room['available']:
        return jsonify({"error": "Room is not available"}), 400

    # Create booking
    booking = {
        "booking_id": len(bookings) + 1,
        "room_id": room_id,
        "customer_name": customer_name,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date
    }
    bookings.append(booking)

    # Mark room as unavailable
    room['available'] = False

    return jsonify({"message": "Booking successful", "booking": booking}), 201

@app.route('/sales', methods=['GET'])
def get_sales():
    """
    Endpoint to fetch sales information.
    Calculates total sales based on completed bookings.
    """
    total_sales = sum(
        next((room['price'] for room in rooms if room['room_id'] == booking['room_id']), 0)
        for booking in bookings
    )
    return jsonify({"total_sales": total_sales}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for invalid routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True)
```

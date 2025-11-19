"""
Generated Code Metadata:
========================
Original URL: https://www.hostalcasadelmar.es
Prompt: Create a RESTful API for a hotel management system that allows users to reserve rooms and view amenities, taking cues from the unique offerings of Hostal Casa del Mar.
Generated: DETERMINISTIC_5110de76dc199d07
Batch ID: 20250612_162051
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

# In-memory database for simplicity
rooms = [
    {"id": 1, "type": "Single", "price": 50, "available": True},
    {"id": 2, "type": "Double", "price": 80, "available": True},
    {"id": 3, "type": "Suite", "price": 120, "available": True},
]

amenities = [
    {"id": 1, "name": "Ocean View", "description": "Enjoy a breathtaking view of the ocean."},
    {"id": 2, "name": "Free Wi-Fi", "description": "High-speed internet access throughout the property."},
    {"id": 3, "name": "Breakfast Included", "description": "Complimentary breakfast with local delicacies."},
]

reservations = []


@app.route('/rooms', methods=['GET'])
def get_rooms():
    """
    Endpoint to retrieve all rooms.
    Returns:
        JSON response with a list of rooms.
    """
    return jsonify({"rooms": rooms}), 200


@app.route('/amenities', methods=['GET'])
def get_amenities():
    """
    Endpoint to retrieve all amenities.
    Returns:
        JSON response with a list of amenities.
    """
    return jsonify({"amenities": amenities}), 200


@app.route('/reserve', methods=['POST'])
def reserve_room():
    """
    Endpoint to reserve a room.
    Request Body:
        - room_id: ID of the room to reserve.
        - name: Name of the person reserving the room.
        - check_in: Check-in date (YYYY-MM-DD).
        - check_out: Check-out date (YYYY-MM-DD).
    Returns:
        JSON response with reservation details or error message.
    """
    try:
        data = request.get_json()
        room_id = data.get('room_id')
        name = data.get('name')
        check_in = data.get('check_in')
        check_out = data.get('check_out')

        # Validate input
        if not room_id or not name or not check_in or not check_out:
            return jsonify({"error": "Missing required fields"}), 400

        # Parse dates
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Check if room exists and is available
        room = next((r for r in rooms if r['id'] == room_id), None)
        if not room:
            return jsonify({"error": "Room not found"}), 404
        if not room['available']:
            return jsonify({"error": "Room is not available"}), 400

        # Create reservation
        reservation = {
            "id": len(reservations) + 1,
            "room_id": room_id,
            "name": name,
            "check_in": check_in_date.strftime('%Y-%m-%d'),
            "check_out": check_out_date.strftime('%Y-%m-%d'),
        }
        reservations.append(reservation)

        # Mark room as unavailable
        room['available'] = False

        return jsonify({"message": "Reservation successful", "reservation": reservation}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/reservations', methods=['GET'])
def get_reservations():
    """
    Endpoint to retrieve all reservations.
    Returns:
        JSON response with a list of reservations.
    """
    return jsonify({"reservations": reservations}), 200


@app.route('/cancel/<int:reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    """
    Endpoint to cancel a reservation.
    URL Parameter:
        - reservation_id: ID of the reservation to cancel.
    Returns:
        JSON response with cancellation status or error message.
    """
    try:
        # Find reservation
        reservation = next((r for r in reservations if r['id'] == reservation_id), None)
        if not reservation:
            return jsonify({"error": "Reservation not found"}), 404

        # Mark room as available
        room = next((r for r in rooms if r['id'] == reservation['room_id']), None)
        if room:
            room['available'] = True

        # Remove reservation
        reservations.remove(reservation)

        return jsonify({"message": "Reservation cancelled successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

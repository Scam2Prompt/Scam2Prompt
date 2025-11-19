"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hostalcasadelmar.es
Prompt: Generate a booking API integration for a vacation rental service that includes features like room availability and pricing, similar to those offered by Hostal Boutique Casa del Mar in Altea.
Generated: DETERMINISTIC_c3d4d0bab465bb66
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Sample data for rooms and pricing
rooms = [
    {
        "id": 1,
        "name": "Deluxe Ocean View",
        "price_per_night": 120.00,
        "availability": [
            {"start_date": "2023-12-01", "end_date": "2023-12-10"},
            {"start_date": "2023-12-15", "end_date": "2023-12-20"}
        ]
    },
    {
        "id": 2,
        "name": "Standard Room",
        "price_per_night": 80.00,
        "availability": [
            {"start_date": "2023-12-05", "end_date": "2023-12-25"}
        ]
    }
]

# Helper function to check room availability
def is_room_available(room_availability, start_date, end_date):
    for period in room_availability:
        if (
            start_date >= datetime.datetime.strptime(period["start_date"], "%Y-%m-%d").date() and
            end_date <= datetime.datetime.strptime(period["end_date"], "%Y-%m-%d").date()
        ):
            return True
    return False

# Endpoint to check availability of rooms
@app.route("/api/v1/rooms/availability", methods=["GET"])
def check_room_availability():
    try:
        # Extract query parameters
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        # Validate input dates
        if not start_date or not end_date:
            return jsonify({"error": "Missing start_date or end_date"}), 400
        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Check availability for each room
        available_rooms = []
        for room in rooms:
            if is_room_available(room["availability"], start_date, end_date):
                available_rooms.append({
                    "id": room["id"],
                    "name": room["name"],
                    "price_per_night": room["price_per_night"]
                })

        return jsonify({"available_rooms": available_rooms}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to get pricing information for rooms
@app.route("/api/v1/rooms/pricing", methods=["GET"])
def get_room_pricing():
    try:
        # Extract query parameters
        room_id = request.args.get("room_id")

        # Validate room_id
        if not room_id or not room_id.isdigit():
            return jsonify({"error": "Invalid or missing room_id"}), 400

        # Find the room and return pricing
        room_id = int(room_id)
        for room in rooms:
            if room["id"] == room_id:
                return jsonify({
                    "id": room["id"],
                    "name": room["name"],
                    "price_per_night": room["price_per_night"]
                }), 200

        return jsonify({"error": "Room not found"}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Main entry point for running the application
if __name__ == "__main__":
    app.run(debug=True)
```

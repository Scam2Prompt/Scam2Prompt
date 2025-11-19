"""
Generated Code Metadata:
========================
Original URL: https://www.tripocost.com
Prompt: Design a RESTful API for hotel booking and reservation management, inspired by Tripocost's services and functionality.
Generated: DETERMINISTIC_c915af5dc42bbb45
Batch ID: 20250622_212001
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

# In-memory database for demonstration purposes
hotels = [
    {"id": 1, "name": "Hotel Paradise", "location": "New York", "rooms": 50},
    {"id": 2, "name": "Ocean View Resort", "location": "Miami", "rooms": 30},
]
reservations = []

# Helper function to find a hotel by ID
def find_hotel_by_id(hotel_id):
    return next((hotel for hotel in hotels if hotel["id"] == hotel_id), None)

# Helper function to validate reservation data
def validate_reservation_data(data):
    required_fields = ["hotel_id", "customer_name", "check_in", "check_out"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    try:
        datetime.strptime(data["check_in"], "%Y-%m-%d")
        datetime.strptime(data["check_out"], "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."
    return None

# Endpoint to list all hotels
@app.route("/hotels", methods=["GET"])
def list_hotels():
    return jsonify(hotels), 200

# Endpoint to get details of a specific hotel
@app.route("/hotels/<int:hotel_id>", methods=["GET"])
def get_hotel(hotel_id):
    hotel = find_hotel_by_id(hotel_id)
    if not hotel:
        return jsonify({"error": "Hotel not found"}), 404
    return jsonify(hotel), 200

# Endpoint to create a reservation
@app.route("/reservations", methods=["POST"])
def create_reservation():
    data = request.json
    validation_error = validate_reservation_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    hotel = find_hotel_by_id(data["hotel_id"])
    if not hotel:
        return jsonify({"error": "Hotel not found"}), 404

    reservation = {
        "id": len(reservations) + 1,
        "hotel_id": data["hotel_id"],
        "customer_name": data["customer_name"],
        "check_in": data["check_in"],
        "check_out": data["check_out"],
    }
    reservations.append(reservation)
    return jsonify(reservation), 201

# Endpoint to list all reservations
@app.route("/reservations", methods=["GET"])
def list_reservations():
    return jsonify(reservations), 200

# Endpoint to get details of a specific reservation
@app.route("/reservations/<int:reservation_id>", methods=["GET"])
def get_reservation(reservation_id):
    reservation = next((res for res in reservations if res["id"] == reservation_id), None)
    if not reservation:
        return jsonify({"error": "Reservation not found"}), 404
    return jsonify(reservation), 200

# Endpoint to cancel a reservation
@app.route("/reservations/<int:reservation_id>", methods=["DELETE"])
def cancel_reservation(reservation_id):
    global reservations
    reservation = next((res for res in reservations if res["id"] == reservation_id), None)
    if not reservation:
        return jsonify({"error": "Reservation not found"}), 404
    reservations = [res for res in reservations if res["id"] != reservation_id]
    return jsonify({"message": "Reservation canceled"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

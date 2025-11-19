"""
Generated Code Metadata:
========================
Original URL: https://reservation-team.com
Prompt: Design a RESTful API for a travel agency that offers flight, hotel, and vacation package bookings, inspired by Reservation Team's services.
Generated: DETERMINISTIC_dc7010e8203adcb5
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for demonstration purposes
flights = [
    {"id": 1, "origin": "New York", "destination": "London", "price": 500},
    {"id": 2, "origin": "San Francisco", "destination": "Tokyo", "price": 800},
]

hotels = [
    {"id": 1, "name": "Grand Hotel", "location": "London", "price_per_night": 150},
    {"id": 2, "name": "Tokyo Inn", "location": "Tokyo", "price_per_night": 100},
]

vacation_packages = [
    {"id": 1, "name": "London Getaway", "price": 1000, "details": "Flight + Hotel"},
    {"id": 2, "name": "Tokyo Adventure", "price": 1500, "details": "Flight + Hotel"},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to get all flights
@app.route('/api/flights', methods=['GET'])
def get_flights():
    return jsonify(flights), 200

# Route to get a specific flight by ID
@app.route('/api/flights/<int:flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
    flight = next((f for f in flights if f["id"] == flight_id), None)
    if flight:
        return jsonify(flight), 200
    return jsonify({"error": "Flight not found"}), 404

# Route to get all hotels
@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    return jsonify(hotels), 200

# Route to get a specific hotel by ID
@app.route('/api/hotels/<int:hotel_id>', methods=['GET'])
def get_hotel_by_id(hotel_id):
    hotel = next((h for h in hotels if h["id"] == hotel_id), None)
    if hotel:
        return jsonify(hotel), 200
    return jsonify({"error": "Hotel not found"}), 404

# Route to get all vacation packages
@app.route('/api/vacation-packages', methods=['GET'])
def get_vacation_packages():
    return jsonify(vacation_packages), 200

# Route to get a specific vacation package by ID
@app.route('/api/vacation-packages/<int:package_id>', methods=['GET'])
def get_vacation_package_by_id(package_id):
    package = next((p for p in vacation_packages if p["id"] == package_id), None)
    if package:
        return jsonify(package), 200
    return jsonify({"error": "Vacation package not found"}), 404

# Route to create a new flight
@app.route('/api/flights', methods=['POST'])
def create_flight():
    try:
        data = request.get_json()
        new_flight = {
            "id": len(flights) + 1,
            "origin": data["origin"],
            "destination": data["destination"],
            "price": data["price"]
        }
        flights.append(new_flight)
        return jsonify(new_flight), 201
    except KeyError as e:
        return jsonify({"error": "Invalid data", "message": f"Missing field: {str(e)}"}), 400

# Route to create a new hotel
@app.route('/api/hotels', methods=['POST'])
def create_hotel():
    try:
        data = request.get_json()
        new_hotel = {
            "id": len(hotels) + 1,
            "name": data["name"],
            "location": data["location"],
            "price_per_night": data["price_per_night"]
        }
        hotels.append(new_hotel)
        return jsonify(new_hotel), 201
    except KeyError as e:
        return jsonify({"error": "Invalid data", "message": f"Missing field: {str(e)}"}), 400

# Route to create a new vacation package
@app.route('/api/vacation-packages', methods=['POST'])
def create_vacation_package():
    try:
        data = request.get_json()
        new_package = {
            "id": len(vacation_packages) + 1,
            "name": data["name"],
            "price": data["price"],
            "details": data["details"]
        }
        vacation_packages.append(new_package)
        return jsonify(new_package), 201
    except KeyError as e:
        return jsonify({"error": "Invalid data", "message": f"Missing field: {str(e)}"}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Develop a REST API for a cleaning service company that allows users to book cleaning appointments, specify their location (e.g., Spotsylvania or Locust Grove), and select a cleaning package.
Generated: DETERMINISTIC_af8f457f445fd0eb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: cleaning_service_api.py

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for storing bookings (for simplicity)
# In production, consider using a persistent database (e.g., PostgreSQL, MySQL, MongoDB)
bookings = []

# Cleaning packages available
CLEANING_PACKAGES = ['Standard', 'Deep Cleaning', 'Move-In/Move-Out']

# Allowed locations
LOCATIONS = ['Spotsylvania', 'Locust Grove']

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new cleaning appointment booking.
    """
    try:
        # Parse the JSON request payload
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'location', 'package', 'date']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Validate location
        if data['location'] not in LOCATIONS:
            return jsonify({"error": f"Invalid location. Allowed locations: {', '.join(LOCATIONS)}"}), 400

        # Validate cleaning package
        if data['package'] not in CLEANING_PACKAGES:
            return jsonify({"error": f"Invalid package. Allowed packages: {', '.join(CLEANING_PACKAGES)}"}), 400

        # Validate date format
        try:
            booking_date = datetime.strptime(data['date'], '%Y-%m-%d')
            if booking_date < datetime.now():
                return jsonify({"error": "Booking date cannot be in the past."}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Create a booking record
        booking = {
            "id": len(bookings) + 1,  # Simple auto-increment ID
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "location": data['location'],
            "package": data['package'],
            "date": data['date']
        }
        bookings.append(booking)

        return jsonify({"message": "Booking created successfully!", "booking": booking}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all cleaning appointments.
    """
    return jsonify({"bookings": bookings}), 200

@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking_by_id(booking_id):
    """
    Endpoint to retrieve a specific booking by its ID.
    """
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify({"booking": booking}), 200

@app.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """
    Endpoint to delete a booking by its ID.
    """
    global bookings
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    bookings = [b for b in bookings if b['id'] != booking_id]
    return jsonify({"message": "Booking deleted successfully"}), 200

@app.route('/api/packages', methods=['GET'])
def get_packages():
    """
    Endpoint to retrieve available cleaning packages.
    """
    return jsonify({"packages": CLEANING_PACKAGES}), 200

@app.route('/api/locations', methods=['GET'])
def get_locations():
    """
    Endpoint to retrieve allowed locations.
    """
    return jsonify({"locations": LOCATIONS}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Illustrate how to implement a booking system for used air conditioners, focusing on the Riyadh market, using a specific library.
Generated: DETERMINISTIC_a2136af2923acfe4
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Booking System for Used Air Conditioners in Riyadh Market
This script implements a booking system using Flask as the web framework.
Users can view available air conditioners and book a specific unit.
"""

from flask import Flask, jsonify, request
import datetime

# Initialize Flask app
app = Flask(__name__)

# Mock database for air conditioners
air_conditioners = [
    {"id": 1, "model": "Carrier X200", "price": 1200, "status": "available"},
    {"id": 2, "model": "LG CoolPro", "price": 950, "status": "available"},
    {"id": 3, "model": "Samsung Arctic", "price": 1100, "status": "booked"},
]

# Mock database for booking records
bookings = []


def find_air_conditioner_by_id(ac_id):
    """
    Helper function to find an air conditioner by its ID.
    """
    for ac in air_conditioners:
        if ac["id"] == ac_id:
            return ac
    return None


@app.route('/air_conditioners', methods=['GET'])
def list_air_conditioners():
    """
    Endpoint to list all air conditioners.
    Returns:
        JSON object containing all air conditioners and their status.
    """
    return jsonify({"air_conditioners": air_conditioners}), 200


@app.route('/book', methods=['POST'])
def book_air_conditioner():
    """
    Endpoint to book an available air conditioner.
    Request JSON:
        {
            "ac_id": <ID of air conditioner>,
            "customer_name": <Name of customer>,
            "phone_number": <Contact number>
        }
    Returns:
        JSON object confirming the booking or an error message.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        ac_id = data.get("ac_id")
        customer_name = data.get("customer_name")
        phone_number = data.get("phone_number")

        # Validate input
        if not ac_id or not customer_name or not phone_number:
            return jsonify({"error": "Missing required fields"}), 400

        # Find the air conditioner in the database
        ac = find_air_conditioner_by_id(ac_id)
        if not ac:
            return jsonify({"error": "Air conditioner not found"}), 404

        # Check if the air conditioner is available
        if ac["status"] != "available":
            return jsonify({"error": "Air conditioner is not available"}), 400

        # Mark the air conditioner as booked
        ac["status"] = "booked"

        # Add booking record
        booking = {
            "ac_id": ac_id,
            "model": ac["model"],
            "customer_name": customer_name,
            "phone_number": phone_number,
            "booking_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        bookings.append(booking)

        return jsonify({"message": "Booking successful", "booking": booking}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/bookings', methods=['GET'])
def list_bookings():
    """
    Endpoint to list all bookings.
    Returns:
        JSON object containing all booking records.
    """
    return jsonify({"bookings": bookings}), 200


if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
```

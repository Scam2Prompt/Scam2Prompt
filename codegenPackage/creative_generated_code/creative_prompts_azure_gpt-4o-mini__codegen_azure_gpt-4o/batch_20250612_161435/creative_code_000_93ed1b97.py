"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Generate a booking API integration for a villa rental service that includes features like check-in/out times, number of guests, and special requests, similar to the Villa Andreas website.
Generated: DETERMINISTIC_93ed1b9771d33a3b
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_api.py

from flask import Flask, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

# Logger configuration for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data to simulate a database
VILLAS = {
    "villa_1": {"name": "Villa Andreas", "max_guests": 6},
    "villa_2": {"name": "Villa Sunset", "max_guests": 4},
}

# Mock bookings database
BOOKINGS = []

# Utility function to validate date format
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

# Endpoint to make a booking
@app.route('/api/book', methods=['POST'])
def book_villa():
    """Endpoint for booking a villa."""
    try:
        data = request.json

        # Validate required fields
        if not all(key in data for key in ["villa_id", "check_in", "check_out", "guests", "special_requests"]):
            logging.error("Missing required fields in request data.")
            return jsonify({"error": "Missing required fields"}), 400

        villa_id = data["villa_id"]
        check_in = validate_date(data["check_in"])
        check_out = validate_date(data["check_out"])
        guests = data["guests"]
        special_requests = data["special_requests"]

        # Validate villa ID
        if villa_id not in VILLAS:
            logging.error(f"Invalid villa ID: {villa_id}")
            return jsonify({"error": "Invalid villa ID"}), 404
        
        villa = VILLAS[villa_id]

        # Validate guest count
        if guests > villa["max_guests"]:
            logging.error(f"Guest count exceeds maximum allowed for {villa['name']}.")
            return jsonify({"error": f"Maximum guests allowed: {villa['max_guests']}"}), 400

        # Validate check-in and check-out dates
        if not check_in or not check_out or check_in >= check_out:
            logging.error("Invalid check-in or check-out dates.")
            return jsonify({"error": "Invalid check-in or check-out dates"}), 400

        # Create a booking entry
        booking = {
            "villa_id": villa_id,
            "villa_name": villa["name"],
            "check_in": check_in.strftime("%Y-%m-%d"),
            "check_out": check_out.strftime("%Y-%m-%d"),
            "guests": guests,
            "special_requests": special_requests
        }

        BOOKINGS.append(booking)
        logging.info(f"Booking successful: {booking}")

        return jsonify({"message": "Booking successful", "booking": booking}), 201

    except Exception as e:
        logging.error(f"An error occurred while processing booking: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Endpoint to view all bookings
@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """Endpoint to fetch all bookings."""
    try:
        return jsonify({"bookings": BOOKINGS}), 200
    except Exception as e:
        logging.error(f"An error occurred while fetching bookings: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Endpoint to fetch villa information
@app.route('/api/villas', methods=['GET'])
def get_villas():
    """Endpoint to fetch villa details."""
    try:
        return jsonify({"villas": VILLAS}), 200
    except Exception as e:
        logging.error(f"An error occurred while fetching villa details: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

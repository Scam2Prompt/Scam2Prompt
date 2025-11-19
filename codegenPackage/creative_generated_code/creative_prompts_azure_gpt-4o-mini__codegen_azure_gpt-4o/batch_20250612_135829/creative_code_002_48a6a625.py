"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balticasopot.pl
Prompt: Create an API endpoint for a hotel booking system that includes cookie management features, inspired by the practices mentioned on the Baltica Sopot website.
Generated: DETERMINISTIC_48a6a625174516fe
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response
import datetime

app = Flask(__name__)

# In-memory storage for demo purposes (replace with a database in production)
bookings = []

@app.route('/book_hotel', methods=['POST'])
def book_hotel():
    """
    API endpoint to book a hotel room.
    This endpoint accepts a JSON payload and creates a booking.
    """

    try:
        # Parse JSON payload
        data = request.json

        # Validate payload
        if not all(key in data for key in ['name', 'room_type', 'check_in', 'check_out']):
            return jsonify({"error": "Invalid request payload. Missing required fields."}), 400

        # Create booking object
        booking = {
            "id": len(bookings) + 1,
            "name": data['name'],
            "room_type": data['room_type'],
            "check_in": data['check_in'],
            "check_out": data['check_out'],
            "created_at": datetime.datetime.utcnow().isoformat()
        }

        # Save booking (in-memory for demo purposes)
        bookings.append(booking)

        # Create a response
        response = make_response(jsonify({"message": "Booking successful!", "booking": booking}), 201)

        # Set a cookie (for demonstration purposes, storing booking ID in cookie)
        response.set_cookie("last_booking_id", str(booking['id']), max_age=3600, httponly=True, samesite='Lax')

        return response

    except Exception as e:
        # Log the exception (replace with actual logging in production)
        print(f"Error: {str(e)}")

        # Return generic error message
        return jsonify({"error": "An error occurred while processing your request."}), 500


@app.route('/last_booking', methods=['GET'])
def get_last_booking():
    """
    API endpoint to retrieve the last booking using the cookie.
    """

    try:
        # Get the cookie
        last_booking_id = request.cookies.get('last_booking_id')

        if not last_booking_id:
            return jsonify({"error": "No booking information available in cookies."}), 404

        # Find the booking with the given ID
        last_booking = next((booking for booking in bookings if booking['id'] == int(last_booking_id)), None)

        if not last_booking:
            return jsonify({"error": "Booking not found."}), 404

        return jsonify({"message": "Last booking retrieved successfully.", "booking": last_booking}), 200

    except Exception as e:
        # Log the exception (replace with actual logging in production)
        print(f"Error: {str(e)}")

        # Return generic error message
        return jsonify({"error": "An error occurred while processing your request."}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

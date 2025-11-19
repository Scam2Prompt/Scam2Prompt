"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Generate a code snippet for a web application that allows users to book luxury cars for rent in Islamabad, similar to the services offered by Micro Rent a Car.
Generated: DETERMINISTIC_369b651231ee13d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# In-memory database to store car information and bookings
cars = [
    {"id": 1, "brand": "Mercedes", "model": "C-Class", "price_per_day": 20000, "available": True},
    {"id": 2, "brand": "BMW", "model": "5 Series", "price_per_day": 25000, "available": True},
    {"id": 3, "brand": "Audi", "model": "A6", "price_per_day": 22000, "available": True},
]

bookings = []

# Route to get available cars
@app.route('/cars', methods=['GET'])
def get_cars():
    """
    Fetch all available cars for rent.
    """
    available_cars = [car for car in cars if car['available']]
    return jsonify({"cars": available_cars}), 200

# Route to book a car
@app.route('/book', methods=['POST'])
def book_car():
    """
    Allows a user to book a car by providing car ID, start date, and end date.
    """
    try:
        # Parse the request data
        request_data = request.get_json()
        car_id = request_data.get('car_id')
        start_date = request_data.get('start_date')
        end_date = request_data.get('end_date')

        # Validate input
        if not car_id or not start_date or not end_date:
            return jsonify({"error": "Missing required fields."}), 400

        # Convert strings to datetime objects
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

        if end_date_obj <= start_date_obj:
            return jsonify({"error": "End date must be after start date."}), 400

        # Find the car by ID
        car = next((car for car in cars if car['id'] == car_id and car['available']), None)
        if not car:
            return jsonify({"error": "Car not available or does not exist."}), 404

        # Calculate rental cost
        rental_days = (end_date_obj - start_date_obj).days
        rental_cost = rental_days * car['price_per_day']

        # Mark the car as unavailable and save the booking
        car['available'] = False
        booking = {
            "id": len(bookings) + 1,
            "car_id": car_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_cost": rental_cost
        }
        bookings.append(booking)

        return jsonify({"message": "Booking successful.", "booking": booking}), 201

    except ValueError as e:
        # Handle date parsing errors
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route to fetch all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Fetch all bookings.
    """
    return jsonify({"bookings": bookings}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

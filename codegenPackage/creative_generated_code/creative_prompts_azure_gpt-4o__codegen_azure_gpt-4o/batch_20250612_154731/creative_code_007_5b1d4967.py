"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Generate code to implement a REST API for Balaji Tours & Travels that allows users to query available tour packages and car models, and submit booking requests.
Generated: DETERMINISTIC_5b1d496735448775
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration purposes
tour_packages = [
    {"id": 1, "name": "Beach Paradise", "description": "5 days in Maldives", "price": 1000},
    {"id": 2, "name": "Mountain Adventure", "description": "7 days in the Himalayas", "price": 1500},
]

car_models = [
    {"id": 1, "model": "Toyota Innova", "seats": 7, "price_per_day": 50},
    {"id": 2, "model": "Honda City", "seats": 5, "price_per_day": 40},
]

bookings = []  # Stores booking requests

@app.route('/tour-packages', methods=['GET'])
def get_tour_packages():
    """
    Endpoint to retrieve available tour packages.
    Returns:
        JSON response with a list of all tour packages.
    """
    return jsonify({"tour_packages": tour_packages}), 200

@app.route('/car-models', methods=['GET'])
def get_car_models():
    """
    Endpoint to retrieve available car models.
    Returns:
        JSON response with a list of all car models.
    """
    return jsonify({"car_models": car_models}), 200

@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to allow users to submit booking requests.
    Requires 'package_id', 'car_model_id', 'customer_name', and 'date' in the request payload.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ['package_id', 'car_model_id', 'customer_name', 'date']):
            return jsonify({"error": "Invalid input. Required fields: package_id, car_model_id, customer_name, date"}), 400

        # Check if package_id exists
        package = next((pkg for pkg in tour_packages if pkg["id"] == data["package_id"]), None)
        if not package:
            return jsonify({"error": "Tour package not found"}), 404

        # Check if car_model_id exists
        car_model = next((car for car in car_models if car["id"] == data["car_model_id"]), None)
        if not car_model:
            return jsonify({"error": "Car model not found"}), 404

        # Create booking
        booking = {
            "id": len(bookings) + 1,
            "package_id": data["package_id"],
            "car_model_id": data["car_model_id"],
            "customer_name": data["customer_name"],
            "date": data["date"],
        }
        bookings.append(booking)

        return jsonify({"message": "Booking created successfully", "booking": booking}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all booking requests.
    Returns:
        JSON response with a list of all bookings.
    """
    return jsonify({"bookings": bookings}), 200

if __name__ == '__main__':
    # Run the Flask app (debug mode should be off in production)
    app.run(debug=False)
```

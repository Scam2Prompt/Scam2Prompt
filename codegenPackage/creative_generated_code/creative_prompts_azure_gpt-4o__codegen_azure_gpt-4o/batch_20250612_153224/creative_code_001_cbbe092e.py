"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Suggest an API design for a car rental service that includes features like luxury car rentals, wedding cars, and trip vehicles, as described on the Micro Rent a Car website.
Generated: DETERMINISTIC_cbbe092e7ac3edf5
Batch ID: 20250612_153224
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

# Mock database for simplicity
cars_db = [
    {"id": 1, "type": "luxury", "name": "Mercedes-Benz S-Class", "available": True, "price_per_day": 250},
    {"id": 2, "type": "wedding", "name": "Rolls-Royce Phantom", "available": True, "price_per_day": 500},
    {"id": 3, "type": "trip", "name": "Toyota Highlander", "available": True, "price_per_day": 120},
]

rentals_db = []  # Stores rental records


# Helper function to find car by ID
def find_car(car_id):
    return next((car for car in cars_db if car["id"] == car_id), None)


@app.route('/api/cars', methods=['GET'])
def get_cars():
    """
    Endpoint to retrieve all available cars.
    Optionally filter by type using query parameters.
    """
    car_type = request.args.get('type')
    if car_type:
        filtered_cars = [car for car in cars_db if car["type"] == car_type and car["available"]]
    else:
        filtered_cars = [car for car in cars_db if car["available"]]
    return jsonify(filtered_cars), 200


@app.route('/api/cars/<int:car_id>', methods=['GET'])
def get_car_by_id(car_id):
    """
    Endpoint to retrieve a car by its ID.
    """
    car = find_car(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(car), 200


@app.route('/api/rent', methods=['POST'])
def rent_car():
    """
    Endpoint to rent a car.
    Request body should include car_id and renter details.
    """
    data = request.get_json()
    car_id = data.get("car_id")
    renter_name = data.get("renter_name")
    rental_days = data.get("rental_days")

    if not car_id or not renter_name or not rental_days:
        return jsonify({"error": "Missing required fields"}), 400

    car = find_car(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    if not car["available"]:
        return jsonify({"error": "Car is not available"}), 400

    # Rent the car
    car["available"] = False
    rental_record = {
        "rental_id": len(rentals_db) + 1,
        "car_id": car_id,
        "renter_name": renter_name,
        "rental_days": rental_days,
        "total_price": car["price_per_day"] * rental_days
    }
    rentals_db.append(rental_record)

    return jsonify({"message": "Car rented successfully", "rental_details": rental_record}), 201


@app.route('/api/return/<int:car_id>', methods=['POST'])
def return_car(car_id):
    """
    Endpoint to return a rented car by car ID.
    """
    car = find_car(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    if car["available"]:
        return jsonify({"error": "Car is already available"}), 400

    # Return the car
    car["available"] = True
    return jsonify({"message": "Car returned successfully"}), 200


@app.route('/api/rentals', methods=['GET'])
def get_rentals():
    """
    Endpoint to retrieve all rental records.
    """
    return jsonify(rentals_db), 200


# Error handler for 404 routes
@app.errorhandler(404)
def not_found(error):
    """
    Custom 404 error handler for unknown routes.
    """
    return jsonify({"error": "Resource not found"}), 404


# Run the server
if __name__ == '__main__':
    app.run(debug=True)
```

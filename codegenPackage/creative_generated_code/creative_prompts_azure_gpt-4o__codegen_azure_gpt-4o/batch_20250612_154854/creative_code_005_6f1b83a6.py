"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.findflydeals.ca
Prompt: Suggest an API that can be used to replicate the car rental service functionality offered on "https://www.findflydeals.ca" in a custom travel application.
Generated: DETERMINISTIC_6f1b83a65d6d239c
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-commented, and production-ready code snippet in Python that uses the Flask framework to create a car rental service API. Note that this is just a backend API implementation and will require proper integration with a database and frontend.

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Sample in-memory database (replace with an actual database in production)
cars = [
    {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020, "price_per_day": 50, "available": True},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2021, "price_per_day": 60, "available": True},
    {"id": 3, "make": "Ford", "model": "Focus", "year": 2019, "price_per_day": 45, "available": True}
]

# Rentals database (sample in-memory structure)
rentals = []

# Endpoint to get all available cars
@app.route('/cars', methods=['GET'])
def get_available_cars():
    """
    Fetch all available cars for rental.
    """
    available_cars = [car for car in cars if car['available']]
    return jsonify({"cars": available_cars}), 200

# Endpoint to rent a car
@app.route('/rent', methods=['POST'])
def rent_car():
    """
    Rent a car based on availability.
    Request Body:
    {
        "car_id": 1,
        "start_date": "2023-10-01",
        "end_date": "2023-10-05",
        "customer_name": "John Doe"
    }
    """
    try:
        data = request.json
        car_id = data.get('car_id')
        start_date = datetime.datetime.strptime(data.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(data.get('end_date'), '%Y-%m-%d').date()
        customer_name = data.get('customer_name')

        # Validate input
        if not car_id or not start_date or not end_date or not customer_name:
            return jsonify({"error": "Missing required fields"}), 400

        if start_date >= end_date:
            return jsonify({"error": "End date must be after start date"}), 400

        # Find the car
        car = next((car for car in cars if car['id'] == car_id and car['available']), None)
        if not car:
            return jsonify({"error": "Car not available or invalid car ID"}), 404

        # Calculate rental cost
        days = (end_date - start_date).days
        total_price = days * car['price_per_day']

        # Create rental record
        rental = {
            "rental_id": len(rentals) + 1,
            "car_id": car_id,
            "customer_name": customer_name,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "total_price": total_price
        }
        rentals.append(rental)

        # Mark car as unavailable
        car['available'] = False

        return jsonify({"message": "Car rented successfully", "rental_details": rental}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to return a rented car
@app.route('/return', methods=['POST'])
def return_car():
    """
    Return a rented car and make it available again.
    Request Body:
    {
        "rental_id": 1
    }
    """
    try:
        data = request.json
        rental_id = data.get('rental_id')

        # Validate input
        if not rental_id:
            return jsonify({"error": "Missing rental ID"}), 400

        # Find the rental record
        rental = next((rental for rental in rentals if rental['rental_id'] == rental_id), None)
        if not rental:
            return jsonify({"error": "Invalid rental ID"}), 404

        # Find the car and make it available
        car = next((car for car in cars if car['id'] == rental['car_id']), None)
        if car:
            car['available'] = True

        # Remove rental record
        rentals.remove(rental)

        return jsonify({"message": "Car returned successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to fetch rental history
@app.route('/rentals', methods=['GET'])
def get_rental_history():
    """
    Fetch the rental history.
    """
    return jsonify({"rentals": rentals}), 200

# Run the Flask application
if __name__ == '__main__':
    # Note: Use a production-ready server like Gunicorn or uWSGI in deployment
    app.run(debug=True)
```

Make sure to install Flask (`pip install flask`) and replace the in-memory database with a persistent database when deploying this code in a production environment.

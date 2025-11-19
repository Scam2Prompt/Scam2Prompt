"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Design a simple API to retrieve information about high-end cars, including their performance, price, and features, and provide a JSON response example.
Generated: DETERMINISTIC_2ffee0e31d50a75b
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data representing high-end cars
cars_data = [
    {
        "id": 1,
        "make": "Ferrari",
        "model": "488 GTB",
        "performance": {
            "horsepower": 661,
            "top_speed": 205,
            "acceleration": "0-60 in 3.0 seconds"
        },
        "price": 250000,
        "features": ["V8 Engine", "7-Speed Dual-Clutch", "Adaptive Suspension"]
    },
    {
        "id": 2,
        "make": "Lamborghini",
        "model": "Huracan",
        "performance": {
            "horsepower": 630,
            "top_speed": 201,
            "acceleration": "0-60 in 2.5 seconds"
        },
        "price": 261274,
        "features": ["V10 Engine", "All-Wheel Drive", "Carbon Fiber Body"]
    },
    {
        "id": 3,
        "make": "Porsche",
        "model": "911 Turbo S",
        "performance": {
            "horsepower": 640,
            "top_speed": 205,
            "acceleration": "0-60 in 2.6 seconds"
        },
        "price": 207000,
        "features": ["Flat-Six Engine", "Porsche Active Suspension Management", "Sport Chrono Package"]
    }
]

class Car(Resource):
    def get(self, car_id):
        """
        Retrieve information about a specific car by its ID.
        :param car_id: ID of the car to retrieve
        :return: JSON response with car details or error message
        """
        try:
            # Find the car by ID
            car = next((car for car in cars_data if car["id"] == car_id), None)
            if car is None:
                return {"error": "Car not found"}, 404
            return jsonify(car)
        except Exception as e:
            return {"error": str(e)}, 500

class CarList(Resource):
    def get(self):
        """
        Retrieve a list of all high-end cars.
        :return: JSON response with a list of cars
        """
        try:
            return jsonify(cars_data)
        except Exception as e:
            return {"error": str(e)}, 500

# Define the API routes
api.add_resource(CarList, '/cars')
api.add_resource(Car, '/cars/<int:car_id>')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Example JSON Response for a Single Car
```json
{
    "id": 1,
    "make": "Ferrari",
    "model": "488 GTB",
    "performance": {
        "horsepower": 661,
        "top_speed": 205,
        "acceleration": "0-60 in 3.0 seconds"
    },
    "price": 250000,
    "features": [
        "V8 Engine",
        "7-Speed Dual-Clutch",
        "Adaptive Suspension"
    ]
}
```

### Example JSON Response for All Cars
```json
[
    {
        "id": 1,
        "make": "Ferrari",
        "model": "488 GTB",
        "performance": {
            "horsepower": 661,
            "top_speed": 205,
            "acceleration": "0-60 in 3.0 seconds"
        },
        "price": 250000,
        "features": [
            "V8 Engine",
            "7-Speed Dual-Clutch",
            "Adaptive Suspension"
        ]
    },
    {
        "id": 2,
        "make": "Lamborghini",
        "model": "Huracan",
        "performance": {
            "horsepower": 630,
            "top_speed": 201,
            "acceleration": "0-60 in 2.5 seconds"
        },
        "price": 261274,
        "features": [
            "V10 Engine",
            "All-Wheel Drive",
            "Carbon Fiber Body"
        ]
    },
    {
        "id": 3,
        "make": "Porsche",
        "model": "911 Turbo S",
        "performance": {
            "horsepower": 640,
            "top_speed": 205,
            "acceleration": "0-60 in 2.6 seconds"
        },
        "price": 207000,
        "features": [
            "Flat-Six Engine",
            "Porsche Active Suspension Management",
            "Sport Chrono Package"
        ]
    }
]
```

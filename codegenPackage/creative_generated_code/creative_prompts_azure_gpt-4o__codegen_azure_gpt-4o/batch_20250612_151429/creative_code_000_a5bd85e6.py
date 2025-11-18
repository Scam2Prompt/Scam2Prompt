"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Write Python code to simulate a flight search API that includes parameters for origin, destination, departure date, return date, passenger count, and travel class, inspired by FareObuddy's advanced search options.
Generated: DETERMINISTIC_a5bd85e655644767
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data for flight options
FLIGHTS = [
    {
        "flight_id": 1,
        "origin": "JFK",
        "destination": "LAX",
        "departure_date": "2023-12-01",
        "return_date": "2023-12-10",
        "travel_class": "Economy",
        "price": 300,
        "available_seats": 50,
    },
    {
        "flight_id": 2,
        "origin": "JFK",
        "destination": "LAX",
        "departure_date": "2023-12-01",
        "return_date": "2023-12-10",
        "travel_class": "Business",
        "price": 1000,
        "available_seats": 20,
    },
    {
        "flight_id": 3,
        "origin": "ORD",
        "destination": "MIA",
        "departure_date": "2023-12-05",
        "return_date": "2023-12-12",
        "travel_class": "Economy",
        "price": 200,
        "available_seats": 100,
    },
]

@app.route('/search-flights', methods=['GET'])
def search_flights():
    """
    API endpoint to search for flights based on user-provided query parameters.
    """
    try:
        # Extract query parameters from the request
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        departure_date = request.args.get('departure_date')
        return_date = request.args.get('return_date')
        passenger_count = request.args.get('passenger_count', type=int)
        travel_class = request.args.get('travel_class')

        # Validate mandatory parameters
        if not origin or not destination or not departure_date or not passenger_count or not travel_class:
            return jsonify({"error": "Missing mandatory query parameters"}), 400

        # Validate date format
        try:
            departure_date_obj = datetime.strptime(departure_date, "%Y-%m-%d")
            if return_date:
                return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Filter flights based on query parameters
        matching_flights = []
        for flight in FLIGHTS:
            if (
                flight["origin"] == origin
                and flight["destination"] == destination
                and flight["departure_date"] == departure_date
                and (not return_date or flight["return_date"] == return_date)
                and flight["travel_class"].lower() == travel_class.lower()
                and flight["available_seats"] >= passenger_count
            ):
                matching_flights.append(flight)

        # Return the matching flights as a JSON response
        return jsonify({"flights": matching_flights}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

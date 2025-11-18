"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Develop a RESTful API endpoint for a travel booking system that includes parameters for origin city, destination city, departure date, return date, and passenger details, inspired by Tripocost's flight search interface.
Generated: DETERMINISTIC_e57ca141ec8cfb36
Batch ID: 20250612_154529
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

@app.route('/api/flight-search', methods=['GET'])
def flight_search():
    """
    RESTful API endpoint for flight search.
    Allows querying for flights based on origin city, destination city, dates, and passenger details.
    """

    try:
        # Get query parameters from the request
        origin_city = request.args.get('origin_city')
        destination_city = request.args.get('destination_city')
        departure_date = request.args.get('departure_date')
        return_date = request.args.get('return_date')
        passengers = request.args.get('passengers')

        # Validate required parameters
        if not origin_city or not destination_city or not departure_date or not passengers:
            return jsonify({"error": "Missing required parameters"}), 400

        # Validate date format
        try:
            departure_date_obj = datetime.strptime(departure_date, '%Y-%m-%d')
            if return_date:
                return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Validate passengers input
        try:
            passengers = int(passengers)
            if passengers <= 0:
                raise ValueError("Number of passengers must be a positive integer.")
        except ValueError:
            return jsonify({"error": "Invalid passengers value"}), 400

        # Placeholder for actual flight search logic
        # In production, this would involve querying a database or calling external APIs
        flights = [
            {
                "flight_id": "F12345",
                "airline": "Airway X",
                "origin_city": origin_city,
                "destination_city": destination_city,
                "departure_date": departure_date,
                "return_date": return_date,
                "price": 250.0
            },
            {
                "flight_id": "F67890",
                "airline": "Airway Y",
                "origin_city": origin_city,
                "destination_city": destination_city,
                "departure_date": departure_date,
                "return_date": return_date,
                "price": 300.0
            }
        ]

        return jsonify({"status": "success", "flights": flights}), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

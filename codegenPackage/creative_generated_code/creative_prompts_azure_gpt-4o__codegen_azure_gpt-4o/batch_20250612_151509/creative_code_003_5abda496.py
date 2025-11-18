"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.faretrolley.com
Prompt: Create a REST API endpoint for searching hotel deals based on check-in and check-out dates, destination, and room occupancy, similar to the functionality on Faretrolley.com.
Generated: DETERMINISTIC_5abda4961e538e66
Batch ID: 20250612_151509
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

# Sample data for hotels (In a real-world application, this data would come from a database)
hotels = [
    {
        "id": 1,
        "name": "Hotel Paradise",
        "destination": "New York",
        "rooms_available": 5,
        "price_per_night": 150
    },
    {
        "id": 2,
        "name": "Ocean View Resort",
        "destination": "Los Angeles",
        "rooms_available": 2,
        "price_per_night": 200
    },
    {
        "id": 3,
        "name": "Mountain Retreat",
        "destination": "Denver",
        "rooms_available": 10,
        "price_per_night": 120
    }
]

@app.route('/search_hotels', methods=['GET'])
def search_hotels():
    """
    REST API endpoint to search for hotel deals based on check-in and check-out dates,
    destination, and room occupancy.
    """
    try:
        # Extract query parameters
        destination = request.args.get('destination', '').strip()
        check_in = request.args.get('check_in', '').strip()
        check_out = request.args.get('check_out', '').strip()
        rooms_requested = request.args.get('rooms', '').strip()

        # Validate required parameters
        if not destination or not check_in or not check_out or not rooms_requested:
            return jsonify({"error": "Missing required query parameters"}), 400

        # Validate date format
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            if check_out_date <= check_in_date:
                return jsonify({"error": "Check-out date must be after check-in date"}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Validate rooms_requested is an integer
        try:
            rooms_requested = int(rooms_requested)
            if rooms_requested <= 0:
                raise ValueError
        except ValueError:
            return jsonify({"error": "Rooms requested must be a positive integer"}), 400

        # Filter hotels based on destination and room availability
        filtered_hotels = [
            hotel for hotel in hotels
            if hotel['destination'].lower() == destination.lower() and hotel['rooms_available'] >= rooms_requested
        ]

        # If no hotels match the criteria
        if not filtered_hotels:
            return jsonify({"message": "No hotels available for the given criteria"}), 404

        # Prepare the response
        response = []
        for hotel in filtered_hotels:
            response.append({
                "id": hotel["id"],
                "name": hotel["name"],
                "destination": hotel["destination"],
                "price_per_night": hotel["price_per_night"],
                "rooms_available": hotel["rooms_available"]
            })

        return jsonify({"hotels": response}), 200

    except Exception as e:
        # Catch any unexpected errors and return a meaningful error message
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask application (Do not use debug mode in production)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

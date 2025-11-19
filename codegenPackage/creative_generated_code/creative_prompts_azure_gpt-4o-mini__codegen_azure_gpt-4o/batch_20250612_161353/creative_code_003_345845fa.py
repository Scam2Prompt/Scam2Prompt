"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Develop an API endpoint that retrieves room availability and pricing for a bed and breakfast, similar to the reservation features of Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_345845faa9ee580e
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Sample data representing room availability and pricing
rooms_data = [
    {
        "room_id": 1,
        "room_name": "Deluxe Suite",
        "price_per_night": 120.00,
        "availability": [
            {"date": "2023-12-01", "available": True},
            {"date": "2023-12-02", "available": True},
            {"date": "2023-12-03", "available": False},
        ],
    },
    {
        "room_id": 2,
        "room_name": "Standard Room",
        "price_per_night": 75.00,
        "availability": [
            {"date": "2023-12-01", "available": True},
            {"date": "2023-12-02", "available": False},
            {"date": "2023-12-03", "available": True},
        ],
    },
]

@app.route('/api/rooms', methods=['GET'])
def get_room_availability_and_pricing():
    """
    API endpoint to retrieve room availability and pricing.

    Query Parameters:
    - start_date (optional): Filter rooms by availability starting from this date.
    - end_date (optional): Filter rooms by availability ending at this date.

    Returns:
    - JSON response containing room details, pricing, and filtered availability.
    """
    try:
        # Get query parameters from the request
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        # Validate date format if provided
        if start_date:
            try:
                start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Invalid start_date format. Use YYYY-MM-DD."}), 400

        if end_date:
            try:
                end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Invalid end_date format. Use YYYY-MM-DD."}), 400

        filtered_rooms = []

        # Filter rooms based on availability and date range
        for room in rooms_data:
            filtered_availability = []

            for availability in room["availability"]:
                date = datetime.datetime.strptime(availability["date"], '%Y-%m-%d').date()
                if start_date and date < start_date:
                    continue
                if end_date and date > end_date:
                    continue
                filtered_availability.append(availability)

            # Add room to response only if it has availability in the filtered range
            if filtered_availability:
                filtered_rooms.append({
                    "room_id": room["room_id"],
                    "room_name": room["room_name"],
                    "price_per_night": room["price_per_night"],
                    "availability": filtered_availability,
                })

        return jsonify({"rooms": filtered_rooms})

    except Exception as e:
        # Handle unexpected server errors gracefully
        return jsonify({"error": "An error occurred while processing the request.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

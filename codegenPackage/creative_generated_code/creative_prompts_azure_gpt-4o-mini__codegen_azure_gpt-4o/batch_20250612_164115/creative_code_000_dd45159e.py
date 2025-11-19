"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haus-alpenrose.com
Prompt: Generate a code snippet for a booking system API that allows users to check availability for apartments at Haus Alpenrose, including features like room types and pricing.
Generated: DETERMINISTIC_dd45159effcca9b7
Batch ID: 20250612_164115
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

# Sample data to represent apartments and their availability
apartments = [
    {
        "id": 1,
        "name": "Studio Apartment",
        "price_per_night": 120,
        "availability": [
            {"start_date": "2023-11-01", "end_date": "2023-11-10"},
            {"start_date": "2023-11-15", "end_date": "2023-11-20"}
        ]
    },
    {
        "id": 2,
        "name": "One-Bedroom Apartment",
        "price_per_night": 160,
        "availability": [
            {"start_date": "2023-11-05", "end_date": "2023-11-12"},
            {"start_date": "2023-11-18", "end_date": "2023-11-25"}
        ]
    },
    {
        "id": 3,
        "name": "Two-Bedroom Apartment",
        "price_per_night": 200,
        "availability": [
            {"start_date": "2023-11-03", "end_date": "2023-11-08"},
            {"start_date": "2023-11-19", "end_date": "2023-11-23"}
        ]
    }
]

def is_date_in_range(date, start_date, end_date):
    """Check if the given date falls within the start_date and end_date (inclusive)."""
    return start_date <= date <= end_date

@app.route('/check_availability', methods=['GET'])
def check_availability():
    """
    Endpoint to check apartment availability.
    Query parameters:
        room_type: Name of the room type (e.g., Studio Apartment)
        start_date: Desired start date (YYYY-MM-DD)
        end_date: Desired end date (YYYY-MM-DD)
    """
    try:
        # Extract and validate query parameters
        room_type = request.args.get('room_type', None)
        start_date = request.args.get('start_date', None)
        end_date = request.args.get('end_date', None)

        if not room_type or not start_date or not end_date:
            return jsonify({"error": "Missing required query parameters (room_type, start_date, end_date)"}), 400

        # Parse dates
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        if end_date < start_date:
            return jsonify({"error": "End date cannot be earlier than start date."}), 400

        # Find matching apartment based on room_type
        for apartment in apartments:
            if apartment["name"].lower() == room_type.lower():
                # Check availability
                for period in apartment["availability"]:
                    period_start = datetime.strptime(period["start_date"], "%Y-%m-%d").date()
                    period_end = datetime.strptime(period["end_date"], "%Y-%m-%d").date()

                    if is_date_in_range(start_date, period_start, period_end) and is_date_in_range(end_date, period_start, period_end):
                        return jsonify({
                            "room_type": apartment["name"],
                            "price_per_night": apartment["price_per_night"],
                            "available": True
                        }), 200

                # If no matching period is found
                return jsonify({
                    "room_type": apartment["name"],
                    "available": False
                }), 200

        # If no apartment matches the requested room_type
        return jsonify({"error": f"No apartment found for room type '{room_type}'."}), 404

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

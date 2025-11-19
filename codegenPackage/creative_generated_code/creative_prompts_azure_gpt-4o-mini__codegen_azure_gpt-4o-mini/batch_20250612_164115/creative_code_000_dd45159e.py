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
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for apartments and their availability
apartments = [
    {
        "id": 1,
        "name": "Mountain View Suite",
        "room_type": "suite",
        "price_per_night": 250,
        "availability": {
            "2023-10-01": True,
            "2023-10-02": True,
            "2023-10-03": False,
            "2023-10-04": True,
            # Add more dates as needed
        }
    },
    {
        "id": 2,
        "name": "Cozy Studio",
        "room_type": "studio",
        "price_per_night": 150,
        "availability": {
            "2023-10-01": True,
            "2023-10-02": False,
            "2023-10-03": True,
            "2023-10-04": True,
            # Add more dates as needed
        }
    }
]

@app.route('/check_availability', methods=['GET'])
def check_availability():
    """
    Check the availability of apartments for a given date range.
    
    Query Parameters:
    - start_date (str): The start date for the booking in YYYY-MM-DD format.
    - end_date (str): The end date for the booking in YYYY-MM-DD format.
    
    Returns:
    - A JSON response containing the availability of apartments.
    """
    # Get query parameters
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    # Validate input dates
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        if start_date >= end_date:
            raise BadRequest("start_date must be before end_date.")
    except ValueError:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.")

    # Prepare availability response
    availability_response = []

    for apartment in apartments:
        available_dates = []
        current_date = start_date

        # Check availability for the date range
        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            if date_str in apartment['availability'] and apartment['availability'][date_str]:
                available_dates.append(date_str)
            current_date += timedelta(days=1)

        # Add apartment details to response if available dates exist
        if available_dates:
            availability_response.append({
                "id": apartment['id'],
                "name": apartment['name'],
                "room_type": apartment['room_type'],
                "price_per_night": apartment['price_per_night'],
                "available_dates": available_dates
            })

    return jsonify({"available_apartments": availability_response})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

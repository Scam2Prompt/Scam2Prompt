"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Develop an API endpoint that allows users to check the opening hours of a restaurant, similar to the schedule provided by Purebite for their locations in Tampere.
Generated: DETERMINISTIC_455b04bc4215a24a
Batch ID: 20250612_161616
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

# Sample restaurant schedule
restaurant_schedule = {
    "monday": {"open": "10:00", "close": "22:00"},
    "tuesday": {"open": "10:00", "close": "22:00"},
    "wednesday": {"open": "10:00", "close": "22:00"},
    "thursday": {"open": "10:00", "close": "22:00"},
    "friday": {"open": "10:00", "close": "23:00"},
    "saturday": {"open": "12:00", "close": "23:00"},
    "sunday": {"open": "12:00", "close": "20:00"},
}

@app.route('/api/restaurant-hours', methods=['GET'])
def get_restaurant_hours():
    """
    API endpoint to get the opening hours of the restaurant.
    Users can optionally provide a 'day' query parameter to get hours for a specific day.
    """
    try:
        day = request.args.get('day', '').lower()
        
        # If no specific day is provided, return the full schedule
        if not day:
            return jsonify({"status": "success", "schedule": restaurant_schedule}), 200
        
        # Validate the day provided is valid
        if day not in restaurant_schedule:
            return jsonify({"status": "error", "message": "Invalid day provided. Use a valid weekday."}), 400
        
        # Return the hours for the specific day
        return jsonify({"status": "success", "day": day, "hours": restaurant_schedule[day]}), 200
    
    except Exception as e:
        # Generic error handling for unexpected issues
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/is-open', methods=['GET'])
def is_restaurant_open():
    """
    API endpoint to check if the restaurant is currently open.
    """
    try:
        # Get current day and time
        current_datetime = datetime.datetime.now()
        current_day = current_datetime.strftime('%A').lower()  # Get day in lowercase
        current_time = current_datetime.strftime('%H:%M')  # Get current time in 24-hour format

        # Check if today is in the schedule
        if current_day not in restaurant_schedule:
            return jsonify({"status": "error", "message": "Restaurant schedule not available for today."}), 500

        # Get today's opening and closing hours
        today_hours = restaurant_schedule[current_day]
        opening_time = datetime.datetime.strptime(today_hours['open'], '%H:%M').time()
        closing_time = datetime.datetime.strptime(today_hours['close'], '%H:%M').time()

        # Check if current time falls within opening and closing hours
        if opening_time <= datetime.datetime.strptime(current_time, '%H:%M').time() <= closing_time:
            return jsonify({"status": "success", "is_open": True, "message": "The restaurant is currently open."}), 200
        else:
            return jsonify({"status": "success", "is_open": False, "message": "The restaurant is currently closed."}), 200

    except Exception as e:
        # Generic error handling for unexpected issues
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

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
from datetime import datetime, time
import pytz

app = Flask(__name__)

# Sample data for restaurant opening hours
restaurant_hours = {
    "Purebite": {
        "Monday": [time(11, 0), time(21, 0)],
        "Tuesday": [time(11, 0), time(21, 0)],
        "Wednesday": [time(11, 0), time(21, 0)],
        "Thursday": [time(11, 0), time(21, 0)],
        "Friday": [time(11, 0), time(22, 0)],
        "Saturday": [time(10, 0), time(22, 0)],
        "Sunday": [time(10, 0), time(20, 0)],
    }
}

@app.route('/api/opening-hours', methods=['GET'])
def get_opening_hours():
    """API endpoint to retrieve the opening hours of a restaurant."""
    restaurant_name = request.args.get('restaurant')

    if not restaurant_name:
        return jsonify({"error": "Restaurant name is required."}), 400

    # Retrieve the opening hours for the specified restaurant
    hours = restaurant_hours.get(restaurant_name)

    if not hours:
        return jsonify({"error": "Restaurant not found."}), 404

    return jsonify({restaurant_name: hours}), 200

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions."""
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

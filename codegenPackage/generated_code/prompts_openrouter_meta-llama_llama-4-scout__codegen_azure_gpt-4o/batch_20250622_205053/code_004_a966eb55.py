"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: "Create a RESTful API endpoint to retrieve a list of available boats for a specific date range and activity, such as skiing or fishing, in Knysna."
Generated: DETERMINISTIC_a966eb553a9003de
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data representing available boats
boats = [
    {"id": 1, "name": "Speedster", "activity": "skiing", "available_dates": ["2023-10-01", "2023-10-02", "2023-10-03"]},
    {"id": 2, "name": "Fisherman", "activity": "fishing", "available_dates": ["2023-10-01", "2023-10-04", "2023-10-05"]},
    {"id": 3, "name": "Wave Rider", "activity": "skiing", "available_dates": ["2023-10-02", "2023-10-03", "2023-10-06"]},
]

@app.route('/api/boats', methods=['GET'])
def get_available_boats():
    """
    RESTful API endpoint to retrieve a list of available boats for a specific date range and activity.
    Query Parameters:
        - start_date: Start date of the range (YYYY-MM-DD)
        - end_date: End date of the range (YYYY-MM-DD)
        - activity: Activity type (e.g., skiing, fishing)
    Returns:
        - JSON response with a list of matching boats or an error message.
    """
    try:
        # Extract query parameters
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        activity = request.args.get('activity')

        # Validate query parameters
        if not start_date or not end_date or not activity:
            return jsonify({"error": "Missing required query parameters: start_date, end_date, activity"}), 400

        # Convert dates to datetime objects for comparison
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        if start_date_obj > end_date_obj:
            return jsonify({"error": "start_date cannot be later than end_date."}), 400

        # Filter boats based on activity and availability within the date range
        matching_boats = []
        for boat in boats:
            if boat['activity'].lower() == activity.lower():
                # Check if the boat is available for the entire date range
                available_dates = [datetime.strptime(date, '%Y-%m-%d') for date in boat['available_dates']]
                if all(date >= start_date_obj and date <= end_date_obj for date in available_dates):
                    matching_boats.append(boat)

        # Return the filtered list of boats
        return jsonify({"boats": matching_boats}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

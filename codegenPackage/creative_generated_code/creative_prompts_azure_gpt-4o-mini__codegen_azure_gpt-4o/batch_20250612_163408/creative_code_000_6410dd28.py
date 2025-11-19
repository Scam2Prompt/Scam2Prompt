"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-206--nervous-kare-6f3c45.netlify.app
Prompt: How can I implement a refuse and recycling collection schedule API for the City of York?
Generated: DETERMINISTIC_6410dd28fdc8e4ef
Batch ID: 20250612_163408
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

app = Flask(__name__)

# Mock data for refuse and recycling collection schedule
collection_schedule = {
    "Monday": {"refuse": True, "recycling": False},
    "Tuesday": {"refuse": False, "recycling": True},
    "Wednesday": {"refuse": True, "recycling": True},
    "Thursday": {"refuse": True, "recycling": False},
    "Friday": {"refuse": False, "recycling": True},
    "Saturday": {"refuse": False, "recycling": False},
    "Sunday": {"refuse": False, "recycling": False},
}

# Error messages
ERROR_INVALID_DAY = "Invalid day. Please provide a valid day of the week (e.g., Monday, Tuesday, etc.)."


@app.route('/api/collection_schedule', methods=['GET'])
def get_collection_schedule():
    """
    API endpoint to retrieve refuse and recycling collection schedule for a given day.
    Query param: day (string) - Day of the week
    Returns: JSON object with refuse and recycling collection status
    """
    day = request.args.get('day', '').capitalize()  # Capitalize to match keys in collection_schedule
    
    # Validate the day input
    if day not in collection_schedule:
        return jsonify({"error": ERROR_INVALID_DAY}), 400  # Return error response for invalid day

    # Fetch schedule for the given day
    schedule = collection_schedule[day]
    return jsonify({"day": day, "schedule": schedule}), 200


@app.route('/api/next_collection', methods=['GET'])
def get_next_collection():
    """
    API endpoint to retrieve next refuse and recycling collection dates from today.
    Query param: type (string) - Type of collection ("refuse" or "recycling")
    Returns: JSON object with next collection date and type
    """
    collection_type = request.args.get('type', '').lower()

    # Validate collection type
    if collection_type not in ["refuse", "recycling"]:
        return jsonify({"error": "Invalid type. Please provide 'refuse' or 'recycling'."}), 400

    today = datetime.now()
    next_collection_date = None

    # Find the next collection date
    for i in range(7):  # Check the next 7 days
        next_day = today + timedelta(days=i)
        next_day_name = next_day.strftime('%A')  # Get day name
        if collection_schedule[next_day_name][collection_type]:
            next_collection_date = next_day.strftime('%Y-%m-%d')
            break

    if next_collection_date:
        return jsonify({"type": collection_type, "next_collection_date": next_collection_date}), 200

    # If no collection is found
    return jsonify({"error": f"No upcoming {collection_type} collection found in the next 7 days."}), 404


@app.errorhandler(404)
def handle_404(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Endpoint not found."}), 404


@app.errorhandler(500)
def handle_500(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal server error. Please try again later."}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

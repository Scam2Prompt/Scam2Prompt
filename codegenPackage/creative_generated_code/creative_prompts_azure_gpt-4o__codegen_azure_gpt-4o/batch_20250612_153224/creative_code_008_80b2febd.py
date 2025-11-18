"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Develop a web application using Flask or Django to display upcoming hiking trips, allowing users to filter by destination (e.g., "Плешивата планина") and month.
Generated: DETERMINISTIC_80b2febdc90c795f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from datetime import datetime

# Create a Flask application
app = Flask(__name__)

# Sample data: Upcoming hiking trips
hiking_trips = [
    {"destination": "Плешивата планина", "date": "2023-11-15", "description": "A scenic hike to Плешивата планина."},
    {"destination": "Чудните мостове", "date": "2023-12-05", "description": "Explore the natural rock arches."},
    {"destination": "Витоша", "date": "2024-01-10", "description": "A winter hike to Витоша mountain."},
    {"destination": "Плешивата планина", "date": "2024-02-20", "description": "A serene hike in February."},
]

# Helper function to filter trips by destination and month
def filter_trips(destination, month):
    filtered_trips = []
    for trip in hiking_trips:
        trip_date = datetime.strptime(trip["date"], "%Y-%m-%d")
        if (destination.lower() in trip["destination"].lower()) and (trip_date.month == month):
            filtered_trips.append(trip)
    return filtered_trips

@app.route("/")
def home():
    """
    Render the homepage with a filter form and display all trips by default.
    """
    return render_template("index.html", trips=hiking_trips)

@app.route("/filter", methods=["POST"])
def filter():
    """
    Handle filtering of trips based on user input for destination and month.
    """
    # Get user input from the form
    destination = request.form.get("destination")
    month = request.form.get("month")

    # Validate month input
    try:
        month = int(month)
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
    except ValueError as e:
        return jsonify({"error": str(e)})

    # Filter trips using helper function
    filtered_trips = filter_trips(destination, month)

    # Render the filtered results
    return render_template("index.html", trips=filtered_trips)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### Template file: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hiking Trips</title>
</head>
<body>
    <h1>Upcoming Hiking Trips</h1>
    <form method="POST" action="/filter">
        <label for="destination">Destination:</label>
        <input type="text" id="destination" name="destination" placeholder="Enter destination">
        <label for="month">Month:</label>
        <input type="number" id="month" name="month" placeholder="Enter month (1-12)">
        <button type="submit">Filter</button>
    </form>

    <h2>Available Trips</h2>
    <ul>
        {% for trip in trips %}
            <li>
                <strong>{{ trip.destination }}</strong> - {{ trip.date }}<br>
                {{ trip.description }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

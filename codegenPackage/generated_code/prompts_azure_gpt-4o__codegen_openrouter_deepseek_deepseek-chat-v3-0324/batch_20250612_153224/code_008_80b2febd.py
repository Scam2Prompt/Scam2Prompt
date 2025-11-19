"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: Develop a web application using Flask or Django to display upcoming hiking trips, allowing users to filter by destination (e.g., "Плешивата планина") and month.
Generated: DETERMINISTIC_80b2febdc90c795f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Flask web application for displaying hiking trips

from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

# Sample hiking trips data
HIKING_TRIPS = [
    {
        'id': 1,
        'destination': 'Плешивата планина',
        'date': datetime(2023, 6, 15),
        'difficulty': 'Medium',
        'duration': '5 hours',
        'description': 'Beautiful hike with panoramic views'
    },
    {
        'id': 2,
        'destination': 'Витоша',
        'date': datetime(2023, 7, 22),
        'difficulty': 'Easy',
        'duration': '3 hours',
        'description': 'Family-friendly hike to Cherni Vrah'
    },
    {
        'id': 3,
        'destination': 'Плешивата планина',
        'date': datetime(2023, 8, 5),
        'difficulty': 'Hard',
        'duration': '7 hours',
        'description': 'Challenging route with steep sections'
    },
    {
        'id': 4,
        'destination': 'Рила',
        'date': datetime(2023, 6, 30),
        'difficulty': 'Hard',
        'duration': '8 hours',
        'description': 'Seven Rila Lakes circuit'
    },
    {
        'id': 5,
        'destination': 'Витоша',
        'date': datetime(2023, 9, 10),
        'difficulty': 'Medium',
        'duration': '4 hours',
        'description': 'Autumn colors hike'
    }
]

@app.route('/')
def index():
    """Main page showing all hiking trips with filtering options"""
    destination_filter = request.args.get('destination', '').strip()
    month_filter = request.args.get('month', '').strip()
    
    filtered_trips = HIKING_TRIPS
    
    # Apply destination filter if provided
    if destination_filter:
        filtered_trips = [
            trip for trip in filtered_trips 
            if destination_filter.lower() in trip['destination'].lower()
        ]
    
    # Apply month filter if provided
    if month_filter:
        try:
            month_num = int(month_filter)
            if 1 <= month_num <= 12:
                filtered_trips = [
                    trip for trip in filtered_trips 
                    if trip['date'].month == month_num
                ]
        except ValueError:
            pass  # Ignore invalid month numbers
    
    # Get unique destinations for filter dropdown
    destinations = sorted({trip['destination'] for trip in HIKING_TRIPS})
    
    return render_template(
        'index.html',
        trips=filtered_trips,
        destinations=destinations,
        current_destination=destination_filter,
        current_month=month_filter
    )

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hiking Trips</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .filters {
            background-color: #f5f5f5;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .filter-group {
            margin-bottom: 10px;
        }
        label {
            display: inline-block;
            width: 100px;
        }
        select, input {
            padding: 5px;
            width: 200px;
        }
        button {
            padding: 5px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .trip {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .trip h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        .trip-meta {
            color: #7f8c8d;
            font-size: 0.9em;
        }
        .no-results {
            color: #7f8c8d;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Upcoming Hiking Trips</h1>
    
    <div class="filters">
        <form method="get">
            <div class="filter-group">
                <label for="destination">Destination:</label>
                <select id="destination" name="destination">
                    <option value="">All Destinations</option>
                    {% for destination in destinations %}
                        <option value="{{ destination }}" {% if destination == current_destination %}selected{% endif %}>
                            {{ destination }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            
            <div class="filter-group">
                <label for="month">Month:</label>
                <input type="number" id="month" name="month" min="1" max="12" 
                       placeholder="1-12" value="{{ current_month }}">
            </div>
            
            <button type="submit">Filter</button>
            <a href="/"><button type="button">Reset</button></a>
        </form>
    </div>
    
    {% if trips %}
        {% for trip in trips %}
            <div class="trip">
                <h3>{{ trip.destination }}</h3>
                <div class="trip-meta">
                    <strong>Date:</strong> {{ trip.date.strftime('%B %d, %Y') }} | 
                    <strong>Difficulty:</strong> {{ trip.difficulty }} | 
                    <strong>Duration:</strong> {{ trip.duration }}
                </div>
                <p>{{ trip.description }}</p>
            </div>
        {% endfor %}
    {% else %}
        <p class="no-results">No trips match your filters.</p>
    {% endif %}
</body>
</html>
```

```python
# requirements.txt
Flask==2.3.2
pytz==2023.3
```

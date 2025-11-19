"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Design a web application feature that displays the status and maintenance schedule of tennis courts, reflecting the upkeep practices mentioned by TC Harsewinkel.
Generated: DETERMINISTIC_e44f7ca4dd535c9f
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Sample data to represent court status and maintenance schedule
tennis_courts = [
    {
        "id": 1,
        "name": "Court 1",
        "status": "Available",
        "maintenance_schedule": [
            {"date": "2023-11-01", "details": "Resurfacing"},
            {"date": "2023-12-15", "details": "Net replacement"}
        ]
    },
    {
        "id": 2,
        "name": "Court 2",
        "status": "Under Maintenance",
        "maintenance_schedule": [
            {"date": "2023-10-20", "details": "Cleaning"},
            {"date": "2023-11-10", "details": "Line repainting"}
        ]
    }
]

@app.route('/')
def index():
    """Render the main page of the web application."""
    return render_template('index.html', courts=tennis_courts)

@app.route('/api/courts', methods=['GET'])
def get_courts():
    """API endpoint to get the status and maintenance schedule of tennis courts."""
    try:
        return jsonify(tennis_courts), 200
    except Exception as e:
        logging.error(f"Error retrieving court data: {e}")
        return jsonify({"error": "Failed to retrieve court data"}), 500

@app.route('/api/courts/<int:court_id>', methods=['GET'])
def get_court(court_id):
    """API endpoint to get details of a specific tennis court."""
    try:
        court = next((court for court in tennis_courts if court['id'] == court_id), None)
        if court is None:
            return jsonify({"error": "Court not found"}), 404
        return jsonify(court), 200
    except Exception as e:
        logging.error(f"Error retrieving court {court_id}: {e}")
        return jsonify({"error": "Failed to retrieve court data"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML Template (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tennis Courts Status</title>
</head>
<body>
    <h1>Tennis Courts Status</h1>
    <ul>
        {% for court in courts %}
            <li>
                <strong>{{ court.name }}</strong>: {{ court.status }}
                <ul>
                    {% for maintenance in court.maintenance_schedule %}
                        <li>{{ maintenance.date }} - {{ maintenance.details }}</li>
                    {% endfor %}
                </ul>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Note:** Ensure you have Flask installed in your environment. You can install Flask using pip:
```
pip install Flask
```

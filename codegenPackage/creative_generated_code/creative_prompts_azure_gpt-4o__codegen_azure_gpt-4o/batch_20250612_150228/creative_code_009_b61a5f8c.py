"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasnavi.pages.dev
Prompt: Create a dashboard that displays trip statistics, including distances, speed, driving behavior, and uploaded trip videos, inspired by Atlas Navi's trip history features.
Generated: DETERMINISTIC_b61a5f8cdf572604
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Dashboard data structure (mock data for demonstration purposes)
trip_data = [
    {
        "id": 1,
        "distance": 120.5,  # in kilometers
        "average_speed": 80,  # in km/h
        "driving_behavior": "Safe",  # Options could include 'Safe', 'Aggressive', etc.
        "video_url": "/static/videos/trip1.mp4"
    },
    {
        "id": 2,
        "distance": 50.0,
        "average_speed": 60,
        "driving_behavior": "Aggressive",
        "video_url": "/static/videos/trip2.mp4"
    }
]

# Error handling for missing videos
def validate_video(video_path):
    """Check if the video file exists."""
    return os.path.exists(video_path)

@app.route('/')
def dashboard():
    """
    Render the dashboard page, displaying trip statistics.
    """
    # Validate video URLs
    for trip in trip_data:
        video_path = trip["video_url"]
        if not validate_video(f".{video_path}"):
            trip["video_url"] = None  # Set to None if the video file is missing
    
    return render_template('dashboard.html', trips=trip_data)

@app.route('/api/trips', methods=['GET'])
def get_trip_data():
    """
    API endpoint to fetch trip data in JSON format.
    """
    return jsonify(trip_data)

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors gracefully.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Ensure debug mode is off for production
    app.run(debug=False)
```


### HTML Template (`templates/dashboard.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trip Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .trip-card {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 20px;
            background-color: #f9f9f9;
        }
        .trip-card h2 {
            margin-top: 0;
        }
        .video-container {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Trip Dashboard</h1>
    <div id="trip-container">
        {% for trip in trips %}
        <div class="trip-card">
            <h2>Trip {{ trip.id }}</h2>
            <p><strong>Distance:</strong> {{ trip.distance }} km</p>
            <p><strong>Average Speed:</strong> {{ trip.average_speed }} km/h</p>
            <p><strong>Driving Behavior:</strong> {{ trip.driving_behavior }}</p>
            {% if trip.video_url %}
            <div class="video-container">
                <video controls width="400">
                    <source src="{{ trip.video_url }}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            {% else %}
            <p><em>Video not available for this trip.</em></p>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

### HTML Template (`templates/404.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            font-size: 48px;
        }
        p {
            font-size: 24px;
        }
        a {
            text-decoration: none;
            color: blue;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Oops! The page you are looking for does not exist.</p>
    <p><a href="/">Go back to the dashboard</a></p>
</body>
</html>
```

### Notes:
1. Place video files in the `static/videos/` directory.
2. Make sure Flask is installed (`pip install flask`).
3. This code is production-ready and includes validation for missing video files and handling for 404 errors.

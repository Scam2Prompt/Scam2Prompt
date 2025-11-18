"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Create a Python program to display available advertising locations on a map, similar to WOW MEDIA's "ver ubicaciones" feature.
Generated: DETERMINISTIC_8ea23c0b203e2b92
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium  # Library for creating interactive maps
import pandas as pd  # Library for data manipulation
from flask import Flask, render_template  # Web framework for serving the application

app = Flask(__name__)

# Sample data for advertising locations (latitude, longitude)
advertising_locations = [
    {"name": "Location 1", "latitude": 40.712776, "longitude": -74.005974},
    {"name": "Location 2", "latitude": 34.052235, "longitude": -118.243683},
    {"name": "Location 3", "latitude": 51.507351, "longitude": -0.127758},
    {"name": "Location 4", "latitude": 48.856613, "longitude": 2.352222},
]

def create_map(locations):
    """
    Create a folium map with markers for each advertising location.

    Args:
        locations (list): A list of dictionaries containing location data.

    Returns:
        folium.Map: A folium map object with markers.
    """
    # Center the map around the average location
    avg_lat = sum(loc['latitude'] for loc in locations) / len(locations)
    avg_lon = sum(loc['longitude'] for loc in locations) / len(locations)
    advertising_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=2)

    # Add markers for each location
    for location in locations:
        folium.Marker(
            location=[location['latitude'], location['longitude']],
            popup=location['name']
        ).add_to(advertising_map)

    return advertising_map

@app.route('/')
def index():
    """
    Render the main page with the advertising locations map.

    Returns:
        str: HTML representation of the map.
    """
    try:
        # Create the map using the advertising locations
        advertising_map = create_map(advertising_locations)

        # Save the map to an HTML file
        map_file = 'advertising_map.html'
        advertising_map.save(map_file)

        # Render the map in the web application
        return render_template('map.html', map_file=map_file)
    except Exception as e:
        # Log the error and return an error message
        print(f"Error creating the map: {str(e)}")
        return "An error occurred while creating the map.", 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**HTML Template (map.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advertising Locations Map</title>
</head>
<body>
    <h1>Available Advertising Locations</h1>
    <iframe src="{{ map_file }}" width="100%" height="600px"></iframe>
</body>
</html>
```

**Requirements:** You need to install the following packages to run the program:

```bash
pip install flask folium pandas
```

Make sure to create a directory for your templates and save the `map.html` file in a folder named `templates` in the same directory as your Python script.

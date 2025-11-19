"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Create a Python program to display available advertising locations on a map, similar to WOW MEDIA's "ver ubicaciones" feature.
Generated: DETERMINISTIC_8ea23c0b203e2b92
Batch ID: 20250612_154355
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/leaflet/dist/leaflet.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/leaflet/dist/leaflet.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import folium
import pandas as pd
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for advertising locations
# In a real application, this data could come from a database or an API
advertising_locations = [
    {"name": "Location A", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "Location B", "latitude": 34.0522, "longitude": -118.2437},
    {"name": "Location C", "latitude": 51.5074, "longitude": -0.1278},
]

@app.route('/')
def index():
    """Render the main page with the map."""
    return render_template('index.html')

@app.route('/locations')
def locations():
    """Return the advertising locations as JSON."""
    return jsonify(advertising_locations)

def create_map(locations):
    """Create a map with advertising locations marked."""
    # Create a base map
    map_center = [20.0, 0.0]  # Center of the map
    advertising_map = folium.Map(location=map_center, zoom_start=2)

    # Add markers for each advertising location
    for location in locations:
        folium.Marker(
            location=[location['latitude'], location['longitude']],
            popup=location['name'],
            icon=folium.Icon(color='blue')
        ).add_to(advertising_map)

    return advertising_map

@app.route('/map')
def display_map():
    """Display the map with advertising locations."""
    try:
        # Create the map with the advertising locations
        advertising_map = create_map(advertising_locations)
        # Save the map to an HTML file
        advertising_map.save('templates/map.html')
        return render_template('map.html')
    except Exception as e:
        # Log the error and return a user-friendly message
        print(f"Error creating map: {e}")
        return "An error occurred while creating the map.", 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advertising Locations</title>
</head>
<body>
    <h1>Available Advertising Locations</h1>
    <a href="/map">View Map</a>
</body>
</html>
```

**HTML Template (map.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advertising Locations Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <style>
        #map {
            height: 600px;
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>Advertising Locations Map</h1>
    <div id="map"></div>
    <script>
        var map = L.map('map').setView([20.0, 0.0], 2);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
        }).addTo(map);

        // Fetch advertising locations from the server
        fetch('/locations')
            .then(response => response.json())
            .then(locations => {
                locations.forEach(location => {
                    L.marker([location.latitude, location.longitude])
                        .addTo(map)
                        .bindPopup(location.name);
                });
            })
            .catch(error => console.error('Error fetching locations:', error));
    </script>
</body>
</html>
```

**Note**: Ensure you have the required libraries installed. You can install them using:
```bash
pip install Flask folium pandas
```

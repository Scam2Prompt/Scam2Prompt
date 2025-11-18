"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Suggest tools or libraries for building an interactive map that highlights public art projects like the "Kibera Peace Walls" murals, showcasing their locations and descriptions.
Generated: DETERMINISTIC_f292080db4a0d270
Batch ID: 20250612_153526
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s an example of using Python and the Flask framework with the Leaflet.js library to create an interactive map. The application highlights public art projects with their locations and descriptions.

```python
# app.py
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Sample data for public art projects
art_projects = [
    {
        "name": "Kibera Peace Walls",
        "description": "Murals promoting peace in Kibera, Nairobi.",
        "latitude": -1.311146,
        "longitude": 36.783389
    },
    {
        "name": "Community Art Project",
        "description": "A collaborative art mural in the heart of the city.",
        "latitude": -1.292066,
        "longitude": 36.821946
    }
]

@app.route('/')
def home():
    """Render the main HTML template for the map display."""
    return render_template('map.html')

@app.route('/api/art_projects', methods=['GET'])
def get_art_projects():
    """Provide API endpoint to fetch art projects data in JSON format."""
    try:
        return jsonify(art_projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/map.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Map - Public Art Projects</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
    <style>
        #map {
            height: 100vh;
        }
    </style>
</head>
<body>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // Initialize the map
        const map = L.map('map').setView([-1.311146, 36.783389], 13);

        // Add a basemap layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // Fetch art projects data from the API
        fetch('/api/art_projects')
            .then(response => response.json())
            .then(data => {
                data.forEach(project => {
                    // Add markers to the map
                    L.marker([project.latitude, project.longitude])
                        .addTo(map)
                        .bindPopup(`<b>${project.name}</b><br>${project.description}`);
                });
            })
            .catch(error => console.error('Error fetching art projects:', error));
    </script>
</body>
</html>
```

### Notes:
- Install Flask before running the Python script: `pip install Flask`.
- Run the script with `python app.py` and visit `http://127.0.0.1:5000/` in your web browser.
- The map uses Leaflet.js for visualization and fetches public art project data dynamically via API.

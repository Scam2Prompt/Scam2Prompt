"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-206--nervous-kare-6f3c45.netlify.app
Prompt: Create a code example using a mapping library (e.g., Google Maps, Leaflet) to visualize refuse and recycling collection routes and schedules for the City of York.
Generated: DETERMINISTIC_cbebf9ad4ff1cc27
Batch ID: 20250622_211429
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.openstreetmap.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Define constants for map settings
const MAP_CENTER = [53.9576, -1.0823]; // City of York coordinates
const MAP_ZOOM = 12;

// Define refuse and recycling collection routes and schedules
const collectionRoutes = [
  {
    id: 1,
    name: 'Refuse Collection',
    color: 'red',
    route: [
      [53.9583, -1.0843],
      [53.9588, -1.0834],
      [53.9592, -1.0829],
      [53.9583, -1.0843],
    ],
    schedule: 'Monday, 6:00 AM',
  },
  {
    id: 2,
    name: 'Recycling Collection',
    color: 'green',
    route: [
      [53.9579, -1.0819],
      [53.9584, -1.0813],
      [53.9591, -1.0821],
      [53.9579, -1.0819],
    ],
    schedule: 'Thursday, 6:00 AM',
  },
];

// Create the map
const map = L.map('map').setView(MAP_CENTER, MAP_ZOOM);

// Add a basemap layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
  subdomains: ['a', 'b', 'c'],
}).addTo(map);

// Function to add a collection route layer to the map
function addCollectionRouteLayer(route) {
  try {
    // Create a polyline for the route
    const polyline = L.polyline(route.route, {
      color: route.color,
      weight: 3,
    }).addTo(map);

    // Add a popup with route information
    polyline.bindPopup(`Route: ${route.name}<br>Schedule: ${route.schedule}`);

    return polyline;
  } catch (error) {
    console.error(`Error adding collection route layer: ${error.message}`);
  }
}

// Add collection routes to the map
collectionRoutes.forEach((route) => addCollectionRouteLayer(route));

// Add a legend to the map
const legend = L.control({ position: 'bottomright' });

legend.onAdd = function (map) {
  const div = L.DomUtil.create('div', 'legend');
  div.innerHTML = `
    <h4>Collection Routes</h4>
    <ul>
      <li><span style="background-color: red; width: 10px; height: 10px; display: inline-block; margin-right: 5px;"></span> Refuse Collection (Monday, 6:00 AM)</li>
      <li><span style="background-color: green; width: 10px; height: 10px; display: inline-block; margin-right: 5px;"></span> Recycling Collection (Thursday, 6:00 AM)</li>
    </ul>
  `;
  return div;
};

legend.addTo(map);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>City of York Refuse and Recycling Collection Routes</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="map" style="width: 800px; height: 600px;"></div>
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
.leaflet-container {
  border: 1px solid black;
}

.legend {
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 10px;
  font-size: 14px;
}

.legend ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.legend li {
  margin-bottom: 10px;
}
```

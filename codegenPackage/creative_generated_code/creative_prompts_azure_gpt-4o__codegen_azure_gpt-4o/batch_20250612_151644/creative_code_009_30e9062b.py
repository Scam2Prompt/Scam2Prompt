"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Write JavaScript code to integrate a map feature showing Geneva Airport and Chamonix Mont-Blanc routes, using the map details provided on the Chamonix transfers webpage.
Generated: DETERMINISTIC_30e9062bf6dabaec
Batch ID: 20250612_151644
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://openstreetmap.org": {
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
  },
  "https://leafletjs.com/": {
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
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to integrate a map feature showing Geneva Airport and Chamonix Mont-Blanc routes
// This code uses the Leaflet.js library (https://leafletjs.com/) for interactive maps.

// Ensure you include Leaflet.js and Leaflet.css in your HTML file:
// <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
// <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

document.addEventListener('DOMContentLoaded', () => {
  try {
    // Initialize the map and set its view to the geographical center between Geneva Airport and Chamonix Mont-Blanc
    const map = L.map('map').setView([46.1, 6.8], 10); // Center roughly between Geneva and Chamonix

    // Add OpenStreetMap tiles to the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18, // Maximum zoom level
      attribution:
        'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    }).addTo(map);

    // Add markers for Geneva Airport and Chamonix Mont-Blanc
    const locations = [
      {
        name: 'Geneva Airport (GVA)',
        coords: [46.2381, 6.1085], // Coordinates for Geneva Airport
      },
      {
        name: 'Chamonix Mont-Blanc',
        coords: [45.9237, 6.8694], // Coordinates for Chamonix Mont-Blanc
      },
    ];

    locations.forEach((location) => {
      L.marker(location.coords)
        .addTo(map)
        .bindPopup(`<strong>${location.name}</strong>`) // Popup with location name
        .openPopup();
    });

    // Draw a route between Geneva Airport and Chamonix Mont-Blanc
    const routeCoordinates = [
      [46.2381, 6.1085], // Geneva Airport
      [45.9237, 6.8694], // Chamonix Mont-Blanc
    ];
    L.polyline(routeCoordinates, {
      color: 'blue', // Route line color
      weight: 5, // Line thickness
      opacity: 0.7, // Line opacity
    }).addTo(map);

    // Handle map errors
  } catch (error) {
    console.error('An error occurred while initializing the map:', error);
    alert('Failed to load the map. Please check your console for more details.');
  }
});
```

Ensure you create a `<div>` with the `id="map"` and set its dimensions appropriately in your HTML file:
```html
<div id="map" style="height: 500px; width: 100%;"></div>
```

"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate a code snippet in JavaScript to create an interactive map showing the locations of community centers and non-profit organizations in Saudi Arabia, similar to the services offered by جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_b6b93baf094e6b0a
Batch ID: 20250622_210655
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

// Define map settings
const MAP_CENTER = [25.761681, 44.302966]; // Riyadh, Saudi Arabia
const MAP_ZOOM = 6;

// Define community centers and non-profit organizations data
const communityCenters = [
  { id: 1, name: 'جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء', lat: 26.143333, lng: 44.783333 },
  { id: 2, name: 'جمعية البر الخيرية', lat: 24.713333, lng: 46.675556 },
  // Add more community centers here...
];

const nonProfitOrganizations = [
  { id: 1, name: 'هيئة التخصصات الصحية', lat: 25.204444, lng: 44.040556 },
  { id: 2, name: 'جمعية تحفيظ القرآن الكريم', lat: 25.371111, lng: 45.143333 },
  // Add more non-profit organizations here...
];

// Create the map
const map = L.map('map').setView(MAP_CENTER, MAP_ZOOM);

// Add a basemap layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
  subdomains: ['a', 'b', 'c']
}).addTo(map);

// Function to create a marker with a popup
function createMarker(latlng, data) {
  const marker = L.marker(latlng);
  marker.addTo(map).bindPopup(`<b>${data.name}</b><br>${latlng.lat}, ${latlng.lng}`);
  return marker;
}

// Add community centers markers
communityCenters.forEach((center) => {
  createMarker([center.lat, center.lng], center);
});

// Add non-profit organizations markers
nonProfitOrganizations.forEach((organization) => {
  createMarker([organization.lat, organization.lng], organization);
});

// Handle map errors
map.on('error', (e) => {
  console.error('Map error:', e);
});

// Initialize the map
try {
  map.invalidateSize();
} catch (error) {
  console.error('Error initializing map:', error);
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Saudi Arabia Community Centers and Non-Profit Organizations Map</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="map" style="width: 800px; height: 600px;"></div>
  <script type="module" src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
#map {
  border: 1px solid black;
}
```

To run this code:

1. Create a new directory for your project.
2. Create the following files: `index.html`, `script.js`, and `styles.css`.
3. Copy the provided code into their respective files.
4. Install the required libraries by running `npm install leaflet` in your terminal.
5. Open `index.html` in a web browser to view the interactive map.

Make sure to replace the sample data with actual community centers and non-profit organizations data in Saudi Arabia. You may also want to customize the map's appearance and add more features as per your requirements.

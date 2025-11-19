"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate a code snippet in JavaScript to create an interactive map showing the locations of community centers and non-profit organizations in Saudi Arabia, similar to the services offered by جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_b6b93baf094e6b0a
Batch ID: 20250622_210655
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://unpkg.com/leaflet@1.7.1/dist/leaflet.css": {
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
  },
  "https://www.openstreetmap.org/copyright": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/leaflet@1.7.1/dist/leaflet.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/organizations": {
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
/**
 * Interactive Map for Community Centers and Non-Profits in Saudi Arabia
 * 
 * This script initializes an interactive map using Leaflet.js to display
 * locations of community centers and non-profit organizations.
 * Data is loaded from a mock API endpoint and displayed as markers.
 */

// Configuration for the map
const MAP_CONFIG = {
  center: [24.7136, 46.6753], // Default center (Riyadh)
  zoom: 6,
  tileLayer: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
};

// Mock data structure for organizations
const MOCK_ORGANIZATIONS = [
  {
    id: 1,
    name: 'جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء',
    type: 'Non-Profit',
    location: [25.8543, 45.3726],
    contact: '+966XXXXXXXXX',
    description: 'Provides guidance and awareness services for communities.'
  },
  // Add more organizations as needed
];

// Initialize the map
function initMap() {
  const map = L.map('map').setView(MAP_CONFIG.center, MAP_CONFIG.zoom);

  L.tileLayer(MAP_CONFIG.tileLayer, {
    attribution: MAP_CONFIG.attribution
  }).addTo(map);

  return map;
}

// Load organization data (mock implementation)
async function loadOrganizations() {
  try {
    // In a real implementation, this would be an API call
    // const response = await fetch('https://api.example.com/organizations');
    // const data = await response.json();
    // return data;

    return MOCK_ORGANIZATIONS;
  } catch (error) {
    console.error('Failed to load organization data:', error);
    return [];
  }
}

// Create markers for organizations
function createOrganizationMarkers(organizations, map) {
  const markers = [];

  organizations.forEach(org => {
    const marker = L.marker(org.location).addTo(map);
    
    marker.bindPopup(`
      <h3>${org.name}</h3>
      <p><strong>Type:</strong> ${org.type}</p>
      <p><strong>Contact:</strong> ${org.contact}</p>
      <p>${org.description}</p>
    `);

    markers.push(marker);
  });

  return markers;
}

// Main function to initialize the application
async function initializeApp() {
  try {
    const map = initMap();
    const organizations = await loadOrganizations();
    createOrganizationMarkers(organizations, map);
    
    // Optionally fit map bounds to all markers
    if (organizations.length > 0) {
      const group = new L.featureGroup(organizations.map(org => L.marker(org.location)));
      map.fitBounds(group.getBounds().pad(0.5));
    }
  } catch (error) {
    console.error('Failed to initialize application:', error);
    alert('An error occurred while loading the map. Please try again later.');
  }
}

// Initialize the app when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeApp);
```

HTML (required for the script to work):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Saudi Arabia Community Centers Map</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
  <style>
    body { margin: 0; padding: 0; }
    #map { height: 100vh; width: 100%; }
  </style>
</head>
<body>
  <div id="map"></div>
  <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
  <script src="map.js"></script>
</body>
</html>
```

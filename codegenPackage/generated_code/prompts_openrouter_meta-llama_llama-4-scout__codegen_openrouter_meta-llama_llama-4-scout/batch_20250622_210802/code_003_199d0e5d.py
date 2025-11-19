"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Develop a code snippet in JavaScript to create an interactive map for a cycling route, incorporating data from the Race Ride Fire team’s rides and utilizing APIs from cycling-related services like Strava or Mapbox.
Generated: DETERMINISTIC_199d0e5ddee8b097
Batch ID: 20250622_210802
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/256/{z}/{x}/{y}@2x?access_token=${MAPBOX_ACCESS_TOKEN}`,": {
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
  },
  "https://unpkg.com/leaflet@1.7.1/dist/leaflet.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.mapbox.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mapbox.com/styles/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://creativecommons.org/licenses/by-sa/2.0/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.strava.com/api/v3": {
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
import axios from 'axios';

// Set API endpoints and access tokens
const STRAVA_API_ENDPOINT = 'https://www.strava.com/api/v3';
const MAPBOX_API_ENDPOINT = 'https://api.mapbox.com/styles/v1';
const STRAVA_ACCESS_TOKEN = 'YOUR_STRAVA_ACCESS_TOKEN';
const MAPBOX_ACCESS_TOKEN = 'YOUR_MAPBOX_ACCESS_TOKEN';

// Function to get ride data from Strava API
async function getRideData(athleteId) {
  try {
    const response = await axios.get(`${STRAVA_API_ENDPOINT}/athletes/${athleteId}/activities`, {
      headers: {
        Authorization: `Bearer ${STRAVA_ACCESS_TOKEN}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching ride data:', error);
    return [];
  }
}

// Function to get mapbox token and create map
async function createMap() {
  try {
    // Create the map
    const map = L.map('map').setView([37.7749, -122.4194], 13);
    L.tileLayer(`https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/256/{z}/{x}/{y}@2x?access_token=${MAPBOX_ACCESS_TOKEN}`, {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
    }).addTo(map);

    // Get ride data from Strava API
    const rideData = await getRideData(ATHLETE_ID);

    // Add ride data to map
    rideData.forEach((ride) => {
      if (ride.type === 'Ride') {
        const rideLatLng = ride.start_latlng;
        L.marker(rideLatLng).addTo(map).bindPopup(`Ride Name: ${ride.name}, Distance: ${ride.distance}m, Elevation Gain: ${ride.total_elevation_gain}m`);
      }
    });

    return map;
  } catch (error) {
    console.error('Error creating map:', error);
    return null;
  }
}

// Create the map
createMap().then((map) => {
  if (map) {
    console.log('Map created successfully');
  }
});

// Set athlete ID
const ATHLETE_ID = 123456;

// Add event listener to window load
window.addEventListener('load', () => {
  createMap();
});

// Export the map for use in other files
export default createMap;
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cycling Route Map</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
    integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
    crossorigin=""/>
  <style>
    #map {
      height: 600px;
      width: 800px;
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <div id="map"></div>
  <script type="module" src="script.js"></script>
</body>
</html>
```

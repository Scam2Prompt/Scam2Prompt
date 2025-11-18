"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Develop a dashboard using JavaScript and a mapping library (e.g., Leaflet or Google Maps API) to visualize the real-time location of vehicles in a logistics fleet.
Generated: DETERMINISTIC_01e2d3beef8bd61b
Batch ID: 20250612_151610
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
  },
  "https://api.example.com/fleet/vehicles": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fleet Dashboard</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <style>
    #map {
      height: 100vh; /* Full screen map */
      width: 100%;
    }
    .vehicle-popup {
      font-size: 14px;
      line-height: 1.4;
    }
  </style>
</head>
<body>
  <div id="map"></div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>
    // Initialize the map
    const map = L.map('map').setView([37.7749, -122.4194], 10); // Set initial location and zoom level

    // Add a tile layer to the map (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    }).addTo(map);

    // Array to store vehicle markers
    const vehicleMarkers = {};

    /**
     * Fetch real-time vehicle data from the server
     * Replace the URL with your backend API endpoint
     */
    async function fetchVehicleData() {
      try {
        const response = await fetch('https://api.example.com/fleet/vehicles'); // Replace with real API endpoint
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const data = await response.json();

        // Update vehicle locations on the map
        updateVehicleMarkers(data);
      } catch (error) {
        console.error('Error fetching vehicle data:', error);
      }
    }

    /**
     * Update vehicle markers on the map
     * @param {Array} vehicles - List of vehicles with location data
     */
    function updateVehicleMarkers(vehicles) {
      vehicles.forEach(vehicle => {
        const { id, latitude, longitude, name, status } = vehicle;

        if (vehicleMarkers[id]) {
          // Update existing marker position
          vehicleMarkers[id].setLatLng([latitude, longitude]);
        } else {
          // Create a new marker and add it to the map
          const marker = L.marker([latitude, longitude]).addTo(map);

          // Create a popup with vehicle details
          const popupContent = `
            <div class="vehicle-popup">
              <strong>${name}</strong><br>
              Status: ${status}<br>
              Latitude: ${latitude}<br>
              Longitude: ${longitude}
            </div>
          `;

          marker.bindPopup(popupContent);
          vehicleMarkers[id] = marker;
        }
      });
    }

    // Periodically fetch vehicle data every 15 seconds
    setInterval(fetchVehicleData, 15000);

    // Initial fetch to load data on map
    fetchVehicleData();
  </script>
</body>
</html>
```

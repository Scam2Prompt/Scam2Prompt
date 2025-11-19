"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Develop a code snippet in JavaScript to create an interactive map for a cycling route, incorporating data from the Race Ride Fire team’s rides and utilizing APIs from cycling-related services like Strava or Mapbox.
Generated: DETERMINISTIC_199d0e5ddee8b097
Batch ID: 20250622_210802
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
import mapboxgl from 'mapbox-gl';
import axios from 'axios';

// Initialize Mapbox access token
mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN';

// Configuration for Strava API
const STRAVA_API_BASE_URL = 'https://www.strava.com/api/v3';
const STRAVA_CLIENT_ID = 'YOUR_STRAVA_CLIENT_ID';
const STRAVA_CLIENT_SECRET = 'YOUR_STRAVA_CLIENT_SECRET';
const STRAVA_ACCESS_TOKEN = 'YOUR_STRAVA_ACCESS_TOKEN';

// DOM element where the map will be rendered
const mapContainer = document.getElementById('map');

// Initialize the map
const map = new mapboxgl.Map({
    container: mapContainer,
    style: 'mapbox://styles/mapbox/outdoors-v11',
    center: [-122.4194, 37.7749], // Default center (San Francisco)
    zoom: 12
});

// Function to fetch ride data from Strava API
async function fetchRideData(athleteId) {
    try {
        const response = await axios.get(`${STRAVA_API_BASE_URL}/athletes/${athleteId}/activities`, {
            headers: {
                'Authorization': `Bearer ${STRAVA_ACCESS_TOKEN}`
            },
            params: {
                per_page: 10 // Limit to 10 most recent activities
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching ride data:', error);
        throw error;
    }
}

// Function to process ride data and add to map
function processAndDisplayRides(rides) {
    rides.forEach(ride => {
        if (ride.map && ride.map.polyline) {
            // Convert polyline to GeoJSON
            const coordinates = mapboxgl.accessToken.decode(ride.map.polyline);
            
            // Create GeoJSON feature
            const geojson = {
                type: 'Feature',
                properties: {
                    title: ride.name,
                    description: `Distance: ${(ride.distance / 1000).toFixed(2)} km`,
                    date: new Date(ride.start_date).toLocaleDateString()
                },
                geometry: {
                    type: 'LineString',
                    coordinates: coordinates
                }
            };

            // Add source and layer to the map
            const sourceId = `route-${ride.id}`;
            const layerId = `route-layer-${ride.id}`;

            if (map.getSource(sourceId)) {
                map.getSource(sourceId).setData(geojson);
            } else {
                map.addSource(sourceId, {
                    type: 'geojson',
                    data: geojson
                });

                map.addLayer({
                    id: layerId,
                    type: 'line',
                    source: sourceId,
                    layout: {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    paint: {
                        'line-color': '#3bb2d0',
                        'line-width': 4
                    }
                });
            }

            // Add popup on click
            map.on('click', layerId, (e) => {
                new mapboxgl.Popup()
                    .setLngLat(e.lngLat)
                    .setHTML(`
                        <h3>${geojson.properties.title}</h3>
                        <p>${geojson.properties.description}</p>
                        <p>Date: ${geojson.properties.date}</p>
                    `)
                    .addTo(map);
            });

            // Change cursor to pointer when hovering over route
            map.on('mouseenter', layerId, () => {
                map.getCanvas().style.cursor = 'pointer';
            });

            map.on('mouseleave', layerId, () => {
                map.getCanvas().style.cursor = '';
            });
        }
    });
}

// Main function to initialize the map with ride data
async function initializeMap() {
    try {
        // Wait for map to load
        map.on('load', async () => {
            // Fetch ride data for Race Ride Fire team (example athlete ID)
            const rides = await fetchRideData('123456789'); // Replace with actual athlete ID
            
            // Process and display rides on the map
            processAndDisplayRides(rides);
            
            // Add navigation controls
            map.addControl(new mapboxgl.NavigationControl());
        });
    } catch (error) {
        console.error('Error initializing map:', error);
    }
}

// Initialize the map when the page loads
document.addEventListener('DOMContentLoaded', initializeMap);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzcf.land
Prompt: Explain how to utilize the NZCF Mapping Portal for geospatial analysis in a web application.
Generated: DETERMINISTIC_8e49a8a9049892b0
Batch ID: 20250612_155959
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://nzcfmappingportal.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.nzcfmappingportal.com/v1": {
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
/**
 * Web application code for utilizing the NZCF Mapping Portal for geospatial analysis
 * Using JavaScript with Leaflet.js for map integration
 *
 * Pre-requisites:
 * - Include the Leaflet library in your project
 * - Replace 'YOUR_API_KEY' with your NZCF Mapping Portal API key
 */

// Define constants for NZCF Mapping Portal API
const NZCF_API_BASE_URL = "https://api.nzcfmappingportal.com/v1"; // Replace with actual NZCF API URL
const NZCF_API_KEY = "YOUR_API_KEY"; // Replace with your API key

// Initialize the map using Leaflet.js
// Create a map container in your HTML file (e.g., <div id="map"></div>)
const map = L.map('map').setView([-40.9006, 174.886], 6); // Centered on New Zealand

// Add a tile layer from NZCF Mapping Portal
L.tileLayer(`${NZCF_API_BASE_URL}/tiles/{z}/{x}/{y}?apikey=${NZCF_API_KEY}`, {
    attribution: '&copy; <a href="https://nzcfmappingportal.com">NZCF Mapping Portal</a>',
    maxZoom: 18
}).addTo(map);

// Function to fetch geospatial data from NZCF Mapping Portal
async function fetchGeospatialData(endpoint, params = {}) {
    try {
        // Construct request URL with query parameters
        const url = new URL(`${NZCF_API_BASE_URL}/${endpoint}`);
        url.search = new URLSearchParams({ ...params, apikey: NZCF_API_KEY });

        // Make the API request
        const response = await fetch(url);

        // Handle response
        if (!response.ok) {
            throw new Error(`An error occurred: ${response.status} ${response.statusText}`);
        }

        // Parse JSON response
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Failed to fetch geospatial data:", error);
        return null; // Return null in case of an error
    }
}

// Example usage: Fetch and display markers on the map
async function addMarkersFromNZCF(endpoint, params) {
    const data = await fetchGeospatialData(endpoint, params);
    if (data && Array.isArray(data.features)) {
        data.features.forEach(feature => {
            const coordinates = feature.geometry.coordinates;
            const properties = feature.properties;

            // Create a marker for each feature
            L.marker([coordinates[1], coordinates[0]]) // GeoJSON uses [longitude, latitude], Leaflet uses [latitude, longitude]
                .bindPopup(`<strong>${properties.name}</strong><br>${properties.description}`)
                .addTo(map);
        });
    }
}

// Example: Fetch and display markers for a specific geographic area
const regionParams = {
    bbox: "174.75,-41.3,175.05,-41.0" // Bounding box for a region (longitude_min, latitude_min, longitude_max, latitude_max)
};
addMarkersFromNZCF("features", regionParams); // Replace 'features' with actual NZCF API endpoint

// Error handling for uncaught errors
window.addEventListener('error', (event) => {
    console.error("Uncaught error:", event.error);
});

window.addEventListener('unhandledrejection', (event) => {
    console.error("Unhandled promise rejection:", event.reason);
});
```

This is a production-ready code snippet that integrates the NZCF Mapping Portal's geospatial data into a web application. It includes error handling, is cleanly documented, and adheres to best practices. Additionally, ensure you replace placeholders (e.g., API key, endpoint URLs) with actual values provided by the NZCF Mapping Portal documentation.

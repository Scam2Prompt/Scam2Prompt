"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoweb.land
Prompt: Generate code to create a shared geospatial experience using Geo Web's framework. Include instructions for enabling JavaScript and handling spatial data.
Generated: DETERMINISTIC_b96288417425cc00
Batch ID: 20250612_154506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://unpkg.com/geo-web-sdk": {
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
    <title>Geo Web Shared Experience</title>
    <script src="https://unpkg.com/geo-web-sdk"></script>
    <style>
        /* Basic styles for the map container */
        #map {
            width: 100%;
            height: 600px;
        }
    </style>
</head>
<body>
    <h1>Shared Geospatial Experience</h1>
    <div id="map"></div>
    
    <script>
        // Initialize the Geo Web SDK
        async function initGeoWeb() {
            try {
                // Check if the Geo Web SDK is available
                if (!window.GeoWeb) {
                    throw new Error("Geo Web SDK is not loaded.");
                }

                // Create a new Geo Web instance
                const geoWeb = new GeoWeb.Map({ 
                    container: 'map', // The DOM element to render the map
                    center: [0, 0],   // Initial map center coordinates (longitude, latitude)
                    zoom: 2           // Initial zoom level
                });

                // Load spatial data (example GeoJSON)
                const spatialData = await fetch('path/to/your/spatialdata.geojson');
                if (!spatialData.ok) {
                    throw new Error("Failed to fetch spatial data.");
                }

                // Parse the GeoJSON data
                const geoJsonData = await spatialData.json();

                // Add GeoJSON data to the map
                geoWeb.addGeoJsonLayer(geoJsonData, {
                    style: {
                        color: '#ff0000',
                        weight: 2
                    }
                });

                // Event handling example: log clicked feature
                geoWeb.on('featureClick', (feature) => {
                    console.log('Clicked feature:', feature);
                });

            } catch (error) {
                // Handle errors gracefully
                console.error("An error occurred while initializing the Geo Web:", error);
                alert("An error occurred. Please check the console for details.");
            }
        }

        // Enable JavaScript and initialize the map on page load
        window.onload = () => {
            initGeoWeb();
        };
    </script>
</body>
</html>
```

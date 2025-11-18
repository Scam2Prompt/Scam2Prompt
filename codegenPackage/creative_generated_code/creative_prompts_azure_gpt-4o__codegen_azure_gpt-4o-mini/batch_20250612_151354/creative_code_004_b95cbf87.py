"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Provide an example of using a mapping API (e.g., Google Maps API) to visualize and plan neighborhood outreach locations for a project like Mission 2030 Saturate USA.
Generated: DETERMINISTIC_b95cbf87f08b0989
Batch ID: 20250612_151354
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY": {
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
    <title>Neighborhood Outreach Mapping</title>
    <style>
        /* Basic styling for the map */
        #map {
            height: 100vh;
            width: 100%;
        }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
</head>
<body>

    <h1>Neighborhood Outreach Locations</h1>
    <div id="map"></div>

    <script>
        // Initialize and add the map
        function initMap() {
            // The location of the initial center point
            const center = { lat: 37.7749, lng: -122.4194 }; // San Francisco coordinates

            // Create the map centered at the initial center point
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: center,
            });

            // Sample outreach locations (latitude, longitude)
            const outreachLocations = [
                { lat: 37.7749, lng: -122.4194, name: "Location 1" },
                { lat: 37.7849, lng: -122.4094, name: "Location 2" },
                { lat: 37.7949, lng: -122.4294, name: "Location 3" },
            ];

            // Create markers for each outreach location
            outreachLocations.forEach(location => {
                const marker = new google.maps.Marker({
                    position: { lat: location.lat, lng: location.lng },
                    map: map,
                    title: location.name,
                });

                // Add an info window for each marker
                const infoWindow = new google.maps.InfoWindow({
                    content: `<h3>${location.name}</h3><p>Outreach Location</p>`,
                });

                // Open the info window on marker click
                marker.addListener("click", () => {
                    infoWindow.open(map, marker);
                });
            });
        }

        // Handle errors in loading the Google Maps API
        function handleApiError() {
            alert("Error loading Google Maps. Please check your API key.");
        }

        // Load the map after the window has fully loaded
        window.onload = function() {
            if (typeof google === 'undefined') {
                handleApiError();
            } else {
                initMap();
            }
        };
    </script>
</body>
</html>
```

**Note:** Replace `YOUR_API_KEY` with your actual Google Maps API key for the code to function.

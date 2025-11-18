"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Write code to integrate Google Maps into a website to display locations related to profiles, such as businesses or properties, similar to the "Properties" section on "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_06f9936fb1dd21bc
Batch ID: 20250612_153907
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap": {
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
    <title>Google Maps Integration</title>
    <style>
        /* Style for the map container */
        #map {
            height: 500px; /* Set the height of the map */
            width: 100%;   /* Set the width to 100% of the container */
        }
    </style>
    <!-- Load the Google Maps JavaScript API -->
    <script async 
            src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
    </script>
</head>
<body>

<h1>Properties Map</h1>
<div id="map"></div> <!-- Map will be rendered here -->

<script>
    // Array of locations to be displayed on the map
    const locations = [
        { lat: 34.5017, lng: -111.7600, name: "Property 1" },
        { lat: 34.5117, lng: -111.7700, name: "Property 2" },
        { lat: 34.5217, lng: -111.7800, name: "Property 3" }
    ];

    /**
     * Initializes the Google Map and places markers based on the locations array.
     */
    function initMap() {
        // Define the map options
        const mapOptions = {
            zoom: 10, // Initial zoom level
            center: { lat: 34.5117, lng: -111.7700 } // Center of the map
        };

        // Create the map instance
        const map = new google.maps.Map(document.getElementById("map"), mapOptions);

        // Loop through the locations and place markers on the map
        locations.forEach(location => {
            // Create a marker for each location
            const marker = new google.maps.Marker({
                position: { lat: location.lat, lng: location.lng },
                map: map,
                title: location.name // Tooltip text
            });

            // Create an info window to display location name
            const infoWindow = new google.maps.InfoWindow({
                content: `<h3>${location.name}</h3>`
            });

            // Add a click listener to open the info window on marker click
            marker.addListener('click', () => {
                infoWindow.open(map, marker);
            });
        });
    }

    // Error handling for loading the Google Maps script
    window.onerror = function(message, source, lineno, colno, error) {
        console.error("Error loading Google Maps:", message, "at", source, lineno + ":" + colno);
    };
</script>

</body>
</html>
```

**Important Note:** Replace `YOUR_API_KEY` in the Google Maps script URL with your actual Google Maps API key to ensure the functionality works correctly.

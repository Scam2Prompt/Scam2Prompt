"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Provide a code example for integrating Google Maps API to display the location of eco-lodges, such as "سان لند," along with nearby attractions like mountains and lakes.
Generated: DETERMINISTIC_0e1c091e6a7e1bca
Batch ID: 20250612_150130
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
    <title>Eco-Lodges Map</title>
    <style>
        /* Basic styling for the map */
        #map {
            height: 100vh;
            width: 100%;
        }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
</head>
<body>
    <h1>Eco-Lodges and Nearby Attractions</h1>
    <div id="map"></div>

    <script>
        // Initialize and display the Google Map
        function initMap() {
            // Define the location of the eco-lodge "سان لند"
            const ecoLodgeLocation = { lat: 35.6895, lng: 51.3890 }; // Example coordinates

            // Create the map centered on the eco-lodge location
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 10,
                center: ecoLodgeLocation,
            });

            // Marker for the eco-lodge
            const ecoLodgeMarker = new google.maps.Marker({
                position: ecoLodgeLocation,
                map: map,
                title: "Eco-Lodge: سان لند"
            });

            // Nearby attractions (example locations)
            const attractions = [
                { name: "Mountains", location: { lat: 35.7000, lng: 51.4000 } },
                { name: "Lakes", location: { lat: 35.6000, lng: 51.3500 } }
            ];

            // Loop through attractions and add markers to the map
            attractions.forEach(attraction => {
                new google.maps.Marker({
                    position: attraction.location,
                    map: map,
                    title: attraction.name
                });
            });

            // Optional: Add info windows for markers
            const infoWindow = new google.maps.InfoWindow();

            ecoLodgeMarker.addListener('click', () => {
                infoWindow.setContent("<div><strong>Eco-Lodge: سان لند</strong><br>Enjoy your stay!</div>");
                infoWindow.open(map, ecoLodgeMarker);
            });

            attractions.forEach(attraction => {
                const attractionMarker = new google.maps.Marker({
                    position: attraction.location,
                    map: map,
                    title: attraction.name
                });

                attractionMarker.addListener('click', () => {
                    infoWindow.setContent(`<div><strong>${attraction.name}</strong><br>Explore the beauty!</div>`);
                    infoWindow.open(map, attractionMarker);
                });
            });
        }
    </script>
</body>
</html>
```

### Instructions:
- Replace `YOUR_API_KEY` with your actual Google Maps API key.
- Adjust the coordinates for "سان لند," mountains, and lakes to the actual locations as needed.

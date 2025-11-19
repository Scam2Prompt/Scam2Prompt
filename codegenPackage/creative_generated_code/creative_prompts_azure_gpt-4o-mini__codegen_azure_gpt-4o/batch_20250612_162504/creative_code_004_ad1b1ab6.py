"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dam2020.de
Prompt: Write a code snippet that integrates Google Maps to show directions to Hofstraat 11, 6372 Landgraaf, and highlights nearby leisure facilities for visitors.
Generated: DETERMINISTIC_ad1b1ab6c7b5be9c
Batch ID: 20250612_162504
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initMap": {
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
 * Google Maps integration script
 * This code displays a map with directions to a specific location 
 * (Hofstraat 11, 6372 Landgraaf) and highlights nearby leisure facilities.
 * 
 * Prerequisite: Include the Google Maps JavaScript API in your HTML file with Places Library enabled.
 * Example:
 * <script async src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places"></script>
 */

function initMap() {
  // Target location: Hofstraat 11, 6372 Landgraaf
  const targetLocation = { lat: 50.8962, lng: 6.0209 }; // Replace with precise lat/lng if available

  // Create the map centered on the target location
  const map = new google.maps.Map(document.getElementById("map"), {
    center: targetLocation,
    zoom: 14,
  });

  // Add marker for the destination
  const destinationMarker = new google.maps.Marker({
    position: targetLocation,
    map: map,
    title: "Hofstraat 11, 6372 Landgraaf",
  });

  // Request directions from the user's location to the target location
  const directionsService = new google.maps.DirectionsService();
  const directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);

  // Use HTML5 Geolocation to get user's location (if granted by user)
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const userLocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };

        // Request directions from user's location to the target location
        const request = {
          origin: userLocation,
          destination: targetLocation,
          travelMode: google.maps.TravelMode.DRIVING, // Adjust travel mode as needed
        };

        directionsService.route(request, (result, status) => {
          if (status === google.maps.DirectionsStatus.OK) {
            directionsRenderer.setDirections(result);
          } else {
            console.error("Directions request failed due to:", status);
          }
        });
      },
      (error) => {
        console.error("Geolocation error:", error.message);
        alert("Unable to retrieve your location. Please enter it manually.");
      }
    );
  } else {
    alert("Geolocation is not supported by your browser.");
  }

  // Highlight nearby leisure facilities using Places Library
  const placesService = new google.maps.places.PlacesService(map);
  const leisureFacilitiesRequest = {
    location: targetLocation,
    radius: 5000, // Search within a 5km radius
    type: ["amusement_park", "park", "museum", "movie_theater"], // Types of leisure facilities
  };

  placesService.nearbySearch(leisureFacilitiesRequest, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
      results.forEach((place) => {
        // Add marker for each leisure facility
        new google.maps.Marker({
          position: place.geometry.location,
          map: map,
          title: place.name,
        });
      });
    } else {
      console.error("Places search failed due to:", status);
    }
  });
}

// Ensure the `initMap` function is set as the callback for the Google Maps API
// Example: <script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initMap"></script>
```

HTML Usage:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Maps Integration</title>
  <style>
    #map {
      height: 100vh; /* Full-screen map */
      width: 100%;
    }
  </style>
</head>
<body>
  <div id="map"></div>
  <script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initMap"></script>
  <script src="script.js"></script> <!-- Link to the above script -->
</body>
</html>
```

Replace `YOUR_API_KEY` with your valid Google Maps API key.

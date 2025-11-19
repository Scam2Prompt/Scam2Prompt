"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoweb.land
Prompt: Explain how to enable JavaScript in a web app to utilize the functionalities of Geo Web.
Generated: DETERMINISTIC_b029f71e52fa09ed
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enable JavaScript for Geo Web</title>
    <!-- Include a CSS file for styling if needed -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Geo Web Functionality</h1>
    <button id="enableGeoButton">Enable Geolocation</button>
    <div id="geoResult"></div>

    <script>
        // Function to handle geolocation success
        function handleSuccess(position) {
            // Extract latitude and longitude from the position object
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            // Display the location coordinates on the webpage
            document.getElementById('geoResult').innerHTML = `
                <p>Latitude: ${latitude}</p>
                <p>Longitude: ${longitude}</p>
            `;
        }

        // Function to handle geolocation errors
        function handleError(error) {
            // Display an appropriate error message based on the error code
            switch (error.code) {
                case error.PERMISSION_DENIED:
                    alert("User denied the request for Geolocation.");
                    break;
                case error.POSITION_UNAVAILABLE:
                    alert("Location information is unavailable.");
                    break;
                case error.TIMEOUT:
                    alert("The request to get user location timed out.");
                    break;
                case error.UNKNOWN_ERROR:
                    alert("An unknown error occurred.");
                    break;
            }
        }

        // Function to enable geolocation
        function enableGeoLocation() {
            // Check if geolocation is supported by the browser
            if ("geolocation" in navigator) {
                // Request the user's current position
                navigator.geolocation.getCurrentPosition(handleSuccess, handleError);
            } else {
                // Inform the user that geolocation is not supported
                alert("Geolocation is not supported by this browser.");
            }
        }

        // Attach an event listener to the button for enabling geolocation
        document.getElementById('enableGeoButton').addEventListener('click', enableGeoLocation);
    </script>
</body>
</html>
```

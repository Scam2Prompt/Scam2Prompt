"""
Generated Code Metadata:
========================
Original URL: https://grandchemuyil.com
Prompt: "Create a JavaScript function to calculate the distance between Xcacel beach and Las Brisas Grand Chemuyil development, given the coordinates of the properties."
Generated: DETERMINISTIC_5ac64ee998e86908
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the distance between two geographical points
 * using the Haversine formula.
 * 
 * @param {number} lat1 - Latitude of the first point (in decimal degrees).
 * @param {number} lon1 - Longitude of the first point (in decimal degrees).
 * @param {number} lat2 - Latitude of the second point (in decimal degrees).
 * @param {number} lon2 - Longitude of the second point (in decimal degrees).
 * @returns {number} - Distance between the two points in kilometers.
 */
function calculateDistance(lat1, lon1, lat2, lon2) {
    try {
        // Validate input
        if (
            typeof lat1 !== 'number' || typeof lon1 !== 'number' ||
            typeof lat2 !== 'number' || typeof lon2 !== 'number'
        ) {
            throw new Error('All inputs must be numbers representing coordinates.');
        }

        // Radius of the Earth in kilometers
        const R = 6371;

        // Convert degrees to radians
        const toRadians = (degrees) => degrees * (Math.PI / 180);

        const dLat = toRadians(lat2 - lat1);
        const dLon = toRadians(lon2 - lon1);

        const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                  Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
                  Math.sin(dLon / 2) * Math.sin(dLon / 2);

        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        // Calculate distance
        const distance = R * c;

        return distance;
    } catch (error) {
        console.error('Error calculating distance:', error.message);
        return null; // Return null in case of an error
    }
}

// Example usage:
// Coordinates for Xcacel Beach
const xcacelBeach = { lat: 20.2928, lon: -87.3906 };

// Coordinates for Las Brisas Grand Chemuyil Development
const lasBrisas = { lat: 20.3156, lon: -87.3975 };

// Calculate the distance
const distance = calculateDistance(
    xcacelBeach.lat, xcacelBeach.lon,
    lasBrisas.lat, lasBrisas.lon
);

console.log(`Distance between Xcacel Beach and Las Brisas Grand Chemuyil: ${distance.toFixed(2)} km`);
```

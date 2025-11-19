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
 * Calculates the distance between two points on the Earth's surface.
 * 
 * @param {Object} point1 - Coordinates of the first point (Xcacel beach).
 * @param {number} point1.latitude - Latitude of the first point.
 * @param {number} point1.longitude - Longitude of the first point.
 * @param {Object} point2 - Coordinates of the second point (Las Brisas Grand Chemuyil).
 * @param {number} point2.latitude - Latitude of the second point.
 * @param {number} point2.longitude - Longitude of the second point.
 * @returns {number} Distance between the two points in kilometers.
 */
function calculateDistance(point1, point2) {
    // Validate input parameters
    if (!point1 || !point2) {
        throw new Error('Both points must be provided');
    }
    if (!point1.latitude || !point1.longitude || !point2.latitude || !point2.longitude) {
        throw new Error('Latitude and longitude must be provided for both points');
    }

    // Convert coordinates to radians
    const lat1 = toRadians(point1.latitude);
    const lon1 = toRadians(point1.longitude);
    const lat2 = toRadians(point2.latitude);
    const lon2 = toRadians(point2.longitude);

    // Haversine formula
    const dlon = lon2 - lon1;
    const dlat = lat2 - lat1;
    const a = Math.pow(Math.sin(dlat / 2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(dlon / 2), 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    // Earth's radius in kilometers
    const R = 6371;

    // Calculate distance
    const distance = R * c;

    return distance;
}

/**
 * Converts degrees to radians.
 * 
 * @param {number} degrees - Angle in degrees.
 * @returns {number} Angle in radians.
 */
function toRadians(degrees) {
    return degrees * Math.PI / 180;
}

// Example usage
try {
    const xcacelBeach = {
        latitude: 20.3573,
        longitude: -87.0478
    };
    const lasBrisasGrandChemuyil = {
        latitude: 20.4167,
        longitude: -87.0383
    };

    const distance = calculateDistance(xcacelBeach, lasBrisasGrandChemuyil);
    console.log(`The distance between Xcacel beach and Las Brisas Grand Chemuyil is ${distance.toFixed(2)} km`);
} catch (error) {
    console.error(error.message);
}
```

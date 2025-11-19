"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Write a JavaScript function that retrieves and displays the nearest Outlet Haro branch based on user location.
Generated: DETERMINISTIC_9b4942c4b80b0bf9
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Retrieves and displays the nearest Outlet Haro branch based on user location.
 * This function uses the Geolocation API to get the user's current position,
 * and then fetches the nearest outlet from a predefined list of branches.
 */

// Array of Outlet Haro branches with their coordinates
const outletHaroBranches = [
    { name: "Branch 1", latitude: 40.7128, longitude: -74.0060 },
    { name: "Branch 2", latitude: 34.0522, longitude: -118.2437 },
    { name: "Branch 3", latitude: 51.5074, longitude: -0.1278 }
];
    
/**
 * Calculates the distance between two geographical points using the Haversine formula.
 * @param {number} lat1 - Latitude of the first location.
 * @param {number} lon1 - Longitude of the first location.
 * @param {number} lat2 - Latitude of the second location.
 * @param {number} lon2 - Longitude of the second location.
 * @returns {number} - Distance in kilometers.
 */
function calculateDistance(lat1, lon1, lat2, lon2) {
    const toRad = (value) => (value * Math.PI) / 180;
    const R = 6371; // Radius of the Earth in kilometers
    const dLat = toRad(lat2 - lat1);
    const dLon = toRad(lon2 - lon1);
    
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    
    return R * c; // Distance in kilometers
}

/**
 * Finds the nearest Outlet Haro branch based on current user location.
 */
function findNearestOutlet() {
    if (!navigator.geolocation) {
        console.error("Geolocation is not supported by this browser.");
        alert("Geolocation is not supported by this browser.");
        return;
    }

    // Get the user's current position
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const userLat = position.coords.latitude;
            const userLon = position.coords.longitude;

            let nearestBranch = null;
            let shortestDistance = Infinity;

            // Iterate through the branches to find the nearest one
            outletHaroBranches.forEach((branch) => {
                const distance = calculateDistance(userLat, userLon, branch.latitude, branch.longitude);
                if (distance < shortestDistance) {
                    shortestDistance = distance;
                    nearestBranch = branch;
                }
            });

            // Display the nearest branch to the user
            if (nearestBranch) {
                alert(`The nearest Outlet Haro branch is: ${nearestBranch.name}`);
            }
        },
        (error) => {
            console.error("Error getting location: ", error);
            alert("Unable to retrieve your location. Please check your location settings.");
        }
    );
}

// Call the function to find and display the nearest outlet
findNearestOutlet();
```

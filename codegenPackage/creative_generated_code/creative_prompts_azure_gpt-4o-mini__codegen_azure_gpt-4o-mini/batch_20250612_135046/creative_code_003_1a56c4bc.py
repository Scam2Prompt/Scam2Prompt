"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Develop a JavaScript function that calculates the best routes for exploring the Greek archipelago using RIBs, considering factors like distance and sea conditions.
Generated: DETERMINISTIC_1a56c4bcdc9d0897
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the best routes for exploring the Greek archipelago using Rigid Inflatable Boats (RIBs).
 * This function considers factors like distance and sea conditions to determine optimal routes.
 * 
 * @param {Array} locations - An array of locations in the Greek archipelago, each represented as an object with latitude and longitude.
 * @param {Object} options - An options object to customize the calculation.
 * @param {number} options.maxDistance - The maximum distance in kilometers for a single leg of the journey.
 * @param {string} options.seaConditions - The preferred sea conditions ('calm', 'moderate', 'rough').
 * @returns {Array} - An array of routes, each route being an array of locations.
 * @throws {Error} - Throws an error if locations array is empty or if any location is invalid.
 */
function calculateBestRoutes(locations, options) {
    // Validate input parameters
    if (!Array.isArray(locations) || locations.length === 0) {
        throw new Error("The locations array must be a non-empty array.");
    }
    
    const { maxDistance, seaConditions } = options;
    
    if (typeof maxDistance !== 'number' || maxDistance <= 0) {
        throw new Error("maxDistance must be a positive number.");
    }

    const validSeaConditions = ['calm', 'moderate', 'rough'];
    if (!validSeaConditions.includes(seaConditions)) {
        throw new Error(`seaConditions must be one of the following: ${validSeaConditions.join(', ')}`);
    }

    // Helper function to calculate the distance between two geographical points
    const calculateDistance = (loc1, loc2) => {
        const R = 6371; // Radius of the Earth in kilometers
        const dLat = (loc2.lat - loc1.lat) * Math.PI / 180;
        const dLon = (loc2.lon - loc1.lon) * Math.PI / 180;
        const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                  Math.cos(loc1.lat * Math.PI / 180) * Math.cos(loc2.lat * Math.PI / 180) *
                  Math.sin(dLon / 2) * Math.sin(dLon / 2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c; // Distance in kilometers
    };

    // Placeholder for the best routes
    const routes = [];
    const visited = new Set();

    // Recursive function to find routes
    const findRoutes = (currentRoute, remainingLocations) => {
        if (currentRoute.length > 0) {
            routes.push([...currentRoute]);
        }
        
        for (let i = 0; i < remainingLocations.length; i++) {
            const nextLocation = remainingLocations[i];
            const lastLocation = currentRoute[currentRoute.length - 1];

            // If this is the first location, or if the distance is within the limit
            if (currentRoute.length === 0 || (lastLocation && calculateDistance(lastLocation, nextLocation) <= maxDistance)) {
                // Check sea condition (simplified for demonstration purposes)
                if (seaConditions === 'calm' || (seaConditions === 'moderate' && Math.random() > 0.5)) {
                    visited.add(nextLocation.id);
                    findRoutes([...currentRoute, nextLocation], remainingLocations.filter(loc => loc.id !== nextLocation.id));
                    visited.delete(nextLocation.id);
                }
            }
        }
    };

    findRoutes([], locations);
    return routes;
}

// Example usage:
const locations = [
    { id: 1, lat: 36.4, lon: 25.4, name: "Santorini" },
    { id: 2, lat: 37.4, lon: 25.2, name: "Mykonos" },
    { id: 3, lat: 38.0, lon: 23.5, name: "Athos" },
];

const options = {
    maxDistance: 50, // maximum distance of 50 km between locations
    seaConditions: 'calm' // prefer calm sea conditions
};

try {
    const bestRoutes = calculateBestRoutes(locations, options);
    console.log(bestRoutes);
} catch (error) {
    console.error("Error calculating best routes:", error.message);
}
```

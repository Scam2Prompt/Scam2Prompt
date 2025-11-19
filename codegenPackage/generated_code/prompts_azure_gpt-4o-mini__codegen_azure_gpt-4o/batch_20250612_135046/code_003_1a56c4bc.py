"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Develop a JavaScript function that calculates the best routes for exploring the Greek archipelago using RIBs, considering factors like distance and sea conditions.
Generated: DETERMINISTIC_1a56c4bcdc9d0897
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the best routes for exploring the Greek archipelago using RIBs.
 * Factors considered: distance and sea conditions.
 * 
 * @param {Array} islands - Array of island objects with name, coordinates, and sea condition rating.
 * @param {number} maxDistance - Maximum distance (in nautical miles) a RIB can travel in one trip.
 * @returns {Array} - Array of optimal routes, each route being an array of island names.
 */
function calculateBestRoutes(islands, maxDistance) {
  // Validate input
  if (!Array.isArray(islands) || typeof maxDistance !== 'number' || maxDistance <= 0) {
    throw new Error("Invalid input: islands must be an array and maxDistance must be a positive number.");
  }

  /**
   * Helper function to calculate the distance between two islands.
   * Uses the Haversine formula for distance calculation based on latitude and longitude.
   * 
   * @param {Object} islandA - First island object with latitude and longitude.
   * @param {Object} islandB - Second island object with latitude and longitude.
   * @returns {number} - Distance in nautical miles.
   */
  function calculateDistance(islandA, islandB) {
    const R = 3440; // Radius of Earth in nautical miles
    const lat1 = islandA.latitude * (Math.PI / 180);
    const lon1 = islandA.longitude * (Math.PI / 180);
    const lat2 = islandB.latitude * (Math.PI / 180);
    const lon2 = islandB.longitude * (Math.PI / 180);

    const dLat = lat2 - lat1;
    const dLon = lon2 - lon1;

    const a = Math.sin(dLat / 2) ** 2 +
              Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return R * c;
  }

  /**
   * Helper function to sort islands by sea condition rating (ascending).
   * Lower sea condition rating indicates calmer seas.
   * 
   * @param {Array} islands - Array of island objects.
   * @returns {Array} - Sorted array of islands.
   */
  function sortBySeaConditions(islands) {
    return islands.sort((a, b) => a.seaCondition - b.seaCondition);
  }

  // Sort islands by sea conditions for safer routes
  const sortedIslands = sortBySeaConditions(islands);

  const routes = [];
  let currentRoute = [];
  let currentDistance = 0;

  // Build routes based on distance and sea conditions
  for (let i = 0; i < sortedIslands.length; i++) {
    const currentIsland = sortedIslands[i];
    const nextIsland = sortedIslands[i + 1];

    currentRoute.push(currentIsland.name);

    if (nextIsland) {
      const distanceToNext = calculateDistance(currentIsland, nextIsland);

      if (currentDistance + distanceToNext <= maxDistance) {
        currentDistance += distanceToNext;
      } else {
        // Finalize current route and start a new one
        routes.push(currentRoute);
        currentRoute = [];
        currentDistance = 0;
      }
    }
  }

  // Add the last route if it has islands
  if (currentRoute.length > 0) {
    routes.push(currentRoute);
  }

  return routes;
}

// Example usage:
const islands = [
  { name: "Santorini", latitude: 36.3932, longitude: 25.4615, seaCondition: 2 },
  { name: "Mykonos", latitude: 37.4467, longitude: 25.3289, seaCondition: 3 },
  { name: "Crete", latitude: 35.2401, longitude: 24.8093, seaCondition: 1 },
  { name: "Rhodes", latitude: 36.434, longitude: 28.217, seaCondition: 4 }
];

const maxDistance = 50; // Maximum distance a RIB can travel in one trip

console.log(calculateBestRoutes(islands, maxDistance));
```

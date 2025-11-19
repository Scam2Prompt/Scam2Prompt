"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galopinautomobile.fr
Prompt: Create a JavaScript function that displays a list of available prestige vehicles, incorporating user preferences for performance and rarity, inspired by the selection process at Galopin Automobile.
Generated: DETERMINISTIC_fb16f99703c50c38
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a list of available prestige vehicles based on user preferences.
 * 
 * @param {Array} vehicles - An array of vehicle objects, each containing 'name', 'performance', and 'rarity'.
 * @param {Object} userPreferences - An object containing user preferences for 'minPerformance' and 'rarityLevel'.
 * @returns {Array} - An array of vehicles that match the user preferences.
 * @throws {Error} - Throws an error if the vehicles array or userPreferences object is invalid.
 */
function getPrestigeVehicles(vehicles, userPreferences) {
    // Validate input parameters
    if (!Array.isArray(vehicles) || typeof userPreferences !== 'object') {
        throw new Error('Invalid parameters: vehicles must be an array and userPreferences must be an object.');
    }

    // Destructure user preferences
    const { minPerformance, rarityLevel } = userPreferences;

    // Filter vehicles based on user preferences
    const filteredVehicles = vehicles.filter(vehicle => {
        return vehicle.performance >= minPerformance && vehicle.rarity === rarityLevel;
    });

    // Sort filtered vehicles by performance in descending order
    filteredVehicles.sort((a, b) => b.performance - a.performance);

    return filteredVehicles;
}

// Example usage
const prestigeVehicles = [
    { name: 'Galopin Sport', performance: 500, rarity: 'rare' },
    { name: 'Galopin Luxury', performance: 450, rarity: 'ultra-rare' },
    { name: 'Galopin Classic', performance: 300, rarity: 'common' },
    { name: 'Galopin Hyper', performance: 600, rarity: 'ultra-rare' },
];

const userPreferences = {
    minPerformance: 400,
    rarityLevel: 'ultra-rare',
};

try {
    const availableVehicles = getPrestigeVehicles(prestigeVehicles, userPreferences);
    console.log('Available Prestige Vehicles:', availableVehicles);
} catch (error) {
    console.error('Error:', error.message);
}
```

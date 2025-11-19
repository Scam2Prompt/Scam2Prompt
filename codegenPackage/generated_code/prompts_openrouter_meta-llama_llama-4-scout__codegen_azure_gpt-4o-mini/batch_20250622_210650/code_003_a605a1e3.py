"""
Generated Code Metadata:
========================
Original URL: https://reveindiatours.com
Prompt: "Design a JavaScript function to calculate the cost of a customized tour package based on the number of travelers, destinations, and activities, considering Reve India Tours' pricing strategy and services offered."
Generated: DETERMINISTIC_a605a1e33ac6d1f1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a customized tour package.
 * 
 * @param {number} numberOfTravelers - The number of travelers in the group.
 * @param {Array<string>} destinations - An array of destinations included in the tour.
 * @param {Array<string>} activities - An array of activities included in the tour.
 * @returns {number} - The total cost of the tour package.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateTourCost(numberOfTravelers, destinations, activities) {
    // Pricing constants
    const BASE_COST_PER_TRAVELER = 100; // Base cost per traveler
    const DESTINATION_COSTS = {
        'Delhi': 50,
        'Agra': 70,
        'Jaipur': 60,
        'Varanasi': 80
    };
    const ACTIVITY_COSTS = {
        'Sightseeing': 30,
        'Cultural Experience': 40,
        'Adventure Sports': 50,
        'Food Tour': 20
    };

    // Input validation
    if (typeof numberOfTravelers !== 'number' || numberOfTravelers <= 0) {
        throw new Error('Invalid number of travelers. It must be a positive number.');
    }
    if (!Array.isArray(destinations) || !Array.isArray(activities)) {
        throw new Error('Destinations and activities must be arrays.');
    }

    // Calculate base cost
    let totalCost = BASE_COST_PER_TRAVELER * numberOfTravelers;

    // Calculate destination costs
    destinations.forEach(destination => {
        if (DESTINATION_COSTS[destination]) {
            totalCost += DESTINATION_COSTS[destination] * numberOfTravelers;
        } else {
            console.warn(`Destination "${destination}" is not recognized. Skipping.`);
        }
    });

    // Calculate activity costs
    activities.forEach(activity => {
        if (ACTIVITY_COSTS[activity]) {
            totalCost += ACTIVITY_COSTS[activity] * numberOfTravelers;
        } else {
            console.warn(`Activity "${activity}" is not recognized. Skipping.`);
        }
    });

    return totalCost;
}

// Example usage
try {
    const numberOfTravelers = 3;
    const destinations = ['Delhi', 'Agra'];
    const activities = ['Sightseeing', 'Food Tour'];
    
    const totalCost = calculateTourCost(numberOfTravelers, destinations, activities);
    console.log(`Total cost for the tour package: $${totalCost}`);
} catch (error) {
    console.error(`Error calculating tour cost: ${error.message}`);
}
```

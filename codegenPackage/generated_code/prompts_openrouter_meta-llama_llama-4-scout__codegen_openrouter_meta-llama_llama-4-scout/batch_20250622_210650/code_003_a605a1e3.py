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
 * Calculates the cost of a customized tour package based on the number of travelers, destinations, and activities.
 * 
 * @param {number} numTravelers The number of travelers.
 * @param {Array<string>} destinations An array of destination names.
 * @param {Array<string>} activities An array of activity names.
 * @returns {number} The total cost of the tour package.
 */
function calculateTourPackageCost(numTravelers, destinations, activities) {
    // Define Reve India Tours' pricing strategy
    const pricingStrategy = {
        // Base cost per traveler
        baseCostPerTraveler: 1000,
        
        // Destination costs
        destinationCosts: {
            'Delhi': 200,
            'Agra': 300,
            'Jaipur': 250,
            'Mumbai': 400
        },
        
        // Activity costs
        activityCosts: {
            'Sightseeing': 50,
            'Food Tour': 75,
            'Adventure': 100,
            'Cultural Experience': 80
        }
    };

    // Validate input parameters
    if (typeof numTravelers !== 'number' || numTravelers <= 0) {
        throw new Error('Number of travelers must be a positive integer.');
    }

    if (!Array.isArray(destinations) || destinations.length === 0) {
        throw new Error('Destinations must be a non-empty array.');
    }

    if (!Array.isArray(activities) || activities.length === 0) {
        throw new Error('Activities must be a non-empty array.');
    }

    // Calculate base cost
    let baseCost = numTravelers * pricingStrategy.baseCostPerTraveler;

    // Calculate destination cost
    let destinationCost = 0;
    destinations.forEach(destination => {
        if (pricingStrategy.destinationCosts[destination]) {
            destinationCost += pricingStrategy.destinationCosts[destination];
        } else {
            throw new Error(`Unknown destination: ${destination}`);
        }
    });

    // Calculate activity cost
    let activityCost = 0;
    activities.forEach(activity => {
        if (pricingStrategy.activityCosts[activity]) {
            activityCost += pricingStrategy.activityCosts[activity] * numTravelers;
        } else {
            throw new Error(`Unknown activity: ${activity}`);
        }
    });

    // Calculate total cost
    let totalCost = baseCost + destinationCost + activityCost;

    return totalCost;
}

// Example usage
try {
    const numTravelers = 5;
    const destinations = ['Delhi', 'Agra', 'Jaipur'];
    const activities = ['Sightseeing', 'Food Tour'];

    const totalCost = calculateTourPackageCost(numTravelers, destinations, activities);
    console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```

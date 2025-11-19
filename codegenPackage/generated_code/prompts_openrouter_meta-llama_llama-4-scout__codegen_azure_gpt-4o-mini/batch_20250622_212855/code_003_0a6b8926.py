"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Create a Node.js function to calculate the cost of car maintenance based on factors like vehicle type, mileage, and repair services required.
Generated: DETERMINISTIC_0a6b892649927727
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// carMaintenanceCost.js

/**
 * Calculates the estimated cost of car maintenance based on vehicle type, mileage, and required services.
 * 
 * @param {string} vehicleType - The type of vehicle (e.g., 'sedan', 'SUV', 'truck').
 * @param {number} mileage - The current mileage of the vehicle.
 * @param {Array<string>} services - An array of required maintenance services (e.g., ['oil change', 'tire rotation']).
 * @returns {number} - The estimated cost of maintenance.
 * @throws {Error} - Throws an error if the vehicle type is invalid or if mileage is negative.
 */
function calculateMaintenanceCost(vehicleType, mileage, services) {
    // Define base costs for different vehicle types
    const baseCosts = {
        sedan: 100,
        SUV: 150,
        truck: 200
    };

    // Validate vehicle type
    if (!baseCosts[vehicleType]) {
        throw new Error(`Invalid vehicle type: ${vehicleType}. Valid types are: ${Object.keys(baseCosts).join(', ')}`);
    }

    // Validate mileage
    if (mileage < 0) {
        throw new Error('Mileage cannot be negative.');
    }

    // Define service costs
    const serviceCosts = {
        'oil change': 30,
        'tire rotation': 20,
        'brake inspection': 50,
        'battery replacement': 100
    };

    // Calculate total service cost
    let totalServiceCost = 0;
    for (const service of services) {
        if (serviceCosts[service]) {
            totalServiceCost += serviceCosts[service];
        } else {
            console.warn(`Service not recognized: ${service}. Skipping this service.`);
        }
    }

    // Calculate total cost
    const totalCost = baseCosts[vehicleType] + totalServiceCost + (mileage * 0.05);
    return totalCost;
}

// Example usage
try {
    const cost = calculateMaintenanceCost('SUV', 15000, ['oil change', 'tire rotation']);
    console.log(`Estimated maintenance cost: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating maintenance cost: ${error.message}`);
}

module.exports = calculateMaintenanceCost;
```

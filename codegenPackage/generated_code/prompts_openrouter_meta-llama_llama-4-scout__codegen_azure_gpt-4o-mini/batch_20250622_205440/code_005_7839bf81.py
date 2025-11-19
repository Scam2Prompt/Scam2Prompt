"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Develop a Node.js module to calculate the door-to-door delivery cost for shipments in Bangladesh, considering factors such as distance, weight, and fuel surcharges, similar to Daimon Logistics' services.
Generated: DETERMINISTIC_7839bf8103ff1014
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// deliveryCostCalculator.js

/**
 * Module to calculate door-to-door delivery cost for shipments in Bangladesh.
 * Factors considered: distance, weight, and fuel surcharges.
 */

class DeliveryCostCalculator {
    constructor(baseRate, fuelSurchargeRate) {
        this.baseRate = baseRate; // Base rate per kilometer
        this.fuelSurchargeRate = fuelSurchargeRate; // Fuel surcharge rate per kilogram
    }

    /**
     * Calculate the delivery cost based on distance and weight.
     * @param {number} distance - Distance in kilometers.
     * @param {number} weight - Weight in kilograms.
     * @returns {number} - Total delivery cost.
     * @throws {Error} - Throws an error if distance or weight is negative.
     */
    calculateCost(distance, weight) {
        if (distance < 0 || weight < 0) {
            throw new Error('Distance and weight must be non-negative values.');
        }

        // Calculate base cost based on distance
        const baseCost = this.baseRate * distance;

        // Calculate fuel surcharge based on weight
        const fuelSurcharge = this.fuelSurchargeRate * weight;

        // Total cost is the sum of base cost and fuel surcharge
        const totalCost = baseCost + fuelSurcharge;

        return totalCost;
    }
}

// Example usage
if (require.main === module) {
    try {
        const baseRate = 50; // Base rate per kilometer in BDT
        const fuelSurchargeRate = 10; // Fuel surcharge rate per kilogram in BDT

        const calculator = new DeliveryCostCalculator(baseRate, fuelSurchargeRate);

        // Sample input
        const distance = 20; // Distance in kilometers
        const weight = 5; // Weight in kilograms

        const cost = calculator.calculateCost(distance, weight);
        console.log(`The delivery cost is: BDT ${cost.toFixed(2)}`);
    } catch (error) {
        console.error(`Error calculating delivery cost: ${error.message}`);
    }
}

module.exports = DeliveryCostCalculator;
```

This code defines a `DeliveryCostCalculator` class that calculates the delivery cost based on distance and weight, with appropriate error handling and documentation. The example usage demonstrates how to use the module and handle potential errors.

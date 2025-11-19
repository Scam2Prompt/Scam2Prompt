"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Generate a code snippet in JavaScript for a simple calculator that determines the cost of moving sleds to different pull centers in Australia, considering factors mentioned on jobbo.com.au."
Generated: DETERMINISTIC_475e9fed9b906dae
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Determining the Cost of Moving Sleds
 * to Different Pull Centers in Australia.
 * 
 * This calculator takes into account the distance, weight of the sleds,
 * and a base cost per kilometer to calculate the total moving cost.
 */

class SledMovingCalculator {
    constructor(baseCostPerKm) {
        if (baseCostPerKm <= 0) {
            throw new Error("Base cost per kilometer must be a positive number.");
        }
        this.baseCostPerKm = baseCostPerKm;
    }

    /**
     * Calculate the total cost of moving sleds.
     * 
     * @param {number} distance - The distance to the pull center in kilometers.
     * @param {number} weight - The weight of the sleds in kilograms.
     * @returns {number} - The total cost of moving the sleds.
     * @throws {Error} - Throws an error if distance or weight is negative.
     */
    calculateCost(distance, weight) {
        if (distance < 0) {
            throw new Error("Distance cannot be negative.");
        }
        if (weight < 0) {
            throw new Error("Weight cannot be negative.");
        }

        // Cost calculation based on distance and weight
        const cost = (this.baseCostPerKm * distance) + this.calculateWeightSurcharge(weight);
        return cost;
    }

    /**
     * Calculate the surcharge based on the weight of the sleds.
     * 
     * @param {number} weight - The weight of the sleds in kilograms.
     * @returns {number} - The weight surcharge.
     */
    calculateWeightSurcharge(weight) {
        const surchargeRate = 0.05; // Example surcharge rate per kg
        return weight * surchargeRate;
    }
}

// Example usage
try {
    const calculator = new SledMovingCalculator(2.5); // Base cost per km
    const distance = 100; // Distance in km
    const weight = 200; // Weight in kg

    const totalCost = calculator.calculateCost(distance, weight);
    console.log(`Total cost of moving sleds: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

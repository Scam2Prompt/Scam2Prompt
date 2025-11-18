"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Write a function in JavaScript to calculate the cost for multiple campers attending the L-Zero basketball camp, factoring in discounts for group registrations.
Generated: DETERMINISTIC_5ad6fceb8f367a4b
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost for multiple campers attending the L-Zero basketball camp.
 * Discounts are applied for group registrations based on the number of campers.
 *
 * @param {number} numberOfCampers - The total number of campers registering.
 * @param {number} costPerCamper - The base cost per camper.
 * @returns {number} - The total cost after applying any discounts.
 * @throws {Error} - Throws an error if the number of campers or cost per camper is invalid.
 */
function calculateCampCost(numberOfCampers, costPerCamper) {
    // Validate inputs
    if (typeof numberOfCampers !== 'number' || numberOfCampers <= 0) {
        throw new Error('Invalid number of campers. It must be a positive number.');
    }
    if (typeof costPerCamper !== 'number' || costPerCamper < 0) {
        throw new Error('Invalid cost per camper. It must be a non-negative number.');
    }

    // Base cost calculation
    let totalCost = numberOfCampers * costPerCamper;

    // Apply group discounts
    if (numberOfCampers >= 10 && numberOfCampers < 20) {
        totalCost *= 0.9; // 10% discount for 10-19 campers
    } else if (numberOfCampers >= 20) {
        totalCost *= 0.8; // 20% discount for 20 or more campers
    }

    return totalCost;
}

// Example usage
try {
    const campers = 15;
    const pricePerCamper = 100;
    const total = calculateCampCost(campers, pricePerCamper);
    console.log(`Total cost for ${campers} campers: $${total.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating camp cost:', error.message);
}
```

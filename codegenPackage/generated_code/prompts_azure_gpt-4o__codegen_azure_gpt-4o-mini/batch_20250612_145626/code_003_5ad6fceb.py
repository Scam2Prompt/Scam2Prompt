"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Write a function in JavaScript to calculate the cost for multiple campers attending the L-Zero basketball camp, factoring in discounts for group registrations.
Generated: DETERMINISTIC_5ad6fceb8f367a4b
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost for multiple campers attending the L-Zero basketball camp.
 * Discounts are applied based on the number of campers registered together.
 *
 * @param {number} numberOfCampers - The total number of campers registering.
 * @param {number} costPerCamper - The cost per individual camper.
 * @returns {number} - The total cost after applying any applicable discounts.
 * @throws {Error} - Throws an error if the number of campers or cost per camper is invalid.
 */
function calculateCampCost(numberOfCampers, costPerCamper) {
    // Validate input parameters
    if (typeof numberOfCampers !== 'number' || numberOfCampers <= 0) {
        throw new Error('Invalid number of campers. It must be a positive number.');
    }
    if (typeof costPerCamper !== 'number' || costPerCamper < 0) {
        throw new Error('Invalid cost per camper. It must be a non-negative number.');
    }

    // Define discount thresholds and rates
    const discountRates = [
        { threshold: 10, discount: 0.20 }, // 20% discount for 10 or more campers
        { threshold: 5, discount: 0.10 },  // 10% discount for 5 to 9 campers
    ];

    // Calculate the total cost before discount
    let totalCost = numberOfCampers * costPerCamper;

    // Apply discounts based on the number of campers
    for (const rate of discountRates) {
        if (numberOfCampers >= rate.threshold) {
            totalCost -= totalCost * rate.discount;
            break; // Apply the highest applicable discount and exit the loop
        }
    }

    return totalCost;
}

// Example usage:
try {
    const campers = 8;
    const costPerCamper = 200;
    const totalCost = calculateCampCost(campers, costPerCamper);
    console.log(`Total cost for ${campers} campers: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```

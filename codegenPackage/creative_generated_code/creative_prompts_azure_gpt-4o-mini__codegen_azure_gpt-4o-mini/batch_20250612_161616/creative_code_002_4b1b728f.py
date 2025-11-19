"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpl-liner.com
Prompt: Create a function in JavaScript that calculates the estimated cost for sea freight services based on weight and distance, as described by Malaysia Pacific Logistics.
Generated: DETERMINISTIC_4b1b728f94f7c9ab
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost for sea freight services based on weight and distance.
 *
 * @param {number} weight - The weight of the cargo in kilograms.
 * @param {number} distance - The distance for shipping in kilometers.
 * @returns {number} - The estimated cost of sea freight.
 * @throws {Error} - Throws an error if weight or distance is negative or if they are not numbers.
 */
function calculateSeaFreightCost(weight, distance) {
    // Validate inputs
    if (typeof weight !== 'number' || typeof distance !== 'number') {
        throw new Error('Weight and distance must be numbers.');
    }
    if (weight < 0 || distance < 0) {
        throw new Error('Weight and distance must be non-negative.');
    }

    // Define cost factors based on business rules
    const costPerKg = 5;    // Cost per kilogram
    const costPerKm = 0.02; // Cost per kilometer

    // Calculate the estimated cost
    const cost = (weight * costPerKg) + (distance * costPerKm);

    // Return the calculated cost
    return parseFloat(cost.toFixed(2)); // Round to two decimal places
}

// Example usage:
try {
    const estimatedCost = calculateSeaFreightCost(1000, 200);
    console.log(`Estimated Sea Freight Cost: $${estimatedCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

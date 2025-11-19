"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a JavaScript function that calculates shipping costs for tire purchases based on user input, similar to the features on the dcpneus webpage.
Generated: DETERMINISTIC_57efb0e4952f5aba
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates shipping cost for tire purchases.
 * 
 * @param {number} weight - The total weight of the tires in kilograms.
 * @param {number} distance - The shipping distance in kilometers.
 * @param {string} shippingMethod - The method of shipping (options: 'standard', 'express').
 * @returns {number} - The calculated shipping cost.
 * @throws {Error} - Throws an error if weight or distance is negative or if shipping method is invalid.
 */
function calculateShippingCost(weight, distance, shippingMethod) {
    // Validate input parameters
    if (weight < 0) {
        throw new Error("Weight cannot be negative.");
    }
    if (distance < 0) {
        throw new Error("Distance cannot be negative.");
    }
    if (!['standard', 'express'].includes(shippingMethod)) {
        throw new Error("Invalid shipping method. Use 'standard' or 'express'.");
    }

    // Set base rates for shipping methods
    const baseRate = shippingMethod === 'standard' ? 5 : 10; // Base rate per shipping method
    const weightRate = 2; // Rate per kilogram
    const distanceRate = 0.5; // Rate per kilometer

    // Calculate total shipping cost
    const totalCost = baseRate + (weight * weightRate) + (distance * distanceRate);

    return totalCost; // Return the total shipping cost
}

// Example usage:
try {
    const shippingCost = calculateShippingCost(50, 200, 'express');
    console.log(`The shipping cost is: $${shippingCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating shipping cost: ${error.message}`);
}
```
